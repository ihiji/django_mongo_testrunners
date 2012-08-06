#!/usr/bin/env python
from distutils.core import setup

setup(
      name='django_mongo_testrunners',
      version='0.0.2',
      author='Stuart Rench',
      author_email='info@ihiji.com',
      maintainer = 'Stuart Rench',
      maintainer_email = 'info@ihiji.com',
      url = 'https://github.com/ihiji/django_mongo_testrunners',
      download_url = 'https://github.com/ihiji/django_mongo_testrunners/tarball/master' ,

      description = 'Django Mongoengine Test Runner',
      long_description = "This allows you to dump a db to and from file"
                         "for running django tests.  A decent replacement"
                         "for fixtures.  One for django_jenkins and one"
                         "standard",

      license = 'Apache License 2.0',
      packages=[ 'mongotestrunner'],

      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
      ],
)
