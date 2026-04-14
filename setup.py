from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'artems_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Artem & Artem',
    maintainer_email='artem20132001@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'first_node = artems_study_pkg.scripts.first_node:main',
            'even_publisher = artems_study_pkg.even_num_publisher:main',
            'even_overflow_listener = artems_study_pkg.even_num_overflow_listener:main',
        ],
    },
)