from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
import os
env.hosts = ['192.168.91.128']
env.user = 'root'
env.password = '900118dly1020'
def deploy():
    with cd('/'):
        run('python /opt/app/lsdir.py')

if __name__ == '__main__':
    deploy()