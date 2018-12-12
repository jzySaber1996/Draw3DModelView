from xml.etree.ElementTree import parse

et = parse("printParameters.xml")
root = et.getroot()
print(root)
et_print = root.findall('entry[@key="shellLayers"]')[0]
print(et_print.text)
