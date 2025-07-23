from setuptools import setup, find_packages
import os
import glob

package_name = 'roomie_rgui'

# UI 파일들을 재귀적으로 찾기
def find_ui_files():
    ui_files = []
    for root, dirs, files in os.walk('ui'):
        for file in files:
            if file.endswith('.ui'):
                rel_path = os.path.relpath(os.path.join(root, file))
                ui_files.append(rel_path)
    return ui_files

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # UI 파일들 포함
        ('share/' + package_name + '/ui/common', glob.glob('ui/common/*.ui')),
        ('share/' + package_name + '/ui/delivery', glob.glob('ui/delivery/*.ui')),
        ('share/' + package_name + '/ui/countdown', glob.glob('ui/countdown/*.ui')),
        ('share/' + package_name + '/ui/call', glob.glob('ui/call/*.ui')),
        ('share/' + package_name + '/ui/guide', glob.glob('ui/guide/*.ui')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Roomie Team',
    maintainer_email='admin@roomie.com',
    description='Robot GUI for Roomie service robot system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rgui_node = roomie_rgui.rgui_node:main',
        ],
    },
) 