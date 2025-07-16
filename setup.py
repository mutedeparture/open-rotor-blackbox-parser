from setuptools import setup, find_packages

setup(
    name='open-rotor-blackbox-parser',
    version='0.1.0',
    description='A lightweight parser for Betaflight Blackbox .bbl logs with support for flight data, GPS, and events.',
    author='Bahadir Arac',
    author_email='iletisim@bahadirarac.com',
    url='https://github.com/mutedeparture/open-rotor-blackbox-parser',
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'blackbox-parse=blackbox_parser.cli:main',
        ],
    },
    include_package_data=True,
)