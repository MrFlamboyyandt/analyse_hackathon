from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Hackathon',
    long_description=open('README.md').read(),
    url='https://github.com/<username>/<package-name>',
    author='Jan du Toit',
    author_email='jandutoitt@gmail.com'
)