# executes a kill process

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
