#Apache is returning a 500 error.
# Fix wp-setting file extension error

exec { 'killmenow':
    command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
    path    => '/bin',
}
