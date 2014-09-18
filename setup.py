
from setuptools import setup

setup(
    name='Email Collector',
    version='0.1',
    long_description=__doc__,
    packages=['emailcollector'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Flask-WTF'],
)
