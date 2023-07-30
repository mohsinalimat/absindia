from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in absindia/__init__.py
from absindia import __version__ as version

setup(
	name="absindia",
	version=version,
	description="absindia frappe app",
	author="Baaridun Nasr, Meghashyam M",
	author_email="baaridun@absindia.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
