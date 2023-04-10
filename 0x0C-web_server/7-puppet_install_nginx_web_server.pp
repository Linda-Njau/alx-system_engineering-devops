#configures anginx server on port 80
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => '
server {
  listen 80;
  root /var/www/html;
  index index.html;
  location /redirect_me {
    return 301 $scheme://$host/new/location;
  }
}',
    require => Package['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx

