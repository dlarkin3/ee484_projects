from setuptools import setup
import os
from glob import glob

package_name = 'ee484_projects'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dominic Larkin',
    maintainer_email='dominic.larkin@example.com',
    description='A Package that makes the OpenManipulator arm stand staight up',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_straight_up = ee484_projects.arm_straight_up_controller:main',
            # Add other entry points here as needed
        ],
    },
)