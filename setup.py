from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Return a clean list of requirements from a requirements file.
    Skips blank lines, comments, and '-e .'.
    """
    requirements: List[str] = []
    with open(file_path, "r", encoding="utf-8") as file_obj:
        for line in file_obj:
            req = line.strip()
            if not req or req.startswith("#"):
                continue
            if req == HYPHEN_E_DOT:
                continue
            requirements.append(req)
    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Mani",
    author_email="manisadvinibolla@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
