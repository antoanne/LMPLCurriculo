import sys
from lxml import etree

# XML file and corresponding DTD definition
try:
    file = sys.argv[1]
except:
    print '\n\n\t USE: %s <arquivo-cv-lattes> \n\n' %sys.argv[0]
    sys.exit(1)

dtdFile = open('LMPLCurriculo.DTD', 'r')
dtd = etree.DTD(dtdFile)

root = etree.XML(open(file,'r').read())
print(dtd.validate(root))
print(dtd.error_log.filter_from_errors())
