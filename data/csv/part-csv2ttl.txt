PART.csv -> PARTs.ttl recipe

1. Insert header
>>>
# baseURI: http://test.linked.data.gov.au/dataset/aaops
# imports: http://linked.data.gov.au/def/aao
# imports: http://linked.data.gov.au/def/auorg

@prefix aao: <http://linked.data.gov.au/def/aao#> .
@prefix aaos: <http://test.linked.data.gov.au/dataset/aao/> .
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

<http://test.linked.data.gov.au/dataset/aaops>
  a owl:Ontology ;
  owl:imports <http://linked.data.gov.au/def/aao> ;
  owl:imports <http://linked.data.gov.au/def/auorg> ;
.
<<<
2. end of lines
(a)
Find
,$
Replace
,"0"

(b)
Find
(\d)"$
Replace
$1 ; \n.

3. successively replace last ","
Find
(.*)(",")

Replace #1
$1 ; \n\tauorg:isPartOfPortfolio auorgs:P


Replace #2
$1 ; \n\taao:responsibleDepartment auorgs:D

Replace #3
$1 ; \n\tdct:isPartOf aaos:A

Replace #4
$1 ; \n\taao:part-number 

4. beginning of lines
Find
^"(\d)
Replace
aaos:P$1 a aao:AAO-Part

5. Check for missing data from syntax errors
