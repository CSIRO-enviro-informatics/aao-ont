PORTFOLIO.csv -> PORTFOLIOs.ttl recipe

1. Insert header
>>>
# baseURI: http://test.linked.data.gov.au/dataset/auorgps
# imports: http://linked.data.gov.au/def/auorg

@prefix auorg: <http://linked.data.gov.au/def/auorg/> .
@prefix auorgs: <http://test.linked.data.gov.au/dataset/auorg/> .
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

<http://test.linked.data.gov.au/dataset/auorgps>
  a owl:Ontology ;
  owl:imports <http://linked.data.gov.au/def/auorg> ;
.
<<<

2. end of lines
Find
"$
Replace
" ; \n.

3. successively replace last ","
Find
(.*)(",")

Replace #1
$1 a auorg:Portfolio ; \n\tdct:title "


4. beginning of lines
Find
^"(\d)
Replace
auorgs:P$1

5. Check for missing data from syntax errors
