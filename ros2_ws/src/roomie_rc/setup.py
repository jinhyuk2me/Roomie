from setuptools import setup

package_name = 'roomie_rc'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/roomie_rc']),
        ('share/' + package_name, ['package.xml']),
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
        ],
    },
)
