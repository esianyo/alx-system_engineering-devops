# Define the file to be modified
$file_path = '/var/www/html/wp-settings.php'

# Create an exec resource to replace "phpp" with "php" in the specified file
exec { 'modify_file':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin', '/usr/bin'],
}
