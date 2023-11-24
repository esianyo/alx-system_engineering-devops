# Kills processes
exec { 'pkill killmenow':
    command => 'pkill killmenow',
}