import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Yandexmusic',
    version=get_version('mopidy_yandexmusic/__init__.py'),
    url='',
    license='Apache License, Version 2.0',
    author='Irokez Petrovic',
    author_email='irokezpetrovic@gmail.com',
    description='Yandex Music plugin for Mopidy',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.14',
        'Pykka >= 1.1',
        'yandex_music',
    ],
    entry_points={
        'mopidy.ext': [
            'yandexmusic = mopidy_yandexmusic:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)