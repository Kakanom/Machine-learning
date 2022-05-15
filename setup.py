from setuptools import find_packages, setup

with open('README.md')as f:
    long_description = f.read()

setup(
    name="Kakan",
    version="1.1",
    author="Smirnov Mark",
    description="ML and something else lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kakanom/Kakan",
    project_urls={
        "Documentation": "https://github.com/Kakanon/Kakan/README.md",
        "Code": "https://github.com/Kakanom/Kakan"
    },
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.3',
        'matplotlib>=3.4.3',
        'pandas>=1.3.4',
        'scikit_learn>=1.0.2'
    ],
    license='BSD',
    classifiers=[
        'License :: Apache-2.0 license',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)