import sys
from xml.parsers.xmlproc import xmlproc
from xml.parsers.xmlproc import xmlval
from xml.parsers.xmlproc import xmldtd

# XML file and corresponding DTD definition
try:
    file = sys.argv[1]
except:
    print '\n\n\t USE: %s <arquivo-cv-lattes> \n\n' %sys.argv[0]
    sys.exit(1)

dtd  = 'LMPLCurriculo.DTD'

d = xmldtd.load_dtd(dtd)
p = xmlval.XMLValidator()
p.parse_resource(file)
