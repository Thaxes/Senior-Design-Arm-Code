from setuptools import setup

package_name = 'py_pubsub2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub2.publisher_member_function2:main',
            'listener = py_pubsub2.subscriber_member_function2:main',
            'wheeltalk = py_pubsub2.pub_member_function:main',       
        ],
    },
)
