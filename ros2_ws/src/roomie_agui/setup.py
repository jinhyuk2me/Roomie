from setuptools import setup, find_packages

package_name = 'roomie_agui'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Roomie Team',
    maintainer_email='admin@roomie.com',
    description='Admin GUI for Roomie service robot system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'agui_node = roomie_agui.agui_node:main',
        ],
    },
)
