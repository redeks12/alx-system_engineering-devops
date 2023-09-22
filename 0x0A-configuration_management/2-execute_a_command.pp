# Using Puppet, create a manifest that kills a process named killmenow

exec { 'terminate_killmenow':
  command => 'pkill killmenow'
}
