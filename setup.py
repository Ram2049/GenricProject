from setuptools import setup,find_packages
from typing import List

def get_requiremnts(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    
    '''
    hypen_e_dot = '-e .'
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if hypen_e_dot in requirements:
           requirements.remove(hypen_e_dot)
    
    return requirements

setup(
    name='GenricMLProject',
    version='0.0.2',
    author='Ram',
    author_email='ramsparttakas23@gmail.com',
    packages=find_packages(),
    install_requires = get_requiremnts('requirement.txt')
)