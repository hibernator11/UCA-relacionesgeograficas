# UCA-relacionesgeograficas
UCA collection relaciones geográficas

### Introducción

Proyecto para la extracción y transformación de la colección digital Relaciones Geográficas a un modelo semántico basado en el vocabulario [European Data Model](https://pro.europeana.eu/page/edm-documentation).

En este prototipo se han seleccionado [20 obras](input/manifests.txt).



### Roles autoridad
- creator: signer, artist
- contributor: interpreter, collector, scribe, contributor, witness

Otros posibles modelos:
- https://data.bnf.fr/vocabulary/roles/
- http://www.rdaregistry.info/Elements/a/#P50204

### Clases (Europeana Data Model y otros...)
- void:Dataset https://txarchives.org/utlac/finding_aids/00056.xml
- edm:Place
- ore:Aggregation
- edm:ProvidedCHO
- edm:WebResource

### URLs patterns
- https://unlockingarchives.com/relaciones/place/papantladeolarte
- https://unlockingarchives.com/relaciones/aggregation/50098d40-75e0-4f70-8622-6c156da2e45d
- https://unlockingarchives.com/relaciones/cho/50098d40-75e0-4f70-8622-6c156da2e45d
- https://unlockingarchives.com/relaciones/autor/gutierrezdeliebana-juan

### Enriquecimiento

- dc:coverage http://vocab.getty.edu/aat/300404510 (sixteenth century)
- edm:hasType http://vocab.getty.edu/aat/300028233 (historical maps)


### Pendiente
- Usar skos:Concept para materias. Ahora se usa dc:subject con el texto completo. Sería necesario dividir las conceptos de las materias.
- Enriquecer los autores con identificadores externos como wikidata/viaf
- Enriquecer los lugares con identificadores de GeoNames
- Ampliar el repositorio con todos los elementos originales. Prototipo con 20 items.
- edm:Place dividir en country-state-city skos:prefLabel 
- Establecer roles
- Completar relaciones de autores
- Añadir texto, anotaciones? https://pro.europeana.eu/files/Europeana_Professional/Share_your_data/Technical_requirements/EDM_profiles/EDM_Annotation_Profile_v1.2.pdf


### Referencias

- https://pro.europeana.eu/files/Europeana_Professional/Share_your_data/Technical_requirements/EDM_Documentation/EDM_Mapping_Guidelines_v2.4_102017.pdf
- https://pro.europeana.eu/files/Europeana_Professional/Share_your_data/Technical_requirements/EDM_profiles/IIIFtoEDM_profile_042016.pdf (IIIF EDM extension guidelines)
- https://www.loc.gov/bibframe/docs/bibframe2-model.html
