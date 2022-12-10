from setuptools import setup

setup(
    name='md2wp',
    version='0.0.1',
    install_requires=[
        'beautifulsoup4',
        'markdown2',
        'requests',
        'tabulate'
    ],
    entry_points = {
        'console_scripts': ['md2wp=md2wp.__main__:main'],
    }
)
