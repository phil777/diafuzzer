#!/usr/bin/python

from Dia import Directory
from cPickle import dump
from datetime import datetime

print('creating Directory instance, this might take a while ...')

start = datetime.now()
d = Directory()
stop = datetime.now()

print('created in %s dumping to .dia-cache' % (stop-start))

print('contains the following applications:')
for app in d.apps:
  print('%s\t\t%d (0x%x)' % (app.name, app.id, app.id))

with open('.dia-cache', 'wb') as f:
  dump(d, f)
