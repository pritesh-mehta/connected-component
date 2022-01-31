"""
@author: pritesh-mehta
"""

from setuptools import setup, find_packages

setup(name='connected_component',
      version='1.0',
      description='Connected component utilities',
      url='https://github.com/pritesh-mehta/connected_component',
      python_requires='>=3.6',
      author='Pritesh Mehta',
      author_email='pritesh.mehta@kcl.ac.uk',
      license='Apache 2.0',
      zip_safe=False,
      install_requires=[
      'numpy',
      'scipy',
      'pathlib',
      'argparse',
      'nibabel',
      ],
      entry_points={
        'console_scripts': [
            'connected_component=connected_component.connected_component:process',
            ],
      },
      packages=find_packages(include=['connected_component']),
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
      ]
      )