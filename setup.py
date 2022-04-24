
from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='moteurmapy',
    version='1.0.0',
    packages=find_packages(),
    url='',
    license='MIT',
    author='mouhcine',
    author_email='',
    description='An unofficial API for scrapping Moteur.ma',
    long_description=long_description,
    long_description_content_type='text/markdown'
)