from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:    # returns a list
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()        # .readlines() add "\n" at end of each line in the text file
        requirements = [req.replace("\n", "") for req in requirements]  # to replace the "\n" by blank spaces

        if "-e ." in requirements:    # ".e -" in requirements.txt connects to setup.py which builds the whole package while requirements.txt is being installed by pip
            requirements.remove('-e .')


setup(
    name='Student Performance Prediction End-to-End',
    version='0.0.1',
    author='Saurabh Chatterjee',
    author_email='chatterjeesaurabh38@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)

