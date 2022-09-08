from pyshex.evaluate import evaluate
from rdflib import Graph, Namespace, XSD



# ShEx Expression
shex = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.org/>
PREFIX weso-s: <http://weso.es/shapes/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX cidoc-crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX schema: <http://schema.org/>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX creativeCommons: <http://creativecommons.org/ns#>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX bibo: <http://purl.org/ontology/bibo/>
PREFIX dev: <http://data.archiveshub.ac.uk/def/>
PREFIX ore: <http://www.openarchives.org/ore/terms/>
PREFIX edm: <http://www.europeana.eu/schemas/edm/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX vcard: <http://www.w3.org/2006/vcard/ns#>
PREFIX uca: <https://unlockingarchives.com/relaciones/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

start = @weso-s:Aggregation

weso-s:Place
{
   rdf:type  [edm:Place]  ;                                    # 100.0 %
   geo:long  xsd:string  +;                                    # 100.0 %
            # 94.11764705882352 % obj: xsd:string. Cardinality: {1}
   geo:lat  xsd:string  +;                                     # 100.0 %
            # 94.11764705882352 % obj: xsd:string. Cardinality: {1}
   skos:prefLabel  rdf:langString  +                           # 100.0 %
            # 88.23529411764706 % obj: rdf:langString. Cardinality: {1}
}


weso-s:WebResource
{
   rdf:type  [edm:WebResource]  ;                              # 100.0 %
   edm:rights  IRI                                             # 100.0 %
}


weso-s:ProvidedCHO
{
   rdf:type  [edm:ProvidedCHO]  ;                              # 100.0 %
   dc:rights  IRI  ;                                           # 100.0 %
   schema:thumbnail  IRI  ;                                    # 100.0 %
   dc:coverage  rdf:langString *;                              # 100.0 %
   dc:description  rdf:langString  ;                           # 100.0 %
   dc:spatial  @weso-s:Place  *;                                # 100.0 %
   dc:publisher  rdf:langString  ;                             # 100.0 %
   dc:issued  xsd:date  *;                                      # 100.0 %
   dc:identifier  xsd:string  {2};                             # 100.0 %
   dc:alternative  rdf:langString  *;                           # 100.0 %
   dc:subject  rdf:langString  ;                               # 100.0 %
   dc:language  rdf:langString  ;                              # 100.0 %
   dc:contributor  IRI  +;                                     # 100.0 %
   edm:hasType  rdf:langString  *;                              # 100.0 %
   edm:hasType  IRI *; 
   dc:date  xsd:date  ;                                        # 100.0 %
   dc:title  rdf:langString  ;                                 # 100.0 %
   dc:extent  rdf:langString  *;                                # 100.0 %
   dc:coverage  IRI  *;
            # 97.53086419753086 % obj: IRI. Cardinality: {1}
   dc:creator  IRI  *
            # 92.5925925925926 % obj: IRI. Cardinality: +
            # 86.41975308641975 % obj: @weso-s:Agent. Cardinality: +
}


weso-s:Aggregation
{
   rdf:type  [ore:Aggregation]  ;                              # 100.0 %
   edm:isShownBy  IRI  ;                                       # 100.0 %
   edm:hasView  @weso-s:WebResource  +;                        # 100.0 %
            # 91.35802469135803 % obj: @weso-s:WebResource. Cardinality: {2}
   edm:isShownAt  IRI  ;                                       # 100.0 %
   edm:aggregatedCHO  @weso-s:ProvidedCHO  ;                   # 100.0 %
   dc:isReferencedBy  IRI  *;                                   # 100.0 %
   edm:dataProvider  rdf:langString                            # 100.0 %
}


weso-s:Agent
{
   rdf:type  [edm:Agent]  ;                                    # 100.0 %
   skos:prefLabel  xsd:string                                  # 100.0 %
}


weso-s:Dataset
{
   rdf:type  [void:Dataset]  ;                                 # 100.0 %
   foaf:homepage  @weso-s:Dataset  ;                           # 100.0 %
   dc:publisher  xsd:string  ;                                 # 100.0 %
   dc:description  rdf:langString                              # 100.0 %
}


weso-s:Concept
{
   rdf:type  [skos:Concept]  ;                                 # 100.0 %
   skos:prefLabel  rdf:langString                              # 100.0 %
}
"""


g = Graph()
g.parse("../rdf/relaciones_uca.ttl")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/20c443dd-6b30-4629-8ddf-04c9703bdd3e")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/209aa6dc-a36e-46f7-9207-0d044ecfe86b")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/15fe4b37-7b5c-48f5-acc8-0858ff0d1d47")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/627cf1b7-9f91-4df6-8101-c5a8b5e55272")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/6f42ff06-ff73-4471-9454-d3a264276d67")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/1dafc85c-ba6b-45cc-8975-fd9b2cfd1f2b")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/9e9ca33c-2580-4851-86c2-0760d62fa7fb")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/5e2afb53-d229-48e1-a279-bd6c707edb69")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/d3b0a22d-e861-4ccd-a7df-b2be938c1b00")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

rslt, reason = evaluate(g, shex, focus="https://unlockingarchives.com/relaciones/aggregation/874cc4b5-f987-4987-a640-b60133be3d07")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")

