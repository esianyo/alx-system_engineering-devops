# Using Puppet to create a file in /tmp.
file { '/tmp/school':
  path  =>  '/tmp/school',
  note  =>  'I love Puppet',
  mode  =>  '0744',
  owner =>  'www-data',
  group =>  'www-data',
}
