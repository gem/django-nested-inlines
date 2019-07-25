#!/usr/bin/python
from setuptools import setup, find_packages

from nested_inlines import __version__

github_url = 'https://github.com/silverfix/django-nested-inlines'
long_desc = open('README.md').read()

setup(
    name='dj-nested-inlines',
    version='.'.join(str(v) for v in __version__),
    description='Adds nested inline support in Django admin',
    long_description=long_desc,
    url=github_url,
    author='Andrea Rabbaglietti',
    author_email='silverfix@gmail.com',
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    # packages=find_packages(exclude=['tests']),
    packages=['.', 'nested_inlines'],
    package_data={'nested_inlines' : ['README.md',
                                      'templates/admin/edit_inline/*.html',
                                      'static/admin/css/*.css',
                                      'static/admin/js/*.js']},
)

