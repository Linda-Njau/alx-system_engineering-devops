#modifying ssh configuration to refuse password
include stdlib

file_line { 'configure SSH':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no\n     IdentityFile ~/.ssh/school',
  replace => true,
}
