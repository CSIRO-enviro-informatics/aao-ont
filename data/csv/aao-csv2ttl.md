# AAO.csv -> aaos.ttl recipe

## Insert header
```
# baseURI: http://test.linked.data.gov.au/dataset/aaos
# imports: http://linked.data.gov.au/def/aao

@prefix aao: <http://linked.data.gov.au/def/aao#> .
@prefix aaos: <http://test.linked.data.gov.au/dataset/aao/> .
@prefix act: <http://test.linked.data.gov.au/dataset/act/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dept: <http://test.linked.data.gov.au/dataset/dept/> .
@prefix leg: <http://linked.data.gov.au/def/legislation#> .
@prefix matter: <http://test.linked.data.gov.au/dataset/matter/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix reg: <http://linked.data.gov.au/def/reg/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://test.linked.data.gov.au/dataset/aaos>
  a owl:Ontology ;
  owl:imports <http://linked.data.gov.au/def/aao> ;
.
```

## end of lines
Find
```
(\d)"$
```
Replace
```
$1> ; \n.
```

## successively replace last ","
Find *greedy match ending with "."*
```
(.*)(",")
```

### Replace #1
```
$1"^^xsd:date ; ] ;
\t] ;
\trdfs:seeAlso <
```
### Replace #2
```
$1"^^xsd:date ; ] ;
\t\ttime:hasEnd [ a time:Instant ; time:inXSDDate "
```
### Replace #3
```
$1"^^xsd:date ;
\tdct:temporal [ a time:ProperInterval ;
\t\ttime:hasBeginning [ a time:Instant ; time:inXSDDate "
```
### Replace #4
```
$1
\ta aao:AAO ;
\tdct:issued "
```
## beginning of lines
Find
```
^"(\d)
```
Replace
```
aaos:A$1
```
## Check for missing data from syntax errors
