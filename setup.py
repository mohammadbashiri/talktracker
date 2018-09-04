from setuptools import setup, find_packages

setup(name='talktracker',
      version='0.1',
      description='Records information about the performance of participants in a group discussion',
      url='https://github.com/mohammadbashiri/talktracker',
      author='Mohammad Bashiri',
      author_email='mohammadbashiri93@gmail.com',
      license='MIT',
      packages=find_packages(),
      
      # required packages
      install_requires=['numpy', 'matplotlib', 'click'],
      )