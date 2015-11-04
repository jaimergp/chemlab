chemlab - the python chemistry package you were waiting for
===========================================================

[![Downloads](https://pypip.in/d/chemlab/badge.png)](https://crate.io/package/chemlab)
[![Build Status](https://travis-ci.org/chemlab/chemlab.svg?branch=master)](https://travis-ci.org/chemlab/chemlab)

- Version: 0.4.1
- Author: Gabriele Lanaro
- Contributors: Yotam Y. Avital, Adam Jackson, Jaime Rodriguez-Guerra
- Email: python-chemlab@googlegroups.com
- Website: http://chemlab.github.com/chemlab
- Docs: http://chemlab.rtfd.org
- Github: http://github.com/chemlab/chemlab

chemlab is a python library and a set of utilities built to ease the
life of the computational chemist. It takes inspiration from other
python scientific library such as numpy, scipy and matplotlib, and aims
to bring a consistent and simple API by following the python
guidelines.


Computational and theoretical chemistry is a huge field, and providing
a program that encompasses all aspect of it is an impossible task. The
spirit of chemlab is to provide a common ground from where you can
build specific programs. For this reason it includes an easily
extendable molecular viewer and flexible field-independent data
structures.

chemlab is looking for contributors, it includes a good documentation
and has an easy structure to get in. Feel free to send me anything that
you may do with chemlab, from supporting a new file format to writing
a new graphic renderer, even if you don'think it's perfect. Send me an
email or write an issue on the github page.

Installation
------------

TIP: more updated instructions are located in the docs:
     http://chemlab.readthedocs.org/en/latest/installation.html

The easiest way to install chemlab is to use the Anaconda python distribution from the following link.

http://continuum.io/downloads

Then you can run the following command:

    conda install -c http://conda.binstar.org/gabrielelanaro chemlab

You can also install chemlab on Ubuntu 14.04 using apt. First install the dependencies:

    $ sudo apt-get install python-numpy python-scipy python-opengl cython python-matplotlib python-qt4-gl python-qt4

Then install chemlab from the setup.py included:

    $ sudo python setup.py install

NOTE: For python3 support install the corresponding python3
      packages available in your distribution or use pip.

Documentation
-------------

Refer to the documentation link at the beginning of this file.

Bug Reports
-----------

Go to http://github.com/chemlab/chemlab or send an email to python-chemlab@googlegroups.com.

License
-------

chemlab is released under the GNU LGPL license if the PyQt parts are omitted (such as chemlab.graphics and chemlab.mviewer packages) or the GNU GPL3 license otherwise. See lgpl.txt and gpl.txt files attached.
