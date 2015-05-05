# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name='combine',
    version='0.1.4',
    provides=['combine'],
    author='MLSec Project',
    url='https://github.com/mlsecproject/combine',
    setup_requires='setuptools',
    license='GPLv3',
    description='Combine gathers Threat Intelligence from publicly available sources',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.3.2',
        'feedparser==5.1.3',
        'netaddr==0.7.14',
        'pygeoip==0.3.2',
        'requests==2.7.0',
        'sortedcontainers==0.9.5',
        'unicodecsv==0.12.0',
    ],
    dependency_links=[
        "git+https://github.com/rtdean/grequests@19239a34b00b8ac226b21f01b0fb55e869097fb7#egg=grequests-0.3.1"
    ],
    entry_points={
        'console_scripts': [
            'combine=combine.combine:main',
            'reaper=combine.reaper:main',
            'thresher=combine.thresher:main',
            'winnower=combine.winnower:main',
            'baler=combine.baler:main',
        ],
    },
)
