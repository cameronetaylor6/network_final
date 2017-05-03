import subprocess as sub
import matplotlib.pyplot as plt

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
#sub.call(['md5sum', pi_image_2_dir])

sub.call(['echo', '\n-----SHA Hash Partition 2-----\n'])
#sub.call(['shasum', pi_image_2_dir])

sub.call(['echo', '\n-----Last Logins-----\n'])
sub.call(['last', '-f', '/mnt/var/log/wtmp'])

sub.call(['echo', '\n-----Last Boot-----\n'])
sub.call(['last', 'reboot', '-f', '/mnt/var/log/wtmp'])

sub.call(['echo', '\n-----OS-----\n'])
sub.call(['cat', '/mnt/etc/os-release'])

#TODO
sub.call(['echo', '\n-----IP-----\n'])
cat = sub.Popen(('cat', '/mnt/var/log/syslog'), stdout=sub.PIPE)
output = sub.check_output(('grep', '-oE', '([0-9]{1,3}\.){3}[0-9]{1,3}'), stdin=cat.stdout)
ips = {}
output = output.splitlines()
for line in output:
	if not line in ips:
		ips[line] = 1
	else:
		ips[line] += 1
print(ips)

sub.call(['echo', '\n-----DNS Servers-----\n'])
sub.call(['cat', '/mnt/etc/resolv.conf'])

sub.call(['echo', '\n-----Log Messages-----\n'])
#sub.call(['cat', '/mnt/var/log/*'])

sub.call(['echo', '\n-----Command History-----\n'])
#sub.call(['cat', '/mnt/home/pi/.bash_history'])

#TODO: write to file using subprocess
sub.call(['echo', '\n-----Passwords-----\n'])
#sub.call(['sudo', 'unshadow', '/mnt/etc/passwd', '/mnt/etc/shadow', '>', 'passwords.txt'])
#sub.call(['john', 'passwords.txt'])

#TODO: table of users + login times
#cam

#TODO: timeline of events from /mnt/var/log/*


#TODO: timeline of file changes
#cam

#TODO: visualize IP addresses - plot on pyplot over time? number of requests from each ip?
#cam

#TODO: software installed
sub.call(['echo', '\n-----Installed Software-----\n'])
grp = sub.Popen(('grep', ' install ', '/mnt/var/log/dpkg.log'), stdout=sub.PIPE)
output = sub.check_output(('grep', '2017-02-11'), stdin=grp.stdout)
print(output)

#TODO: py_game vulnerabilities





sub.call(['sudo', 'umount', pi_image_2_dir])