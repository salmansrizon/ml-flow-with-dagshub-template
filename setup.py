from setuptools import find_packages,setup
from typing import List
setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Salman Sakib',
    author_email='salmansrizon2016@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)