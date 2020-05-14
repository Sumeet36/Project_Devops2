import os
os.system("touch /etc/yum.repos.d/docker.repo")
file = open("/etc/yum.repos.d/docker.repo","w")
file.write(""" 
[docker]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
""")
file.close()
os.system("yum update -y")
os.system("yum install docker-ce --nobest -y")