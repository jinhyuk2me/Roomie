from setuptools import setup

setup(
    name='roomie_vs',
    version='1.0.0',
    packages=['roomie_vs'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/roomie_vs']),
        ('share/roomie_vs', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'vs_node = roomie_vs.vs_node:main',
        ],
    },
) 