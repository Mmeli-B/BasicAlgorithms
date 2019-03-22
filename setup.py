from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Basic Algorithms to test out github, :)',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Mmeli-B/BasicAlgorithms',
    author='<Mmeli Mavuso>',
    author_email='<mmeli.b.mavuso@gmail.com>'
)