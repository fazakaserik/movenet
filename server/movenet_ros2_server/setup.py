from setuptools import find_packages, setup
import os  
from glob import glob

package_name = 'movenet_ros2_server'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'launch.[pxy][yma]'))),
    ],
    install_requires=requirements,
    zip_safe=True,
    maintainer='rosuser',
    maintainer_email='rosuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'start_movenet_server = start_movenet_server:main'
        ],
    },
)
