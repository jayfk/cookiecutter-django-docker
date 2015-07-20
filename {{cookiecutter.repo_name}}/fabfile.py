# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from fabric.api import *
from fabric.contrib.files import append
from fabric.contrib.console import confirm

env.git_url = ""
env.projectname = "{{cookiecutter.repo_name}}"


def production():

    env.hosts = [""]
    env.port = 22
    env.user = "root"


def initial_setup():

    sudo("mkdir -p /code/%s" % env.projectname)

    with cd("/code/" + env.projectname):
        sudo("git clone %s ." % env.git_url)
        sudo("docker-compose build")

    # installing supervisor
    sudo("apt-get install -y supervisor")

    # add this projects supervisord.conf
    sudo("ln -sfn /code/{0}/supervisord.conf /etc/supervisor/conf.d/{0}.conf".format(env.projectname))

    # restart supervisord gracefully
    sudo("supervisorctl reread")
    sudo("supervisorctl update")
    sudo("supervisorctl start " + env.projectname)

    if confirm("Run database migration?", default=True):
        sudo("docker-compose run django python manage.py migrate")

    if confirm("Create super user?", default=False):
        sudo("docker-compose run django python manage.py createsuperuser")


def commit_and_push():
    message = prompt("Commit message:")
    local("git commit -a -m '{0}'".format(message))
    local("git push origin master")


def deploy():

    #
    # commit_and_push()

    with cd("/code/" + env.projectname):
        sudo("git pull origin master")
        sudo("docker-compose build")
        sudo("docker-compose up")

    if confirm("Run database migration?", default=False):
        with cd("/code/%s" % env.projectname):
            sudo("docker-compose run django python manage.py migrate")