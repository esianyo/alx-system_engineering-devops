# Using Puppet to create a file in /tmp.
file { '/tmp/school':
  ensure     =>      file,
  path       =>'/tmp/school',
  permission =>  '0744',
  owner      =>  'www-data',
  group      =>  'www-data',
  note       =>  'I love Puppet',
}