# filepath: bank-reconciliation-app/setup.py

from setuptools import setup, find_packages

setup(
    name='bank-reconciliation-app',  # Name of the package
    version='0.1.0',  # Version of the package
    packages=find_packages(where='src'),  # Find all packages in the 'src' directory
    package_dir={'': 'src'},  # Specify the root directory for packages
    install_requires=[
        'pandas==1.3.0',  # Specify the version of pandas to install
        'openpyxl==3.0.7'  # Specify the version of openpyxl to install
    ],
    entry_points={
        'console_scripts': [
            'bank-reconciliation-app=main:main',  # Create a console script entry point
        ],
    },
)