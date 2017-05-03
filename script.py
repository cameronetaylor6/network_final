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
ip_output = sub.check_output(('grep', '-oE', '([0-9]{1,3}\.){3}[0-9]{1,3}'), stdin=cat.stdout)
ips = {}
ip_output = ip_output.splitlines()

'''
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
#ax.bar(range(len(ips)), ips.values(), align='center')
plt.xticks(range(len(x)), x)
fig.autofmt_xdate()

plt.show()

d = {ni: indi for indi, ni in enumerate(set(ip_output))}
numbers = [d[ni] for ni in ip_output]
print(d)

fig, ax = plt.subplots()
ax.scatter(range(len(ip_output)), numbers)
plt.yticks(range(len(d)), ip_output)

plt.show()
'''
sub.call(['echo', '\n-----DNS Servers-----\n'])
sub.call(['cat', '/mnt/etc/resolv.conf'])

sub.call(['echo', '\n-----Log Messages-----\n'])
#sub.call(['cat', '/mnt/var/log/*'])
sub.call(['ls', '-la', '/mnt/var/log'])

sub.call(['echo', '\n-----Command History-----\n'])
#sub.call(['cat', '/mnt/home/pi/.bash_history'])

#TODO: write to file using subprocess
sub.call(['echo', '\n-----Passwords-----\n'])
#sub.call(['sudo', 'unshadow', '/mnt/etc/passwd', '/mnt/etc/shadow', '>', 'passwords.txt'])
#sub.call(['john', 'passwords.txt'])

#TODO: table of users + login times
#cam

#TODO: timeline of events from /mnt/var/log/*
sub.call(['echo', '\n-----Events-----\n'])
sub.call(['grep', 'COMMAND', '/mnt/var/log/auth.log'])

#TODO: timeline of file changes
#cam
sub.call(['echo', '\n-----File Changes-----\n'])
grp = sub.Popen(('sudo', 'find', '/mnt/*', '-mtime', '-100', '-ls'), stdout=sub.PIPE)
output = sub.check_output(('grep', 'Feb 11'), stdin=grp.stdout)
print(output)

#TODO: visualize IP addresses - plot on pyplot over time? number of requests from each ip?
#cam

#TODO: software installed
sub.call(['echo', '\n-----Installed Software-----\n'])
grp = sub.Popen(('grep', ' install ', '/mnt/var/log/dpkg.log'), stdout=sub.PIPE)
output = sub.check_output(('grep', '2017-02-11'), stdin=grp.stdout)
print(output)

#TODO: py_game vulnerabilities





sub.call(['sudo', 'umount', pi_image_2_dir])