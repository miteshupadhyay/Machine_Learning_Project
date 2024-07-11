# This setup file is responsible to create our machine learning application as package.
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
        This Function will return list of requiremtns
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
setup (
    name ='Machine Learning Project',
    version = '0.0.1',
    author = 'Mitesh Upadhyay',
    author_email='upadhyaymitesh91@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)