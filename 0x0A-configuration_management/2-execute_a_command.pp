# This Puppet maifest kill a process named killmenow
exec { 'kill killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => ['/bin/', '/usr/bin/'],
}
