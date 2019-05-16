# Data and examples
A dataset has been assembled by scraping the AAOs for the last 10 years - see https://confluence.csiro.au/display/LongSpineGovFunc/Database

These were exported into a set of CSV's, and converted into RDF for further analysis.

- [AAOs.ttl](data/AAOs.ttl) AAOs formalized using the AAO Ontology and presented in RDF.
- [PARTs.ttl](data/PARTs.ttl) Parts of AAOs
- [PORTFOLIOs.ttl](data/PORTFOLIOs.ttl) Portfolios
- [DEPTs.ttl](data/DEPTs.ttl) Departments of state mentioned in AAOs
- [ACT_NAMEs.ttl](data/ACT_NAMEs.ttl) Legistation mentioned in AAOs and denoted by name
- [MATTERs.ttl](data/MATTERs.ttl) Matters taken from AAOs
- [PART_LEGs.ttl](data/PART_LEGs.ttl) Links from Parts to Administered legislation of AAOs
- [PART_MATs.ttl](data/PART_MATs.ttl) Links from Parts to Matters dealt with of AAOs


Examples from https://github.com/CSIRO-enviro-informatics/aao-ont/data/aao-time.ttl:
```
aaos:A97
  rdf:type aao:AAO ;
  dct:hasPart aaos:P683 ;
  dct:hasPart aaos:P684 ;
  dct:hasPart aaos:P685 ;
  dct:hasPart aaos:P686 ;
  dct:hasPart aaos:P687 ;
  dct:hasPart aaos:P688 ;
  dct:hasPart aaos:P689 ;
  dct:hasPart aaos:P690 ;
  dct:hasPart aaos:P691 ;
  dct:hasPart aaos:P692 ;
  dct:hasPart aaos:P693 ;
  dct:hasPart aaos:P694 ;
  dct:hasPart aaos:P695 ;
  dct:hasPart aaos:P696 ;
  dct:hasPart aaos:P697 ;
  dct:hasPart aaos:P698 ;
  dct:hasPart aaos:P699 ;
  dct:hasPart aaos:P700 ;
  dct:isReplacedBy aaos:A98 ;
  dct:issued "2018-04-19"^^xsd:date ;
  dct:replaces aaos:A96 ;
  dct:temporal [
      rdf:type owlTime:ProperInterval ;
      owlTime:hasBeginning [
          rdf:type owlTime:Instant ;
          owlTime:inXSDDate "2018-05-10"^^xsd:date ;
        ] ;
      owlTime:hasEnd [
          rdf:type owlTime:Instant ;
          owlTime:inXSDDate "2018-08-27"^^xsd:date ;
        ] ;
    ] ;
  rdfs:seeAlso <https://www.legislation.gov.au/Details/C2018Q00017> ;
  owlTime:intervalMeets aaos:A98 ;
  owlTime:intervalMetBy aaos:A96 ;
.

aaos:P696
  rdf:type aao:AAO-Part ;
  aao:administeredLegislation legs:A1106 ;
  aao:administeredLegislation legs:A1193 ;
  aao:administeredLegislation legs:A1280 ;
  aao:administeredLegislation legs:A1284 ;
  aao:administeredLegislation legs:A1384 ;
  aao:administeredLegislation legs:A1446 ;
  aao:administeredLegislation legs:A1447 ;
  aao:administeredLegislation legs:A1449 ;
  aao:administeredLegislation legs:A1453 ;
  aao:administeredLegislation legs:A1454 ;
  aao:administeredLegislation legs:A1519 ;
  aao:administeredLegislation legs:A1627 ;
  aao:administeredLegislation legs:A1688 ;
  aao:administeredLegislation legs:A1822 ;
  aao:administeredLegislation legs:A1888 ;
  aao:administeredLegislation legs:A1889 ;
  aao:administeredLegislation legs:A1890 ;
  aao:administeredLegislation legs:A2033 ;
  aao:administeredLegislation legs:A2088 ;
  aao:administeredLegislation legs:A2089 ;
  aao:administeredLegislation legs:A2090 ;
  aao:administeredLegislation legs:A2091 ;
  aao:administeredLegislation legs:A361 ;
  aao:administeredLegislation legs:A363 ;
  aao:administeredLegislation legs:A366 ;
  aao:administeredLegislation legs:A367 ;
  aao:administeredLegislation legs:A373 ;
  aao:administeredLegislation legs:A380 ;
  aao:administeredLegislation legs:A385 ;
  aao:administeredLegislation legs:A386 ;
  aao:administeredLegislation legs:A387 ;
  aao:administeredLegislation legs:A388 ;
  aao:administeredLegislation legs:A389 ;
  aao:administeredLegislation legs:A392 ;
  aao:matterDealtWith aaos:M283 ;
  aao:matterDealtWith aaos:M395 ;
  aao:matterDealtWith aaos:M423 ;
  aao:matterDealtWith aaos:M424 ;
  aao:matterDealtWith aaos:M454 ;
  aao:matterDealtWith aaos:M466 ;
  aao:matterDealtWith aaos:M504 ;
  aao:matterDealtWith aaos:M56 ;
  aao:matterDealtWith aaos:M59 ;
  aao:matterDealtWith aaos:M64 ;
  aao:part-number 13 ;
  aao:responsibleDepartment auorgs:D56 ;
  auorg:isPartOfPortfolio auorgs:P0 ;
  dct:isPartOf aaos:A97 ;
.

auorgs:D56
  rdf:type auorg:DepartmentOfState ;
  dct:title "Jobs and Small Business" ;
  rdfs:label "Jobs and Small Business" ;
.

legs:A2090
  rdf:type leg:Act ;
  dct:title "Social Security Act 1991, insofar as it relates to the participation and activity test requirements and compliance obligations for participation payment recipients" ;
  rdfs:label "Social Security Act 1991, insofar as it relates to the participation and activity test requirements and compliance obligations for participation payment recipients" ;
.

aaos:M424
  rdf:type aao:Matter ;
  dct:description "Work and family programmes" ;
  rdfs:comment "Work and family programmes" ;
.

```

##  data

These refer to:

### Identifiers
Identifiers for **AAOs** and for **Legislation** are taken from the [Federal Register of Legislation](https://www.legislation.gov.au), e.g.
- [C2010Q00191](data/aaos.ttl) [AAO for 2nd Gillard Administration](https://www.legislation.gov.au/Details/C2010Q00191)
- C2004A01468 [Acts Citation Act 1976](https://www.legislation.gov.au/Details/C2004A01468)
- C2004A04340 [A.C.T. Supreme Court (Transfer) Act 1992](https://www.legislation.gov.au/Details/C2004A04340)
- C2004A04749 [Agricultural and Veterinary Chemical Products Levy Imposition (Customs) Act 1994](https://www.legislation.gov.au/Details/C2004A04749)

What are the best identifiers for
- **Departments** (AGOR is only good for current state)
- **Matters** (text ...)?

How can we align **Matters** to **Functions**?
