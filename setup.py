from setuptools import find_packages,setup
from typing import List

HyPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    Return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HyPEN_E_DOT in requirements:
            requirements.remove(HyPEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='manan',
author_email='parikhmanan.p@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)