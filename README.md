metaBPM.py
==========

A small script that uses the Echo Nest Remix API to analyze and add BPM information to your music collection.

Usage
-----
	$$python metaBPM.py -s [path to your music collection]

Requirements
------------

* [Echo Nest Remix API](http://echonest.github.com/remix/)
* [eyed3](http://eyed3.nicfit.net/) *For retrieving and manipulating metadata information*

An Important Note
------------------

The Echo Nest API does not do local processing. It calculates the audio fingerprint, and either uploads it to the server if it has no record of it or draws the analysis from an earlier upload. Either way, 
the fact that it is unable to calculate and output the BPM information locally makes this an inefficient solution for a large input of music files. Unless of course the user is unhindered by bandwidth and time limitations.

