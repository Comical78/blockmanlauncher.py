from setuptools import setup, find_packages

setup(
    name='blockmanlauncher.py',                     
    version='1.0.0',                      
    author='Spargat Team',                   
    author_email='blockmanlauncher@gmail.com', 
    description='Blockman Launcher API on Python',  
    long_description=open('README.md').read(), 
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
        'requests>=2.25.1',                      
    ],
)
