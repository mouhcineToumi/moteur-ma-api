
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pymoteurma',
    version='1.0.0',
    packages=find_packages(),
    url='',
    license='MIT',
    author='mouhcine',
    author_email='mouhcine.toumi98@gmail.com',
    description='An unofficial API for scrapping Moteur.ma',
    install_requires=required
)