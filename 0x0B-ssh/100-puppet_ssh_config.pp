# Creates a file 
file { '/home/ubuntu/.ssh/config':
  ensure  => 'present',
  content => 'Host 34.239.160.19
    HostName 4888-web-01
    User ubuntu
    ForwardAgent yes 
    IdentitiesOnly yes 
    IdentityFile ~/.ssh/school
',
}

