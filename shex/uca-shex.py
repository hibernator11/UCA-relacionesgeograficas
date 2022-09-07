from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
  "http://www.europeana.eu/schemas/edm/WebResource",
  "http://www.openarchives.org/ore/terms/Aggregation"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://www.w3.org/2000/01/rdf-schema#": "rdfs", 
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://www.cidoc-crm.org/cidoc-crm/": "cidoc-crm",
                   "http://schema.org/": "schema",
                   "http://rdfs.org/ns/void#": "void",
                   "http://creativecommons.org/ns#": "creativeCommons",
                   "http://purl.org/dc/terms/": "dc",
                   "http://www.w3.org/2003/01/geo/wgs84_pos#": "geo",
                   "http://purl.org/ontology/bibo/": "bibo",
                   "http://data.archiveshub.ac.uk/def/": "dev",
                   "http://www.openarchives.org/ore/terms/": "ore",
                   "http://www.europeana.eu/schemas/edm/": "edm"
                   }

#url_endpoint="https://slod.fiz-karlsruhe.de/sparql"
input_nt_file = '../rdf/relaciones_uca.ttl'

shaper = Shaper(#target_classes=target_classes,
                #raw_graph=raw_graph,
                graph_file_input=input_nt_file,
                #url_endpoint=url_endpoint, 
                #input_format=NT,
                all_classes_mode=True,
                input_format="turtle",
                limit_remote_instances=20,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_uca.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")
