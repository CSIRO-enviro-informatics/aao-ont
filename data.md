# Data and examples
A dataset has been assembled by scraping the AAOs for the last 10 years - see https://confluence.csiro.au/display/LongSpineGovFunc/Database

These were exported into a set of CSV's, and converted into RDF using the [AAO Ontology](README.md).
The information is factored into a number of files (graphs):

- [AAOs.ttl](data/AAOs.ttl) AAOs each with their dates of validity
- [PARTs.ttl](data/PARTs.ttl) Parts of AAOs with their department (and portfolio if available), each linked back to the AAO it belongs to
- [PORTFOLIOs.ttl](data/PORTFOLIOs.ttl) Portfolios mentioned in AAOs denoted by name
- [DEPTs.ttl](data/DEPTs.ttl) Departments of state mentioned in AAOs denoted by name
- [ACT_NAMEs.ttl](data/ACT_NAMEs.ttl) Legislation mentioned in AAOs and denoted by name
- [MATTERs.ttl](data/MATTERs.ttl) Matters taken from AAOs expressed as text
- [PART_LEGs.ttl](data/PART_LEGs.ttl) Links from Parts to Administered legislation of AAOs
- [PART_MATs.ttl](data/PART_MATs.ttl) Links from Parts to Matters dealt with of AAOs

These can be viewed together in [data/aao-all.ttl](data/aao-all.ttl).

## Processing
### Inverse relations
```
INSERT {
	?aao dct:hasPart ?aaop ;
}
WHERE {
	?aaop a aao:AAO-Part ;
		dct:isPartOf ?aao .
}
```
### Time sequence
Processing the AAOs into a time-sequence with OWL-Time relationships is described in [aao-time-processing](aao-time-processing.md) - results in [aao-time.ttl](data/aao-time.ttl)

### Responsibility for Functions
Processing the AAOs to get a view of functional responsibility is described in [function-responsibility](function-responsibility.md) - results in [aao-all.ttl](data/aao-all.ttl)

## Preview

```
aaos:A97
  rdf:type aao:AAO ;
  dct:hasPart aaos:P683 ;
  dct:hasPart aaos:P684 ;
  dct:hasPart aaos:P685 ;
  dct:hasPart aaos:P686 ;
  [...]
  dct:hasPart aaos:P696 ;
  [...]
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
.

aaos:P696
  rdf:type aao:AAO-Part ;
  aao:administeredLegislation legs:A1106 ;
  aao:administeredLegislation legs:A1193 ;
  aao:administeredLegislation legs:A1280 ;
  aao:administeredLegislation legs:A1284 ;
  [...]
  aao:administeredLegislation legs:A2090 ;
  [...]
  aao:matterDealtWith aaos:M283 ;
  aao:matterDealtWith aaos:M395 ;
  aao:matterDealtWith aaos:M423 ;
  aao:matterDealtWith aaos:M424 ;
  [...]
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
