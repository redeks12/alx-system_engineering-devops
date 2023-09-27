#!/usr/bin/env bash
# using puppet to configure ssh

package { 'nginx':
    ensure => 'installed',
}

file {'/etc/nginx/nginx.conf':
    ensure => 'file',
}

exec { 'allow nginx':
  command  => "sudo ufw allow 'Nginx HTTP'",
  provider => 'shell',
}

file { '/var/www/html/index.html':
    ensure => 'file',
    content => 'Hello World!'
}

class mymodule::nginx {
  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'file',
    content => '
      server {
              listen 80;

              root /var/www/html;

              index index.html index.htm index.nginx-debian.html;

              server_name _;
              rewrite /redirect_me https://www.youtube.com permanent;

              location / {
                  try_files $uri $uri/ =404;
              }
        }
    ',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-enabled/default',
    require => File['/etc/nginx/sites-enabled/default'],
  }
}

exec { 'text nginx':
  command  => "sudo nginx -t",
  provider => 'shell',
}

exec { 'restart nginx':
  command  => "sudo service nginx restart",
  provider => 'shell',
}