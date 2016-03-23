#!/usr/bin/env python

import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        
        #filter word based on your choice
        #lets filter words which start with "some"
        key = 'some'
        if word.startswith(key):
            print '%s\t%s' % (key, 1)
