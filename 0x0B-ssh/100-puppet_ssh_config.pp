#!/usr/bin/env bash
# using puppet to configure ssh

file { 'etc/ssh/ssh_config':
	ensure => present,

content => "
	#ssh client configuration
	host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
