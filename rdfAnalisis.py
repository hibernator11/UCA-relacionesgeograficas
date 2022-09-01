#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:51:21 2022

@author: gustavo
"""
from rdflib import Graph

# Create a Graph
g = Graph().parse("rdf/relaciones_uca.rdf")

print('##### edm:Agent')

# Query the data in g using SPARQL
# This query returns the 'name' of all ``edm:Agent`` instances
q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>

    SELECT ?name
    WHERE {
        ?p rdf:type edm:Agent .

        ?p skos:prefLabel ?name .
    }
"""

# Apply the query to the graph and iterate through results
for r in g.query(q):
    print(r["name"])

print('##### edm:Place')

# Query the data in g using SPARQL
# This query returns the 'name' of all ``edm:Place`` instances
q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>

    SELECT ?name
    WHERE {
        ?p rdf:type edm:Place .

        ?p skos:prefLabel ?name .
    }
"""

# Apply the query to the graph and iterate through results
for r in g.query(q):
    print(r["name"])


print('##### edm:ProvidedCHO')
    
# Query the data in g using SPARQL
# This query returns the 'name' of all ``edm:ProvidedCHO`` instances
q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    SELECT ?title
    WHERE {
        ?p rdf:type edm:ProvidedCHO .

        ?p dc:title ?title .
    }
"""

# Apply the query to the graph and iterate through results
for r in g.query(q):
    print(r["title"])    
    

print('##### ore:Aggregation')
    
# Query the data in g using SPARQL
# This query returns the 'name' of all ``edm:ProvidedCHO`` instances
q = """
    PREFIX ore: <http://www.openarchives.org/ore/terms/>
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    SELECT DISTINCT ?p
    WHERE {
        ?s rdf:type ore:Aggregation .

        ?s ?p ?o.
    }
"""

# Apply the query to the graph and iterate through results
for r in g.query(q):
    print(r["p"])        

