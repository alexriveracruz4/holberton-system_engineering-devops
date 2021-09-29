# replace the typo extension in wp-setting file

exec { 'fix-word':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
