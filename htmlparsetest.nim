import htmlparser
import xmltree  # To use '$' for XmlNode
import strtabs  # To access XmlAttributes
import os       # To use splitFile
import strutils # To use cmpIgnoreCase

#proc transformHyperlinks() =
let html = loadHtml("data/html/crawl_test.html")

for a in html.findAll("a"):
  if a.attrs.hasKey "href":
    echo splitFile(a.attrs["href"])
  
#writeFile("data/html/output.html", v)
