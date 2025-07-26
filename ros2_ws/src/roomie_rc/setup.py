from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'roomie_rc'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/scripts', glob('scripts/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Roomie Team',
    maintainer_email='admin@roomie.com',
    description='Robot Controller for Roomie service robot system',
    license='MIT',
    entry_points={
        'console_scripts': [
            'rc_node = roomie_rc.rc_node:main',
            'test_gui_node = roomie_rc.test_gui_node:main',
        ],
    },
)
