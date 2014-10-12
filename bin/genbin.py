#!/usr/bin/env python

import re,sys,os,binascii
if len(sys.argv) < 3:
	print >>sys.stderr,"Usage: %s infile outfile"%sys.argv[0]
	sys.exit(1)

infile=sys.argv[1]
outfile=sys.argv[2]

if not os.path.isfile(infile):
	print >>sys.stderr,"Please pass a valid input file"
	sys.exit(1)

if os.path.exists(outfile):
	print >>sys.stderr,"Output file exists"
	sys.exit(1)


fh=open(infile,"r")
ofh=open(outfile,"wb")

out=""
c=0
num=0
for a in fh.readlines():
	for b in a:
		if re.match('[A-Za-z]',b):
			c=c+1
			num=num*2
			if re.match('[A-Z]',b):
				num=num+1
		if c==4:
			d=re.sub('^0x','',hex(num))
			out="%s%s"%(out,d)
			num=0
			c=0
			

ofh.write(binascii.a2b_hex(out))
