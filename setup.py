#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import mayan

PACKAGE_NAME = 'mayan'
PACKAGE_DIR = 'mayan'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


def find_packages(directory):
    # Compile the list of packages available, because distutils doesn't have
    # an easy way to do this.
    packages, data_files = [], []
    root_dir = os.path.dirname(__file__)
    if root_dir != '':
        os.chdir(root_dir)

    for dirpath, dirnames, filenames in os.walk(directory):
        # Ignore dirnames that start with '.'
        if os.path.basename(dirpath).startswith('.'):
            continue
        if '__init__.py' in filenames:
            packages.append('.'.join(fullsplit(dirpath)))
        elif filenames:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])
    return packages

install_requires = [
'APScheduler==2.0.3',
'cssmin==0.1.4',
'Django==1.6.5',
'django-filetransfers==0.1.0',
'django-pagination==1.0.7',
'django-compressor==1.4',
'django-taggit==0.12',
'django-mptt==0.6.0',
'django-sendfile==0.3.4',
'djangorestframework==2.3.13',
'GitPython==0.3.2.RC1',
'ghostscript==0.4.1',
'Pillow==2.4.0',
'PyYAML==3.10',
'pbs==0.105',
'pdfminer==20110227',
'psutil==0.5.1',
'python-gnupg==0.3.6',
'python-hkp==0.1.3',
'python-magic==0.4.6',
'pytz==2014.4',
'requests==0.14.1',
'South==0.8.4',
'sh==1.09',
'slate==0.3',
'unicode-slugify==0.1',
'wsgiref==0.1.2',
]

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    author='Roberto Rosario',
    author_email='roberto.rosario@mayan-edms.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Communications :: File Sharing',
    ],
    description='A Django based Document Management System.',
    include_package_data=True,
    install_requires=install_requires,
    license=license,
    long_description=readme + '\n\n' + history,
    name=PACKAGE_NAME,
    packages=find_packages(PACKAGE_DIR),
    platforms=['any'],
    scripts=['mayan/bin/mayan-edms.py'],
    url='https://github.com/mayan-edms/mayan-edms',
    version=mayan.__version__,
    zip_safe=False,
)
