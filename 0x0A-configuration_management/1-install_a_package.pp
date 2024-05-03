# This Puppet manifest install flask version 2.1.0
exec { 'install flask 2.1.0':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 freeze | grep flask==2.1.0',
  path    => ['/bin/', '/usr/bin/'],
}
