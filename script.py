#script.py
#by Cameron Taylor and Steven Jace Conflenti
#TLEN 5540

#most lines commented out just print too much output, can be uncommented to see results

import subprocess as sub
import matplotlib.pyplot as plt

pi_image_1_dir = '/home/cameron/Desktop/network_final/pi_image_sdb1.dd'
pi_image_2_dir = '/home/cameron/Desktop/network_final/pi_image_sdb2.dd'

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


sub.call(['echo', '\n-----IP-----\n'])
cat = sub.Popen(('cat', '/mnt/var/log/syslog'), stdout=sub.PIPE)
ip_output = sub.check_output(('grep', '-oE', '([0-9]{1,3}\.){3}[0-9]{1,3}'), stdin=cat.stdout)
ips = {}
ip_output = ip_output.splitlines()


for i in range(0, len(ip_output)):
	ip_output[i] = ip_output[i].decode('UTF-8')

for line in ip_output:
	if not line in ips:
		ips[line] = 1
	else:
		ips[line] += 1

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05+height,
                '%d' % int(height),
                ha='center', va='bottom')

lists = sorted(ips.items())
x,y = zip(*lists)

fig, ax = plt.subplots()
bar = plt.bar(range(len(y)), y, align='center')
autolabel(bar)

plt.xticks(range(len(x)), x)
fig.autofmt_xdate()
plt.ylabel('Number of occurences')
plt.xlabel('IP Address')
plt.title('IP Address occurences in /var/log/syslog')

plt.show()

ips_numbers = {'7.45.41.23':0, '169.254.180.50':7, '169.254.0.0':8, '192.168.42.12':18, '192.168.42.14':20, '192.168.42.13':19, '0.0.0.0':1, '96.126.122.39':11, '216.182.1.1':13, '96.244.96.19':14, '10.201.9.77':5, '192.168.42.1':15, '10.201.8.0':9, '10.201.8.1':10, '10.201.11.66':3, '204.11.201.12':12, '192.168.42.10':16, '192.168.42.11':17, '128.138.129.173':4, '128.138.240.17':6, '127.0.0.1':2}
ip_nums = []
for i in range(len(ips_numbers)):
	for item in ips_numbers:
		if ips_numbers[item] is i:
			ip_nums.append(item)

numbers = []
for i in range(0, len(ip_output)):
	numbers.append(ips_numbers[ip_output[i]])

fig, ax = plt.subplots()
ax.scatter(range(len(numbers)), numbers)

plt.yticks(range(len(ip_nums)), ip_nums, size='small')

plt.ylabel('IP Address')
plt.xlabel('Occurence in Series')
plt.title('IP Address occurences over time from /var/log/syslog')

plt.show()

sub.call(['echo', '\n-----DNS Servers-----\n'])
sub.call(['cat', '/mnt/etc/resolv.conf'])

sub.call(['echo', '\n-----Log Messages-----\n'])
#sub.call(['cat', '/mnt/var/log/*'])
sub.call(['ls', '-la', '/mnt/var/log'])

sub.call(['echo', '\n-----Command History-----\n'])
#sub.call(['cat', '/mnt/home/pi/.bash_history'])

sub.call(['echo', '\n-----Passwords-----\n'])
#sub.call(['sudo', 'unshadow', '/mnt/etc/passwd', '/mnt/etc/shadow', '>', 'passwords.txt'])
#sub.call(['john', 'passwords.txt'])

sub.call(['echo', '\n-----Events-----\n'])
#sub.call(['grep', 'COMMAND', '/mnt/var/log/auth.log'])

sub.call(['echo', '\n-----File Changes-----\n'])
grp = sub.Popen(('sudo', 'find', '/mnt/.', '-mtime', '-100', '-ls'), stdout=sub.PIPE)
file_output = sub.check_output(["grep 'Feb 11'"], stdin=grp.stdout, shell=True)
file_output = file_output.splitlines()
for i in range(0, len(file_output)):
	file_output[i] = file_output[i].decode('UTF-8')
	#print(file_output[i])

sub.call(['echo', '\n-----Installed Software-----\n'])
grp = sub.Popen(('grep', ' install ', '/mnt/var/log/dpkg.log'), stdout=sub.PIPE)
installed_output = sub.check_output(('grep', '2017-02-11'), stdin=grp.stdout)
installed_output = installed_output.splitlines()
for i in range(0, len(installed_output)):
	installed_output[i] = installed_output[i].decode('UTF-8')
	print(installed_output[i])

sub.call(['sudo', 'umount', pi_image_2_dir])