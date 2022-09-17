# Installs flask
package { 'flask':
  ensure   => 'installed',
  provider => 'pip3',
}
