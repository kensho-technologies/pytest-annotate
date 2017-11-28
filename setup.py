# Copyright 2017 Kensho Technologies, Inc.
from setuptools import find_packages, setup

package_name = 'pytest-annotate'
version = '1.0.2'

setup(
    name=package_name,
    version=version,
    description='pytest-annotate: Generate PyAnnotate annotations from your pytest tests.',
    url='https://github.com/kensho-technologies/pytest-annotate',
    author='Kensho Technologies, Inc.',
    author_email='pytest-annotate-maintainer@kensho.com',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'pyannotate>=1.0.0,<2.0.0',
        'pytest>=3.2.0,<4.0.0'
    ],
    entry_points={
        'pytest11': [
            'pytest_annotate = pytest_annotate.plugin',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ],
    keywords='pytest py.test types annotations pyannotate',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.5.0,!=3.5.1',
)
