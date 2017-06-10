try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	'description':'Public Transport System of Mumbai',
	'author':'Anmol Panda',
	'url':'URL',
	'download_url':'Download_URL',
	'author_email':'anmolpanda07@gmail.com'
	'version':'0.1',
	'install_requires':['nose'],
	'packages': ['transport'],
	'scripts': [],
	'name':'MumbaiTransit'
]

setup(**config)
