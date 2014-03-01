import sys

from setuptools import setup
from setuptools import find_packages

requirements = ['PyZenity']

setup(name='worklogger',
      version='0.0.2',
      description='Small helper app, to keep track of your worklog',
      long_description='',
      keywords='work worklog markdown',
      url='https://github.com/bascht/worklogger',
      author='Sebastian Schulze',
      author_email='github.com@bascht.com',
      license='GPL',
      packages=find_packages(),
      install_requires=[
          'PyZenity==0.1.4',
      ],
      entry_points={
          'console_scripts': ['worklogger = worklogger:main'],
      })
