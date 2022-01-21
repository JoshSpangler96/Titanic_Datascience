from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pypandoc>=1.4',
        'watermark>=2.3.0',
        'pandas>=1.3.5',
        'scikit-learn>=1.0.2',
        'scipy>=1.7.3',
        'matplotlib>=3.5.1',
        'pytest>=6.2.5',
        'pytest-runner>=5.3.1',
        'click>=7.1.2'
    ],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    entry_points='''
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis
    '''
)