# This Puppet manifest install flask version 2.1.0
exec { 'install flask 2.1.0':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin/'],
}
