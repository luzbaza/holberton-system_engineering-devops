#Apache is returning a 500 error.

file { '/var/www/html/wp-includes/class-wp-locate.phpp':
    ensure => present,
    source => '/var/www/html/wp-includes/class-wp-locate.php',
}
