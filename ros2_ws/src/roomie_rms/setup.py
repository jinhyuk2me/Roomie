from setuptools import setup, find_packages
import os
import glob

package_name = 'roomie_rms'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Launch 파일들 포함
        ('share/' + package_name + '/launch', glob.glob('launch/*.py')),
        # Config 파일들 포함
        ('share/' + package_name + '/config', glob.glob('config/*.yaml')),
        # Static 파일들 포함
        ('share/' + package_name + '/static', glob.glob('roomie_rms/static/*.*')),
<<<<<<< Updated upstream
        ('share/' + package_name + '/static/images', glob.glob('roomie_rms/static/images/*.*')),
=======
>>>>>>> Stashed changes
        ('share/' + package_name + '/static/images/food', glob.glob('roomie_rms/static/images/food/*')),
        ('share/' + package_name + '/static/images/supply', glob.glob('roomie_rms/static/images/supply/*')),
        ('share/' + package_name + '/static/sql', glob.glob('roomie_rms/static/sql/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Roomie Team',
    maintainer_email='admin@roomie.com',
    description='Robot Main Server for Roomie service robot system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rms_node = roomie_rms.rms_node:main',
        ],
    },
) 