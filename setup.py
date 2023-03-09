import codecs
from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="sharedousocks",
    version="2.9.2",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="Fast tunnel proxy that helps you access neighboring C-network in a local area network.",
    author='none',
    author_email='none@gmail.com',
    url='https://github.com/sharedousocks/sharedousocks',
    packages=['sharedousocks', 'sharedousocks.crypto'],
    package_data={
        'sharedousocks': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    sslocal = sharedousocks.local:main
    ssserver = sharedousocks.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
