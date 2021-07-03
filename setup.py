from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in mendybraun_changes/__init__.py
from mendybraun_changes import __version__ as version

setup(
	name='mendybraun_changes',
	version=version,
	description='ERPNext Changes for jplakerp',
	author='nomi-g',
	author_email='nomi9639@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
