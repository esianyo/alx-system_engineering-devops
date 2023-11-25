#!/usr/bin/env bash
# Escaping passwd request using Puppet

node 'ubuntu' {
  file_line { 'Turn off passwd auth':
    ensure => absent,
    path => '/etc/ssh/ssh_config',
    match => '.*PasswordAuthentication .*',
  }

  file_line { 'Declare identity file':
    ensure => present,
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
  }
}
