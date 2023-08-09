from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    """
    This is used to return the list of requirments from requirements.txt file 
    """
    
    trigger = "-e ."

    with open(filepath) as libraray:
        required = libraray.readlines()
        requirements = [req.replace("\n", "") for req in required]
        #list(map(lambda i:i.replace("\n", ""), required))

        if trigger in requirements:
            requirements.remove(trigger)


setup(

    name="ML_End_To_End",
    version="0.0.1",
    author="Nitin",
    author_email="nithin.nagireddy@gmail.com",
    packages=find_packages()
    install_requires= get_requirements("requirements.txt") 
)