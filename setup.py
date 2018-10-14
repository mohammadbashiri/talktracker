from setuptools import setup, find_packages

with open("README.md", "r") as fh:
      long_description = fh.read()

setup(
      name='talktracker',
      version='0.12',
      author='Mohammad Bashiri',
      author_email='mohammadbashiri93@gmail.com',
      description='Records information about the performance of participants in a group discussion',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/mohammadbashiri/talktracker',
      license='MIT',
      packages=find_packages(),

      # required packages
      install_requires=['numpy', 'matplotlib', 'click'],
      tests_require = ['pytest'],
      )
