# coding: utf-8

from lxml import etree

page = etree.Element('html')

headElt = etree.SubElement(page, 'head')
bodyElt = etree.SubElement(page, 'body')

title = etree.SubElement(headElt, 'title')
title.text = 'Your page title here'

linkElt = etree.SubElement(headElt, 'link', rel='stylesheet',
    href='mystyle.css', type='text/css')

bodyH1 = etree.SubElement(bodyElt, 'h1')
bodyH1.text = 'Hello people!'
bodyH1 = etree.SubElement(bodyElt, 'p')
bodyH1.text = 'quanto costa'

doc = etree.ElementTree(page)
outFile = open('homemade.html', 'w')
doc.write(outFile)
