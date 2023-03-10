About sharedousocks-rm
---------------

This project is https://github.com/sharedousocks/sharedousocks clone. I JUST fix bug on the original code. Unless it is necessary to have additional features.

sharedousocks
===========

|PyPI version| |Build Status| |Coverage Status|

A Fast tunnel proxy that helps you access neighboring C-network in a local area network.

Server
------

Install
~~~~~~~

Debian / Ubuntu:

::

    apt-get install python-pip
    pip install sharedousocks

CentOS:

::

    yum install python-setuptools && easy_install pip
    pip install sharedousocks

Windows:

See `Install Server on
Windows <https://github.com/sharedousocks/sharedousocks/wiki/Install-sharedousocks-Server-on-Windows>`__

Usage
~~~~~

::

    ssserver -p 443 -k password -m rc4-md5

To run in the background:

::

    sudo ssserver -p 443 -k password -m rc4-md5 --user nobody -d start

To stop:

::

    sudo ssserver -d stop

To check the log:

::

    sudo less /var/log/sharedousocks.log

Check all the options via ``-h``. You can also use a
`Configuration <https://github.com/sharedousocks/sharedousocks/wiki/Configuration-via-Config-File>`__
file instead.

Client
------

-  `Windows <https://github.com/sharedousocks/sharedousocks/wiki/Ports-and-Clients#windows>`__
   / `OS
   X <https://github.com/sharedousocks/sharedousocks-iOS/wiki/sharedousocks-for-OSX-Help>`__
-  `Android <https://github.com/sharedousocks/sharedousocks/wiki/Ports-and-Clients#android>`__
   / `iOS <https://github.com/sharedousocks/sharedousocks-iOS/wiki/Help>`__
-  `OpenWRT <https://github.com/sharedousocks/openwrt-sharedousocks>`__

Use GUI clients on your local PC/phones. Check the README of your client
for more information.

Documentation
-------------

You can find all the documentation in the
`Wiki <https://github.com/sharedousocks/sharedousocks/wiki>`__.

License
-------

Copyright 2015 none

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

::

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Bugs and Issues
---------------

-  `Troubleshooting <https://github.com/sharedousocks/sharedousocks/wiki/Troubleshooting>`__
-  `Issue
   Tracker <https://github.com/sharedousocks/sharedousocks/issues?state=open>`__
-  `Mailing list <https://groups.google.com/group/sharedousocks>`__

.. |PyPI version| image:: https://img.shields.io/pypi/v/sharedousocks.svg?style=flat
   :target: https://pypi.python.org/pypi/sharedousocks
.. |Build Status| image:: https://img.shields.io/travis/sharedousocks/sharedousocks/master.svg?style=flat
   :target: https://travis-ci.org/sharedousocks/sharedousocks
.. |Coverage Status| image:: https://jenkins.shadowvpn.org/result/sharedousocks
   :target: https://jenkins.shadowvpn.org/job/sharedousocks/ws/PYENV/py34/label/linux/htmlcov/index.html
