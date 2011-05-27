from setuptools import setup, find_packages
 
setup(
    name='Django-Municipios',
    version=VERSION,
    description='Aplicação plugável Django com modelos e widgets para os Municípios Brasileiros',
    long_description=open('README.rst').read(),
    author='ZNC Sistemas',
    author_email='contato@znc.com.br',
    maintainer='ZNC Sistemas',
    maintainer_email='contato@znc.com.br',
    url='https://github.com/znc-sistemas/django-municipios',
    packages=find_packages(),
    package_data=package_data,
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Development Status :: 3 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "Intended Audience :: System Administrators",
        "Topic :: Software Development"
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: JavaScript',
    ],
)