# Installs puppet-lint package
package { 'flask':
  ensure =>  '2.1.0',
  name   =>  'flask',
}

package { 'werkzeug':
  ensure =>  '2.1.1',
  name   =>  'werkzeug'
}