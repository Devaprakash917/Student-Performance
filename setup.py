from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:  #file_path is the name of the parameter.: str is a type hint that says:“This parameter should be a string (str).” and function should return string(->List[Str])
    """This function reads and returns a list of requirements from a file."""
    requirements = []
    with open(file_path) as file_pg:
        requirements = file_pg.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Deva Prakash",
    author_email="prakashdev298@gmail.com",
    packages=find_packages(),  #It will include all folders (and their subfolders) that contain an __init__.py file.our own code of proect
    #if __init__.py is missing Python won’t recognize the folder as a package.
    install_requires=get_requirements('requirements.txt')  #install dependencies like pandas ,numpy etc
)
