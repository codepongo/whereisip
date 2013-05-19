#!/usr/bin/env python
# coding: utf-8

import sys
import qqwry
import ip2nation
def main():
    i = qqwry.IPInfo('QQWry.Dat')
    if len(sys.argv) == 2:
        (c, a) = i.getIPAddr(sys.argv[1])
    else:
        print ("""\
USAGE:
%s <ip>
""" % sys.argv[0])
        return

    if sys.platform == 'win32':
        c = unicode(c, 'utf-8').encode('gb2312')
        a = unicode(a, 'utf-8').encode('gb2312')
    print '%s %s/%s' % (sys.argv[1], c, a)
    print str(ip2nation.nation(sys.argv[1])[0][0])

if __name__ == '__main__':
    main()

#vim:tabexpand=on
