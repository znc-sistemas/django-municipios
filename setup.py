# !/usr/bin/env python

import os
import sys

import municipios

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = municipios.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


def get_requirements():
    return open('requirements.txt').read().splitlines()


setup(
    name='django-municipios',
    version=version,
    description="""Aplicação plugável Django com modelos e widgets para os Municípios Brasileiros""",
    long_description=readme + '\n\n' + history,
    author='ZNC Sistemas',
    author_email='contato@znc.com.br',
    url='https://github.com/znc-sistemas/django-municipios',
    packages=['municipios'],
    data_files=[
        ('migrations', [
            'municipios/migrations/__init__.py',
            'municipios/migrations/0001_initial.py',
        ]),
        ('templates', [
            'municipios/templates/municipios/municipio_field.html',
            'municipios/templates/municipios/municipios_options.html',
            'municipios/templates/municipios/uf_field.html',
        ]),
        ('utils', [
            'municipios/utils/__init__.py',
            'municipios/utils/ibge.py',
            'municipios/utils/settings.py',
        ]),
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='django-municipios',
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Utilities',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=get_requirements(),
)
