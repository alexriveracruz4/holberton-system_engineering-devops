#login with the holberton user and open a file without any error message.

exec { 'hardfile_limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
exec { 'softfile_limit':
  command => 'sed -i "/holberton hard/s/5/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
