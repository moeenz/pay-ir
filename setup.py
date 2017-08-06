import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pay-ir',
    version='0.1.0',
    packages=find_packages(),
    test_suite='pay_ir.tests',
    include_package_data=True,
    author='Moeen Zamani',
    author_email='moeen.zamani@gmail.com',
    license='MIT',
    description='Python interface for pay.ir payment gateway.',
    url='https://github.com/moeenz/pay-ir',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python'
    ],
)
