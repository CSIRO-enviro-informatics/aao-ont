# Administrative Arrangement Orders ontology

This is an [OWL2](https://www.w3.org/OWL/) ontology that models the elements within the Australian Government's Administrative Arrangement Orders (AAOs).

This ontology and instance data have been created for the *Longitudinal Spine of Government Functions* project which is
a [Platforms for Open Data](https://pmc.gov.au/public-data/open-data/platforms-open-data)-funded project involving
[CSIRO](https://www.csiro.au/), the [Department of Finance](https://www.finance.gov.au/), the [National Archives of
Australia](http://naa.gov.au/) and other interested agencies.

## Source
This ontology is based on the current structure of an AAO instance as listed at the [Federal Register of Legislation](https://www.legislation.gov.au/Browse/ByRegDate/AdministrativeArrangementsOrders/), e.g. [AAO for "2nd Gillard Adminstration"](https://www.legislation.gov.au/Details/C2010Q00191)
.
A [comprehensive archive of AAOs](http://www.naa.gov.au/information-management/information-governance/aao/index.aspx) is also available from the
[National Archives of Australia](http://www.naa.gov.au).

## Classes
### Administrative Arrangement Order structure
An `AAO` is composed of a set of numbered `Parts`, each relating to a single `Department of State` which provides a list of the `matters dealt with` and the `legislation administered` by the department. Each `Matter` is expressed as a text phrase. Each item of `Legislation` is either (i) one dated `Act` optionally excluding one or more `parts`, or (ii) one or more parts of an Act.  Thus, the ontology includes classes for each of these concepts:

![](image/aao.png)

Figure: The AAO ontology's main classes and properties.

`aao:AAO` is an Administrative Arrangements Order. When issued, it replaces the previous AAO. The time interval that it is in force is indicated using `dct:temporal` and ends when it is replaced. It is subject to amendment by a `aao:AAO-Amendment`

`aao:AAO-Part` is an **Association Class** which
- links the **department** to the **matters** and **legislation** that it is responsible for **while this AAO is in force**
- asserts the existence of a **matter** specified using the given wording, while this AAO is in force

Administered legislation refers to an `leg:Act`, optionally with excluded parts that are administered by another department.

`leg:Act` is an Act of Parliament. The year that it was enacted is indicated by the `dct:date`. An Act is composed of one or more `leg:Act-Part`

`aao:Qualified-Act` is a collection which refers to either
- an `leg:Act` excluding some `leg:Act-Part(s)`, else to
- a group of `leg:Act-Part` excluded from the administrative responsibility of another department.

`leg:Legislation` is the superclass of acts, legislative-, notifiable-, and prerogative-instruments, which are listed in the [Federal Register of Legislation](https://www.legislation.gov.au/Home).

`aao:Matter` is an area of responsibility denoted by its `rdfs:label` which is a descriptive phrase.

The description of each Department of State should be formalized as an `auorg:DepartmentOfState` using the [Au Org Ontology](https://github.com/CSIRO-enviro-informatics/auorg-ont

Code example:

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
See [aaos-test.ttl](./data/aaos-test.ttl).

### Responsibility for legislation and matters
Each `AAO` describes a set of responsibilities from an organizational viewpoint, sorted by each Department of State, over a specified time interval.
A more functional view, centered on legislation and matters, can be constructed from this.

The sequence of responsibility for Matters can be computed using this SPARQL query:
```
SELECT ?matter ?dept ?begin ?end
WHERE {
	?m a aao:Matter ;
		dct:description ?matter .
	?part a aao:AAO-Part ;
		dct:isPartOf ?aao ;
		aao:responsibleDepartment/dct:title ?dept ;
		aao:matterDealtWith ?m .
  ?aao dct:temporal/time:hasBeginning/time:inXSDDate ?begin .
  OPTIONAL { ?aao dct:temporal/time:hasEnd/time:inXSDDate ?end . }
}
ORDER BY ?matter ASC(?begin)
```
| matter | dept | begin | end |
| --- | --- | --- | --- |
| ... | ... | ... | ... |
| Energy efficiency | Environment, Water, Heritage and the Arts | 2008-01-25 | 2008-04-30 |
| Energy efficiency | Environment, Water, Heritage and the Arts | 2008-05-01 | 2010-03-07 |
| Energy efficiency | Climate Change and Energy Efficiency | 2010-03-08 | 2010-05-05 |
| Energy efficiency | Climate Change and Energy Efficiency | 2010-05-06 | 2010-06-28 |
| Energy efficiency | Climate Change and Energy Efficiency | 2010-06-29 | 2010-09-13 |
| Energy efficiency | Climate Change and Energy Efficiency | 2010-09-14 | 2010-10-13 |
| Energy efficiency | Climate Change and Energy Efficiency | 2010-10-14 | 2011-10-18 |
| Energy efficiency | Climate Change and Energy Efficiency | 2011-10-19 | 2011-12-06 |
| Energy efficiency | Climate Change and Energy Efficiency | 2011-12-07 | 2011-12-13 |
| Energy efficiency | Climate Change and Energy Efficiency | 2011-12-14 | 2012-02-08 |
| Energy efficiency | Climate Change and Energy Efficiency | 2012-02-09 | 2013-03-24 |
| Energy efficiency | Resources, Energy and Tourism | 2013-03-25 | 2013-05-15 |
| Energy efficiency | Resources, Energy and Tourism | 2013-05-16 | 2013-09-17 |
| Energy efficiency | Industry | 2013-09-18 | 2013-10-02 |
| Energy efficiency | Industry | 2013-10-03 | 2013-12-12 |
| Energy efficiency | Industry | 2013-12-12 | 2014-12-22 |
| Energy efficiency | Industry and Science | 2014-12-23 | 2015-07-08 |
| Energy efficiency | Industry and Science | 2015-07-09 | 2015-09-20 |
| Energy efficiency | Industry, Innovation and Science | 2015-09-21 | 2015-09-29 |
| Energy efficiency | Industry, Innovation and Science | 2015-09-30 | 2016-02-17 |
| Energy efficiency | Industry, Innovation and Science | 2016-02-18 | 2016-07-18 |
| Energy efficiency | Environment and Energy | 2016-07-19 | 2016-08-31 |
| Energy efficiency | Environment and Energy | 2016-09-01 | 2016-10-26 |
| Energy efficiency | Environment and Energy | 2016-10-27 | 2017-04-12 |
| Energy efficiency | Environment and Energy | 2017-04-13 | 2017-11-29 |
| Energy efficiency | Environment and Energy | 2017-11-30 | 2017-12-19 |
| Energy efficiency | Environment and Energy | 2017-12-20 | 2018-04-18 |
| Energy efficiency | Environment and Energy | 2018-04-19 | 2018-05-09 |
| Energy efficiency | Environment and Energy | 2018-05-10 | 2018-08-27 |
| Energy efficiency	| Environment and Energy | 2018-08-28	|  |
| Energy efficiency policy and standards | Climate Change | 2007-12-03 | 2008-01-24 |
| Energy policy | Resources, Energy and Tourism | 2007-12-03 | 2008-01-24 |
| Energy policy | Resources, Energy and Tourism | 2008-01-25 | 2008-04-30 |
| Energy policy | Resources, Energy and Tourism | 2008-05-01 | 2010-03-07 |
| ... | ... | ... | ... |

The sequence of responsibility for Legislation can be computed using this SPARQL query:
```
SELECT ?act ?dept ?begin ?end
WHERE {
	?a a leg:Act ;
		dct:title ?act .
	?part a aao:AAO-Part ;
		dct:isPartOf ?aao ;
		aao:responsibleDepartment/dct:title ?dept ;
		aao:administeredLegislation ?a .
  ?aao dct:temporal/time:hasBeginning/time:inXSDDate ?begin .
  OPTIONAL { ?aao dct:temporal/time:hasEnd/time:inXSDDate ?end . }
}
ORDER BY ?act ASC( ?begin )
```
| act | dept | begin | end |
| --- | --- | --- | --- |
| ... | ... | ... | ... |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2001-11-26 | 2003-12-17 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2003-12-18 | 2004-10-25 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2004-10-26 | 2004-12-15 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2004-12-16 | 2005-07-20 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2005-07-21 | 2006-01-26 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2006-01-27 | 2006-09-20 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2006-09-21 | 2007-01-29 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Employment and Workplace Relations | 2007-01-30 | 2007-12-02 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Education, Employment and Workplace Relations | 2007-12-03 | 2008-01-24 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Education, Employment and Workplace Relations | 2008-01-25 | 2008-04-30 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Education, Employment and Workplace Relations | 2008-05-01 | 2010-03-07 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Education, Employment and Workplace Relations | 2010-03-08 | 2010-05-05 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Education, Employment and Workplace Relations | 2010-05-06 | 2010-06-28 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2010-06-29 | 2010-09-13 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2010-09-14 | 2010-10-13 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2010-10-14 | 2011-10-18 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2011-10-19 | 2011-12-06 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2011-12-07 | 2011-12-13 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Infrastructure and Transport | 2011-12-14 | 2012-02-08 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2012-02-09 | 2013-03-24 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2013-03-25 | 2013-05-15 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2013-05-16 | 2013-09-17 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2013-09-18 | 2013-10-02 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2013-10-03 | 2013-12-12 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2013-12-12 | 2014-12-22 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2014-12-23 | 2015-07-08 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2015-07-09 | 2015-09-20 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2015-09-21 | 2015-09-29 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2015-09-30 | 2016-02-17 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2016-02-18 | 2016-07-18 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2016-07-19 | 2016-08-31 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2016-09-01 | 2016-10-26 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2016-10-27 | 2017-04-12 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2017-04-13 | 2017-11-29 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2017-11-30 | 2017-12-19 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2017-12-20 | 2018-04-18 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2018-04-19 | 2018-05-09 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2018-05-10 | 2018-08-27 |
| Equal Employment Opportunity (Commonwealth Authorities) Act 1987 | Prime Minister and Cabinet | 2018-08-28 |  |
| Equal Employment Opportunity for Women in the Workplace Act 1999 | Employment and Workplace Relations | 2001-11-26 | 2003-12-17 |
| Equal Opportunity for Women in the Workplace Act 1999 | Employment and Workplace Relations | 2003-12-18 | 2004-10-25 |
| Equal Opportunity for Women in the Workplace Act 1999 | Employment and Workplace Relations | 2004-10-26 | 2004-12-15 |
| Equal Opportunity for Women in the Workplace Act 1999 | Employment and Workplace Relations | 2004-12-16 | 2005-07-20 |
| ... | ... | ... | ... |

### Persistent representation of responsibility

Since legislation and matters typically persist across multiple AAOs, with the responsibility either remaining with or passing from one department to another when a new AAO is issued, the functional view will be a time-sequence of associations from the function to the responsible department.
There are several complications in mapping this data to a strict functional timeline, including
- Departments routinely change name as their responsibilities shift
- 'matters' are denoted by a text phrase, which may shift for either substantial reasons, or due to minor wording changes that have no significance of substance
- ...

A generic structure for expressing the sequence of responsibility which respects the formal conceptualization of the AAO is summarized in this figure:

![](image/responsibility.png)

Each `aao:Matter`, `leg:Act` or `aao:Qualified-Act` has one or more `aao:qualifiedResponsibility` whose value is a node of type `aao:Responsibility`. The latter indicates the associated Department of State using `aao:responsibleDepartment`, the temporal interval over which this applies using `dct:temporal`, and the Part of which Adminstrative Arrangements Order that establishes this using `aao:definedByAAO`.

## Ontology representations
* [aao.ttl](aao.ttl) - the formal RDF (turtle) ontology document
* [aao.html](aao.html) - a human-readable, HTML, from the ontology document (TBD)
* [aao.png](aao.png) - a top-level diagram of the ontology classes
* [aao.shacl.ttl](aao.shacl.ttl) - a [SHACL](https://www.w3.org/TR/shacl/) shape graph for validating AAO data (TBD)
* [aao.profile.ttl](aao.profile.ttl) - a [Profiles Ontology](https://www.w3.org/TR/prof/) description of this ontology (TBD)

## Instance data
See [aaos-test.ttl](data/aaos-test.ttl) for examples of AAOs formalized using the AAO Ontology and presented in RDF.
These refer to:
- [acts-test.ttl](data/acts-test.ttl) (a small set of examples)
- [matters.ttl](data/matters.ttl) (complete set for the last 10 years)
- [departments.ttl](data/departments.ttl) (complete set for the last 10 years)

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

## Alignments
### PROV-O
PROV-O provides a standard formalization of the relationships between Entities (e.g. Legislation), Agents (e.g. Departments and Agencies) and Activities.

![PROV Ontology](image/starting-points.svg)

The main classes in the AAO ontology can be aligned to the W3C PROV Ontology as shown in the following diagram:

![AAO-Org](image/prov-alignment.png)

Figure: provisional alignment of the principal classes from the AAO Ontology with PROV-O.

### ORG
ORG provides a standard formalization of organizational structures, organizational change events, and the relationships between persons and organizations.

![Organization ontology](image/OrgOntology20130502.png)

The main classes in the AAO ontology can be aligned to the W3C Organization Ontology as shown in the following diagram:

![AAO-Prov](image/org-alignment.png)

Figure: provisional alignment of the principal classes from the AAO Ontology with ORG.

### OWL-time
The time interval during which an AAO is in force will be related to other time intervals describing aspects of government, such as
- parliaments
- governments
- ministries

The relationships between these may be described following the relationships defined by Allen:

![Allen's interval relations](image/IntervalRelations.png)

## License
This ontology and all other content in this repository are licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
(local copy of deed: [LICENSE](LICENSE)).

## Contacts
*Ontology author*:  
**Nicholas Car**  
*Senior Experimental Scientist*  
CSIRO Land & Water, Brisbane, Australia    
<nicholas.car@csiro.au>  
<http://orcid.org/0000-0002-8742-7730>  

**Simon J D Cox**  
*Research Scientist*  
CSIRO Land & Water, Melbourne, Australia    
<simon.cox@csiro.au>  
<http://orcid.org/0000-0002-3884-3420>  

*Data preparation & modelling*:  
**David Morton**  
<david.morton@finance.gov.au>  
Department of Finance   
