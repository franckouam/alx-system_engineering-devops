# Puppet script to automatically fix the eror
exec {'fix-phpp':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => '/bin';
}

