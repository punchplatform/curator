import os
import re
import sys
from setuptools import setup

# Utility function to read from file.
def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    VERSIONFILE="curator/_version.py"
    verstrline = fread(VERSIONFILE).strip()
    vsre = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(vsre, verstrline, re.M)
    if mo:
        VERSION = mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
    build_number = os.environ.get('CURATOR_BUILD_NUMBER', None)
    if build_number:
        return VERSION + "b{}".format(build_number)
    return VERSION

def get_install_requires():
    res = ['elasticsearch>=7.0.0,<8.0.0' ]
    res.append('requests>=2.20.0')
    res.append('boto3>=1.9.142')
    res.append('requests_aws4auth>=0.9')
    res.append('click>=6.7,<7.0')
    res.append('pyyaml==3.12')
    res.append('voluptuous>=0.9.3')
    res.append('certifi>=2019.3.9')
    res.append('six>=1.11.0')
    res.append('urllib3<1.26')
    return res

setup(
    name = "elasticsearch-curator",
    version = get_version(),
    author = "Elastic",
    author_email = "info@elastic.co",
    description = "Tending your Elasticsearch indices",
    long_description=fread('README.rst'),
    url = "http://github.com/elastic/curator",
    download_url = "https://github.com/elastic/curator/tarball/v" + get_version(),
    license = "Apache License, Version 2.0",
    install_requires = get_install_requires(),
    keywords = "elasticsearch time-series indexed index-expiry",
    packages = ["curator"],
    include_package_data=True,
    entry_points = {
        "console_scripts" : [
            "curator = curator.cli:cli",
            "curator_cli = curator.curator_cli:main",
            "es_repo_mgr = curator.repomgrcli:repo_mgr_cli",
        ]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite = "test.run_tests.run_all",
    tests_require = ["mock", "nose", "coverage", "nosexcover"]
)
