from setuptools import setup, find_packages

setup(
    name='mara-app',
    version='1.7.0',

    description="Framework for distributing flask apps across separate packages with minimal dependencies",

    python_requires='>=3.6',

    install_requires=[
        'mara-page>=1.2.3',
        'mara-db>=3.0.0',
        'flask>=0.12'
    ],

    dependency_links=[
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={
    }
)
