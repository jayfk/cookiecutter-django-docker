cookiecutter-django-docker
==========================

A cookiecutter_ template for Django. Based on the popular cookiecutter-django_ with enhanced docker support.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-django: https://github.com/pydanny/cookiecutter-django

Status
------
The current status is experimental.

Differences
-----------

* Uses uWSGi instead of gunicorn
* Redis cache instead of memcached
* A merged requirements.txt

Features
---------

* For Django 1.8
* Twitter Bootstrap_ 3
* AngularJS_
* 12-Factor_ based settings via django-environ_
* Optimized development and production settings
* Registration via django-allauth_
* Grunt build for compass and livereload
* Basic e-mail configurations for send emails via Mailgun_
* Pre configured Celery_ (optional)
* Pre configured Newrelic_ support (optional)
* Pre configured Sentry_ support (optional)

.. _Bootstrap: https://github.com/twbs/bootstrap
.. _AngularJS: https://github.com/angular/angular.js
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _django-avatar: https://github.com/jezdez/django-avatar/
.. _Mailgun: https://mailgun.com/
.. _Celery: http://www.celeryproject.org/
.. _Sentry:
.. _Newrelic:


Constraints
-----------

* Only maintained 3rd party libraries are used.
* PostgreSQL everywhere (9.0+)
* Environment variables for configuration.

Docker Support
--------------

This project comes with docker support.


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/jayfk/cookiecutter-django-docker.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name (default is "project_name")? Reddit Clone
    repo_name (default is "Reddit_Clone")? reddit
    author_name (default is "Your Name")? Daniel Greenfeld
    email (default is "Your email")? pydanny@gmail.com
    description (default is "A short description of the project.")? A reddit clone.
    domain_name (default is "example.com")? myreddit.com
    version (default is "0.1.0")? 0.0.1
    timezone (default is "UTC")?
    now (default is "2015/01/13")? 2015/01/16
    year (default is "2015")?
    use_whitenoise (default is "y")?


Enter the project and take a look around::

    $ cd redditclone/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:pydanny/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* docker
* docker-compose

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f dev.yml up

You can also set the environment variable ``COMPOSE_FILE`` pointing to ``dev.yml`` like this::

    $ export COMPOSE_FILE=dev.yml

And then run::

    $ docker-compose up


To migrate your app and to create a superuser, run::

    $ docker-compose run django python manage.py migrate

    $ docker-compose run django python manage.py createsuperuser



**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading and Sass / Compass CSS compilation you can do so with the included Grunt task.

Make sure that nodejs_ is installed. Then in the project root run::

    $ npm install

.. _nodejs: http://nodejs.org/download/

Now you just need::

    $ grunt serve

The base app will now run as it would with the usual ``manage.py runserver`` but with live reloading and Sass compilation enabled.

To get live reloading to work you'll probably need to install an `appropriate browser extension`_

.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-

It's time to write the code!!!

Deployment
----------



For Readers of Two Scoops of Django 1.8
--------------------------------------------

You may notice that some elements of this project do not exactly match what we describe in chapter 3. The reason for that is this project, amongst other things, serves as a test bed for trying out new ideas and concepts. Sometimes they work, sometimes they don't, but the end result is that it won't necessarily match precisely what is described in the book I co-authored.

"Your Stuff"
-------------

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.

Releases
--------

Want a stable release? You can find them at https://github.com/pydanny/cookiecutter-django/releases


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutters/

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own project development
experience better.
