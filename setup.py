from setuptools import setup, find_packages
from typing import List

Hyphen_E_Dot = '-e .'

def get_requirements(filename:str)->List[str]:

    """
    this function is used to read the requirements.txt file and return the list of requirements
    """

    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [x.replace('\n', '') for x in requirements]

        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)

        return requirements


setup(
    name='MLProject',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Hanzla Khan',
    author_email='khanzalah548@gmail.com'
)
