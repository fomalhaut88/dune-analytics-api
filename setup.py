from setuptools import setup

with open('dune_analytics_api/version.py') as f:
    __version__ = f.read().split("=", 1)[1].strip()


setup(
    name='dune_analytics_api',
    version=__version__,
    description="API to interact with https://duneanalytics.com/ to make SQL queries.",
    author='Alexander Khlebushchev',
    packages=[
        'dune_analytics_api',
    ],
    zip_safe=False,
    install_requires=[
        'requests==2.25.1',
        'prettytable==2.0.0',
    ],
    entry_points={
        'console_scripts': ['dune-analytics-api=dune_analytics_api:main'],
    },
)
