import subprocess as sub

pi_image_1_dir = '/home/cameron/Desktop/network_final/pi_image_sdb1.dd'
pi_image_2_dir = '/home/cameron/Desktop/network_final/pi_image_sdb2.dd'

#shell=True
sub.call(['sudo', 'mount', '-oro,loop', pi_image_2_dir, '/mnt'])
sub.call(['echo', '\nResults'])

sub.call(['echo', '\n-----MD5 Hash Partition 1-----\n'])
sub.call(['md5sum', pi_image_1_dir])

sub.call(['echo', '\n-----SHA Hash Partition 1-----\n'])
sub.call(['shasum', pi_image_1_dir])

sub.call(['echo', '\n-----MD5 Hash Partition 2-----\n'])
sub.call(['md5sum', pi_image_2_dir])

sub.call(['echo', '\n-----SHA Hash Partition 2-----\n'])
sub.call(['shasum', pi_image_2_dir])

sub.call(['echo', '\n-----Last Logins-----\n'])
sub.call(['last', '-f', '/mnt/var/log/wtmp'])

sub.call(['echo', '\n-----Last Boot-----\n'])
sub.call(['last', 'reboot', '-f', '/mnt/var/log/wtmp'])

sub.call(['echo', '\n-----OS-----\n'])
sub.call(['cat', '/mnt/etc/os-release'])

#TODO
sub.call(['echo', '\n-----IP-----\n'])
#cat /mnt/var/log/syslog | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"
#sub.call(['cat', '/mnt/var/log/syslog', '|', 'grep', '-Ei', 'dhcp'], shell=True)

sub.call(['echo', '\n-----DNS Servers-----\n'])
sub.call(['cat', '/mnt/etc/resolv.conf'])

sub.call(['echo', '\n-----Log Messages-----\n'])
#sub.call(['cat', '/mnt/var/log/*'])

sub.call(['echo', '\n-----Command History-----\n'])
#sub.call(['cat', '/mnt/home/pi/.bash_history'])

#TODO: write to file using subprocess
sub.call(['echo', '\n-----Passwords-----\n'])
#sub.call(['sudo', 'unshadow', '/mnt/etc/passwd', '/mnt/etc/shadow', '>', 'passwords.txt'])
sub.call(['john', 'passwords.txt'])

#TODO: table of users + login times

#TODO: timeline of events from /mnt/var/log/*

#TODO: timeline of file changes

#TODO: visualize IP addresses - plot on pyplot over time? number of requests from each ip?

#TODO: software installed

#TODO: py_game vulnerabilities





sub.call(['sudo', 'umount', pi_image_2_dir])