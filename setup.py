from setuptools import setup, find_packages

VERSION = '0.0.1'

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

setup(
    name='conform',
    author='b1nzy',
    url='https://github.com/b1naryth1ef/conform',
    version=VERSION,
    packages=find_packages(),
    license='MIT',
    description='a data modeling and validation library',
    long_description=readme,
    include_package_data=True,
    install_requires=requirements,
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ])
