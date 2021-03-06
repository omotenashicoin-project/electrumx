import setuptools
version = '1.0.0'

setuptools.setup(
    name='Mtns electrumX',
    version=version,
    scripts=['electrumx_server', 'electrumx_rpc', 'electrumx_compact_history'],
    python_requires='>=3.6',
	install_requires=['aiorpcX>=0.10.1,<0.11', 'attrs',
                      'plyvel', 'pylru', 'aiohttp >= 2'],
    extras_require={
        'rocksdb': ['python-rocksdb>=0.6.9'],
        'uvloop': ['uvloop>=0.12.2'],   # Bump when the uvloop connection_lost bug is fixed
        # For various coins
        'blake256': ['blake256>=0.1.1'],
        'crypto': ['pycryptodomex>=3.8.1'],
        'groestl': ['groestlcoin-hash>=1.0.1'],
        'tribus-hash': ['tribus-hash>=1.0.2'],
        'xevan-hash': ['xeven-hash'],
        'x11-hash': ['x11-hash>=1.4'],
        'zny-yespower-0-5': ['zny-yespower-0-5'],
        'mtns_skein_hash':  ['mtns_skein-hash'],
    },
    packages=setuptools.find_packages(include=('electrumx*',)),
    description='ElectrumX MTNS Server',
    author='mtnsdev',
    author_email='git@omotenashicoin.site',
    license='MIT Licence',
    url='https://github.com/omotenashicoin-project/electrumx.git',
    long_description='Server implementation for the Electrum protocol',
    download_url=('https://github.com/omotenashicoin-project/electrumx/archive/'
                  f'{version}.tar.gz'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        'Topic :: Internet',
    ],
)
