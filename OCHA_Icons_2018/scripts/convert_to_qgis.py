import os
import xml.etree.ElementTree as ET
import helpers

sourceDir = '../original_un_blue_versions/svg'
destDir = '../qgis_versions_ETparser_test/svg'

svgNs = 'http://www.w3.org/2000/svg'
ET.register_namespace('', svgNs)

files = os.listdir(sourceDir)

tags = ('path', 'polygon', 'circle', 'rect')
uriPrefixedTags = ['{{{0}}}'.format(svgNs) + s for s in tags]

qgisStylingAttributes = {'fill': 'param(fill)',
                     'stroke': 'param(outline)',
                     'stroke-width': 'param(outline-width) 0'}

for file in files:
    sourceFile = os.path.join(sourceDir, file)
    destFile = os.path.join(destDir, file)
    #print(sourceFile)
    #print(destFile)

    tree = ET.parse(sourceFile)
    root = tree.getroot()

    enlargedViewbox = helpers.enlargeViewboxSize(root.get('viewBox'), 1)
    root.set('viewBox', enlargedViewbox)

    for element in root.iter():
        if element.tag in uriPrefixedTags:
            element.attrib.pop('class', None)
            element.attrib.update(qgisStylingAttributes)
            #print(element.attrib)

    tree.write(destFile, encoding='utf-8')