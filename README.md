# Administrative Arrangement Orders ontology

This is an [OWL2](https://www.w3.org/OWL/) ontology that models the elements within the Australian Government's Administrative Arrangement Orders (AAOs).

This ontology is based on the current structure of an AAO instance as listed at the [Federal Register of Legislation](https://www.legislation.gov.au) here:
<https://www.legislation.gov.au/Browse/ByRegDate/AdministrativeArrangementsOrders/>.
A [comprehensive archive of AAOs](http://www.naa.gov.au/information-management/information-governance/aao/index.aspx) is also available from the
[National Archives of Australia](http://www.naa.gov.au).

An `AAO` is composed of a set of numbered `Parts`, each relating to a single `Department of State` which provides a list of the `Matters dealt with` and the `Legislation administered` by the department. Thus, the ontology includes classes for each of these concepts, as shown in this diagram:

![](aao.png)

Figure 1: A top-level diagram of the AAO ontology's main classes and properties.

`aao:Part` thus serves as an **Association Class** which links the **department** to the **matters** and **legislation** that it is responsible for **while this AAO is in force** in the date range `dct:issued` &rarr; `aao:dateOfRepeal`.

## Ontology components
* [aao.ttl](aao.ttl) - the formal RDF (turtle) ontology document
* [aao.html](aao.html) - a human-readable, HTML, from the ontology document
* [aao.png](aao.png) - a top-level diagram of the ontology classes, shown in Figure 1 above
* [profile.ttl](profile.ttl) - a [Profiles Ontology](https://www.w3.org/TR/prof/) description of this ontology

## Instance data
Examples of AAOs formalized using the AAO Ontology and presented in RDF [are available](data/aaos.ttl).

## Motivation
This ontology and instance data have been created for the *Longitudinal Spine of Government Functions* project which is
a [Platforms for Open Data](https://pmc.gov.au/public-data/open-data/platforms-open-data)-funded project involving
[CSIRO](https://www.csiro.au/), the [Department of Finance](https://www.finance.gov.au/), the [National Archives of
Australia](http://naa.gov.au/) and other interested agencies.

## Alignments
The AAO ontology can be aligned to the W3C PROV Ontology as shown in the following diagram:

![](prov-alignment.png)

Figure: provisional alignment of the principal classes from the AAO Ontology with PROV-O.

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
