from setuptools import setup, find_packages

setup(
    name='awesome-args',
    version=open("version.txt").read(),
    packages=find_packages(),
    url='https://github.com/GabrielMusat/awesome-args',
    python_requires=">=3.5.*",
    license='MIT',
    author='Gabriel Musat',
    install_requires=[req for req in open("requirements.txt").read().split("\n") if len(req) > 0],
    author_email='gabimtme@gmail.com',
    description='Awesome configuration parser for Python programs which can parse from command line, environment '
                'variables and .yml files',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        "Typing :: Typed"
    ]
)
