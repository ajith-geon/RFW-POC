import setuptools
import os
from shutil import copyfile
import shutil
import sys

#print os.path.dirname(sys.executable)

with open("README.md", "r") as fh:
    long_description = fh.read()

	
def driver_install():
	PATH = os.path.dirname(sys.executable)
	shutil.copy('geckodriver.exe', PATH)
	shutil.copy('chromedriver.exe', PATH)

driver_install()

setuptools.setup(
    name="WebDrivers",
    version="0.0.1",
    author="Ajith George",
    author_email="ajith.george@gadgeon.com",
    description="Selenium WebDrivers Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TBD",
    packages=setuptools.find_packages(),
	package_data={'*': ['*.exe']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)