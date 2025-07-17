from setuptools import find_packages , setup
from typing import List


def get_requirements()->list[str] :
    requirments_list = []
    return requirments_list

setup(
    name = 'sensor',
    version="0.0.1",
    author="Kartik",
    author_email="kartikvijay9680@gmail.com",
    packages=find_packages() ,
    install_requires = get_requirements() #["pymongo"]
)

