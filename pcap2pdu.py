#!/usr/bin/env python

import sys

from Pdml import PdmlLoader
from Diameter import Msg
from cStringIO import StringIO

if __name__ == '__main__':
  pcap = sys.argv[1]

  c = PdmlLoader(pcap)

  for pdu in c.pdus:
    m = Msg.decode(pdu.content)

    print('''# frame %d
%r
''' % (pdu.pdml.frm_number, m))
