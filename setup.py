from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='blockmanlauncher.py',
    version='1.0.0',
    author='Spargat Team',
    author_email='blockmanlauncher@gmail.com',
    description='Blockman Launcher API for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ComicalSGT/blockmanlauncher.py',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests"
    ],
    include_package_data=True
)