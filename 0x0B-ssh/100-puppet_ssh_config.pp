#!/usr/bin/env bash
# Escaping passwd request using Puppet

#!/usr/bin/env bash
# using Puppet to make changes to our configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    #SSH client configuration
    host
        HostName 54.197.45.145
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
   "
}
