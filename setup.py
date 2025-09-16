from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylib_essentials',
    version='0.2.2', # Bumped version for the fix
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # This line ensures mappings.json is included in the pylib_essentials package.
        'pylib_essentials': ['mappings.json'],
    },
    author='SaphicDeveloper',
    author_email='saphic.developer@example.com',
    description='A compiler and utility library for creating Pymods for Minecraft Forge.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SaphicDeveloper/pylib',
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Games/Entertainment'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pymod-compiler=pylib_essentials.compiler:main',
        ],
    },
)

