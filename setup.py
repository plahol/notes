try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools
    
config = {
    "description": "Notes",
    "author": "Place Holder",
    "url": "www.placeholder.com",
    "download_url": "www.placeholder.com",
    "author_email": "placeholder@placeholder.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["Name"],
    "scripts": []
    "name": "projectname"
}

setup(**config)    

    
