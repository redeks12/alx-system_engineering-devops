# Automating project requirements using Puppet

# package { 'nginx':
#   ensure => installed,
# }
$hostname = $::hostname
notify { "PATH Variable": message => "PATH is $hostname" }

# file_line { 'install':
#   ensure => 'present',
#   path   => '/etc/nginx/sites-enabled/default',
#   after  => 'server_name _;',
#   line   => 'add_header X-Served-By $HOSTNAME;',
# }

# file { '/var/www/html/index.html':
#   content => 'Hello World!',
# }

# service { 'nginx':
#   ensure  => running,
#   require => Package['nginx'],
# }