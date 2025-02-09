from setuptools import setup, find_packages

setup(
    name='bank-reconciliation-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A bank reconciliation application to compare bank statements and identify discrepancies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/bank-reconciliation-app',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'pytest>=6.2.0',
        'commitizen>=2.17.6',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)