#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:40:15 2022

@author: gustavo
"""

import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
import urllib.parse #for parsing strings to URI's
import numpy as np

df=pd.read_csv('rdf/enrichment-wikidata-geonames.csv',sep=",",quotechar='"',dtype={'geonames': str})
print(df)

g = Graph()
owl = Namespace('http://www.w3.org/2002/07/owl#')

for index, row in df.iterrows():
    
    if not pd.isnull(row['wikidata']):
        g.add((URIRef(row['url']), URIRef(owl+'sameAs'), URIRef('https://www.wikidata.org/wiki/' + str(row['wikidata'])) ))
    if not pd.isnull(row['geonames']):   
        g.add((URIRef(row['url']), URIRef(owl+'sameAs'), URIRef('https://www.geonames.org/' + str(row['geonames'])) ))
   
    
print(g.serialize(format='turtle'))

g.serialize('rdf/sameAslinks.xml',format='xml')
    