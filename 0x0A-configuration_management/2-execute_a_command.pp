# Kills processes
exec { 'pkill killmenow':
    command  => 'pkill killmenow',
    provider =>  'shell',
    returns  =>  [0, 1],
}