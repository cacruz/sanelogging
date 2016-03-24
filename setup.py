from distutils.core import setup

setup(
    name='sanelogging',
    version='1.0.0',
    author='Jeffrey Paul',
    author_email='sneak@datavibe.net',
    packages=['sanelogging'],
    url='http://pypi.python.org/pypi/sanelogging/',
    license='LICENSE.txt',
    description='Python logging for humans',
    long_description=open('README.md').read(),
    install_requires=[
        "colorlog",
    ],
)
