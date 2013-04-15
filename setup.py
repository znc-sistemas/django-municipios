# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-municipios',
    version='0.8.0',
    description='Aplicação plugável Django com modelos e widgets para os Municípios Brasileiros',
    long_description=open('README.rst').read(),
    author='ZNC Sistemas',
    author_email='contato@znc.com.br',
    maintainer='ZNC Sistemas',
    maintainer_email='contato@znc.com.br',
    url='https://github.com/znc-sistemas/django-municipios',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
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
        'Natural Language :: Portuguese (Brazilian)'
    ],
)
