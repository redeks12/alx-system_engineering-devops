#!/usr/bin/env bash
# using puppet to configure ssh
import stdlib

file_line { 'add_idetity_file':
	path  => '/etc/ssh/ssh_config',
	line  => '		IdentityFile ~/.ssh/school',
	match => '		# IdentityFile ~/.ssh/school',

	PasswordAuthentication no
}

file_line { 'no_auth':
	path  => '/etc/ssh/ssh_config',
	line  => '		PasswordAuthentication no',
	match => '		PasswordAuthentication yes',

	
}
