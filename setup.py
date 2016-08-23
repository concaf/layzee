from setuptools import setup, find_packages

setup(name='layzee',
      version='0.1',
      description=
      'Specify Vagrantfile options on the command line and run the VM',
      author='Shubham | containscafeine',
      author_email='shubham@linux.com',
      url='https://github.com/containscafeine/layzee',
      packages=find_packages(), requires=['jinja2'],
      entry_points={
          'console_scripts': [
              'layzee = cli:main'
          ]
      }
      )
