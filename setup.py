from setuptools import find_packages, setup
from typing import List


hiphen_minus_e = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns the list of libraries in requirements file
    '''
    requirements = []
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [ele.replace("\n","") for ele in requirements]
        if hiphen_minus_e in requirements:
            requirements.remove(hiphen_minus_e)
    return requirements
        


setup(
    name='MLProject',
    version='0.0.1',
    author='M.Thirupati Reddy',
    author_email='thirupati953@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')


)