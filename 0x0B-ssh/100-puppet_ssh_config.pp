#!/usr/bin/env bash
# using puppet to configure ssh

file { 'ect/ssh/ssh_cofig':
	ensure  => present,

content => "
	#ssh client configuration
	host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
