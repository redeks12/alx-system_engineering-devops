#!/usr/bin/env bash
# using puppet to configure ssh
include stdlib

file_line { 'add_idetity_file':
	path  			   => '/etc/ssh/ssh_config',
	line               => '		IdentityFile ~/.ssh/school',
	match              => '		# IdentityFile ~/.ssh/school',
	replace            => true,
	append_on_no_match => true,
}

file_line { 'no_auth':
	path  			   => '/etc/ssh/ssh_config',
	line               => '		PasswordAuthentication no',
	match              => '		PasswordAuthentication yes',
	replace            => true,
	append_on_no_match => true,

	
}
