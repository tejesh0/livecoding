#! /usr/bin/python
import sys
import os
import xmpp

if len(sys.argv) < 2:
    print "Syntax : xsend JID text"
    sys.exit(0)

tojid = sys.argv[1]
text = ' '.join(sys.argv[2:])
