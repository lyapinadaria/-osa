from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='Cosa',
   version='1.0',
   description='A useful module',
   author='Daria Lyapina',
   author_email='Daria Lyapina@mail.ru',
   packages=find_packages(),  #same as name
   install_requires=[],
   entry_points ={
       'console_scripts': [ 
           'WhiteDwarf = Cosa.__main__:main', ]
       },
)
