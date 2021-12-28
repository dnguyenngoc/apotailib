from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.9'
]
 
setup(
  name='apotailib',
  version='0.0.2',
  description='A very basic calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Duy Nguyen',
  author_email='duynguyenngoc@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='ai', 
  packages=find_packages(),
  install_requires=[''] 
)