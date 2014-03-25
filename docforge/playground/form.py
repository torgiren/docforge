#!/usr/bin/env python
#*-* coding: utf8 *-*
from xml.dom import minidom

#tree = minidom.parse('doc.xml')


def parse_object(obj):
    result = ""
    t = obj.getAttribute('type')
    if t == 'input':
        name = obj.getAttribute('name')
        result = "<input type='{type}' name='{name}'/>".format(type=t, name=name)
    elif t == 'label':
        f = obj.getAttribute('for')
        value = obj.getAttribute('value')
        result = "<label for='{f}'>{value}</label>".format(f=f, value=value)
    elif t == 'newline':
        result = "<br/>"
    else:
        result = "Not recognized object"
    return result


def print_c(cont, ident=""):
    result = ""
    result += ident
    result += "<div name={name}>".format(name=cont.getAttribute('name')) + "\n"
    ident += "  "
    for i in [i for i in cont.childNodes if i.nodeName == 'object']:
        result += ident
        result += parse_object(i) + "\n"
    for i in [i for i in cont.childNodes if i.nodeName == 'container']:
        result += print_c(i, ident)
    ident = ident[:-2]
    result += ident
    result += "</div>" + "\n"
    return result

#print print_c(tree.childNodes[0])

