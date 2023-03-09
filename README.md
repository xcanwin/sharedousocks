sharedousocks
===========

[![PyPI version]][PyPI]
[![Build Status]][Travis CI]
[![Coverage Status]][Coverage]

A Fast tunnel proxy that helps you access neighboring C-network in a local area network.

Features:
- TCP & UDP support
- User management API
- TCP Fast Open
- Workers and graceful restart
- Destination IP blacklist

Server
------

### Install

Debian / Ubuntu:

    apt-get install python-pip
    cd sharedousocks
    pip install .

CentOS:

    yum install python-setuptools && easy_install pip
    cd sharedousocks
    pip install .

Windows:

See [Install sharedousocks Server on Windows](https://github.com/sharedousocks/sharedousocks/wiki/Install-sharedousocks-Server-on-Windows).

### Usage

    ssserver -p 443 -k password -m aes-256-cfb
    OR
    python -m sharedousocks.server -p 443 -k password -m aes-256-cfb

To run in the background:

    sudo ssserver -p 443 -k password -m aes-256-cfb --user nobody -d start

To stop:

    sudo ssserver -d stop

To check the log:

    sudo less /var/log/sharedousocks.log

Check all the options via `-h`. You can also use a [Configuration] file
instead.

### Usage with Config File

[Create configeration file and run](https://github.com/sharedousocks/sharedousocks/wiki/Configuration-via-Config-File)

To start:

    ssserver -c /etc/sharedousocks.json


Documentation
-------------

You can find all the documentation in the [Wiki](https://github.com/sharedousocks/sharedousocks/wiki).

License
-------

Apache License







[Build Status]:      https://img.shields.io/travis/sharedousocks/sharedousocks/master.svg?style=flat
[Coverage Status]:   https://jenkins.shadowvpn.org/result/sharedousocks
[Coverage]:          https://jenkins.shadowvpn.org/job/sharedousocks/ws/PYENV/py34/label/linux/htmlcov/index.html
[PyPI]:              https://pypi.python.org/pypi/sharedousocks
[PyPI version]:      https://img.shields.io/pypi/v/sharedousocks.svg?style=flat
[Travis CI]:         https://travis-ci.org/sharedousocks/sharedousocks

