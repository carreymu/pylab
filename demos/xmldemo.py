from xml.etree.ElementTree import parse, Element, tostring, iterparse
from urllib.request import urlopen
import xml.dom.minidom
import os

def dict_to_xml(tag, d):
    '''
    turn a simple dict of key/value pairs into xml
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

class XMLNammespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'
    def __call__(self, path):
        return path.format_map(self.namespaces)


if __name__ == "__main__":
    print("============xml convert============")
    u = urlopen("http://planet.python.org/rss20.xml")
    print(u)

    filepath = 'file/xmldemo.xml'
    if os.path.exists(filepath):
        dom = xml.dom.minidom.parse(filepath)
        root = dom.documentElement
        print(root.nodeName)
        print(root.nodeValue)
        print(root.nodeType)
        print(root.ELEMENT_NODE)

        doc = parse(filepath)
        roots = doc.getroot()
        # print(root.find('language'))

        if roots.find('language') is not None:
            roots.remove(roots.find('language'))
            roots.getchildren().index(roots.find('description'))

        # oops,fail to insert.
        el = Element('spam')
        el.text = "this is a test"
        roots.insert(2, el)


        # ns = XMLNammespaces(html="http://purl.org/dc/elements/1.1/")
        # ht = doc.find(ns('content/{html}/html'))
        # print(ht)
        # title =doc.findtext(ns('content/{html}html/{html}head/{html}title'))
        # print(title)
        print("============read xml by iterparse============")
        for evt, elem in iterparse(filepath,('end', 'start-ns', 'end-ns')):
            print(evt, elem)


    print("============read xml============")
    doc = parse(u)
    print(doc)

    e = doc.find('channel/link')
    print(e.get('title'))
    print("e.tag:{},e.text:{}".format(e.tag,e.text))

    print("============for loop============")
    i = 0
    for item in doc.iterfind("channel/item"):
        title = item.findtext("title")
        date = item.findtext("pubDate")
        link = item.findtext("link")
        i = i + 1
        print(title)
        print(date)
        print(link)
        if i>2:
            break

    print("============dict to xml============")
    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    ee = dict_to_xml('stock', s)
    print(e)

    print("string1:", tostring(ee))

    ee.set("_id","1234")
    ee.set("_id1", "1s")

    # ee = doc.find('stock/name')
    # ee.set("_id1", "1s")
    print("string2:", tostring(ee))