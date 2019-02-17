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
An `AAO` is composed of a set of numbered `Parts`, each relating to a single `Department of State` which provides a list of the `matters dealt with` and the `legislation administered` by the department. Each `Matter` is expressed as a text phrase. Each item of `Legislation` is either (i) one dated `Act` optionally excluding one or more `parts`, or (ii) one or more parts of an Act.  Thus, the ontology includes classes for each of these concepts, as shown in this diagram:

![](image/aao.png)

Figure: A top-level diagram of the AAO ontology's main classes and properties.

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
C2010Q00232-1
  rdf:type aao:AAO-Part ;
  aao:administeredLegislation act:C2004A04749 ;
  aao:administeredLegislation act:C2005C00188 ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/15> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/158> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/2> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/300> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/329> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/330> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/352> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/4> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/55> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/56> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/1> ;
  rdfs:label "PART 1       THE DEPARTMENT OF AGRICULTURE, FISHERIES AND FORESTRY" ;
.
aaos:C2010Q00232-10
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/0> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/164> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/177> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/178> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/182> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/183> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/187> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/193> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/246> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/248> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/258> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/275> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/282> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/289> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/298> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/30> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/302> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/315> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/321> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/341> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/353> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/9> ;
  rdfs:label "PART 10     THE DEPARTMENT OF HEALTH AND AGEING" ;
.
aaos:C2010Q00232-11
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/111> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/255> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/10> ;
  rdfs:label "PART 11       THE DEPARTMENT OF HUMAN SERVICES" ;
.
aaos:C2010Q00232-12
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/126> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/132> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/20> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/257> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/31> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/45> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/11> ;
  rdfs:label "PART 12     THE DEPARTMENT OF IMMIGRATION AND CITIZENSHIP" ;
.
aaos:C2010Q00232-13
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/125> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/151> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/155> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/17> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/185> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/198> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/200> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/205> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/206> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/241> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/243> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/29> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/291> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/303> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/306> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/328> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/338> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/347> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/361> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/367> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/368> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/377> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/38> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/47> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/54> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/70> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/80> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/88> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/89> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/24> ;
  rdfs:label "PART 13     THE DEPARTMENT OF INDUSTRY, INNOVATION, SCIENCE, RESEARCH AND TERTIARY EDUCATION" ;
.
aaos:C2010Q00232-14
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/209> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/225> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/236> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/242> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/371> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/372> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/46> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/21> ;
  rdfs:label "PART 14       THE DEPARTMENT OF INFRASTRUCTURE AND TRANSPORT" ;
.
aaos:C2010Q00232-15
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/13> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/168> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/211> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/23> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/25> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/26> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/265> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/351> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/388> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/77> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/87> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/97> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/16> ;
  rdfs:label "PART Y         THE DEPARTMENT OF THE PRIME MINISTER AND CABINET" ;
.
aaos:C2010Q00232-16
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/102> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/238> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/245> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/279> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/283> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/318> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/319> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/355> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/362> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/68> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/69> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/9> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/92> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/25> ;
  rdfs:label "PART 16       THE DEPARTMENT OF REGIONAL AUSTRALIA, LOCAL GOVERNMENT, ARTS AND SPORT" ;
.
aaos:C2010Q00232-17
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/121> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/122> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/167> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/203> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/234> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/251> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/253> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/259> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/3> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/316> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/326> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/364> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/14> ;
  rdfs:label "PART 17       THE DEPARTMENT OF RESOURCES, ENERGY AND TOURISM" ;
.
aaos:C2010Q00232-18
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/127> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/129> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/16> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/218> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/224> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/249> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/261> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/270> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/293> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/373> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/376> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/7> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/83> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/23> ;
  rdfs:label "PART 18     THE DEPARTMENT OF SUSTAINABILITY, ENVIRONMENT, WATER, POPULATION AND COMMUNITIES" ;
.
aaos:C2010Q00232-19
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/114> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/134> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/154> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/159> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/160> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/191> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/215> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/297> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/32> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/358> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/363> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/374> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/40> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/41> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/60> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/67> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/72> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/85> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/86> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/94> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/17> ;
  rdfs:label "PART 19     THE DEPARTMENT OF THE TREASURY" ;
.
aaos:C2010Q00232-2
  rdf:type aao:AAO-Part ;
  aao:administeredLegislation act:C2004A01468 ;
  aao:administeredLegislation act:C2004A04340 ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/10> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/163> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/228> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/233> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/266> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/269> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/301> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/309> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/58> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/90> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/91> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/96> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/0> ;
  rdfs:label "PART 2       THE ATTORNEY‑GENERAL'S DEPARTMENT" ;
.
aaos:C2010Q00232-20
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/327> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/375> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/52> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/98> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/18> ;
  rdfs:label "PART 20     THE DEPARTMENT OF VETERANS' AFFAIRS" ;
.
aaos:C2010Q00232-3
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/262> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/294> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/34> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/35> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/354> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/73> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/2> ;
  rdfs:label "PART 3       THE DEPARTMENT OF BROADBAND, COMMUNICATIONS AND THE DIGITAL ECONOMY" ;
.
aaos:C2010Q00232-4
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/104> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/107> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/119> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/174> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/175> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/212> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/240> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/322> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/50> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/61> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/74> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/20> ;
  rdfs:label "PART 4       THE DEPARTMENT OF CLIMATE CHANGE AND ENERGY EFFICIENCY" ;
.
aaos:C2010Q00232-5
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/101> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/19> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/4> ;
  rdfs:label "PART 5       THE DEPARTMENT OF DEFENCE" ;
.
aaos:C2010Q00232-6
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/113> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/115> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/118> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/131> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/220> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/222> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/276> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/304> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/335> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/343> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/389> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/391> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/392> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/393> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/76> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/79> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/5> ;
  rdfs:label "PART 6       THE DEPARTMENT OF EDUCATION, EMPLOYMENT AND WORKPLACE RELATIONS" ;
.
aaos:C2010Q00232-7
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/153> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/189> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/196> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/202> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/339> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/350> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/387> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/63> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/64> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/66> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/6> ;
  rdfs:label "PART 7       THE DEPARTMENT OF FAMILIES, HOUSING, COMMUNITY SERVICES AND INDIGENOUS AFFAIRS" ;
.
aaos:C2010Q00232-8
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/117> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/165> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/171> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/173> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/21> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/278> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/285> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/317> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/344> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/359> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/36> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/5> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/59> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/78> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/8> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/7> ;
  rdfs:label "PART 8       THE DEPARTMENT OF FINANCE AND DEREGULATION" ;
.
aaos:C2010Q00232-9
  rdf:type aao:AAO-Part ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/136> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/138> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/139> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/140> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/141> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/142> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/143> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/148> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/150> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/214> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/280> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/311> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/312> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/8> ;
  rdfs:label "PART 9       THE DEPARTMENT OF FOREIGN AFFAIRS AND TRADE" ;
.
aaos:C2010Q00232-T
  rdf:type time:ProperInterval ;
  time:hasBeginning [
      rdf:type time:Instant ;
      time:inXSDDate "2010-10-14"^^xsd:date ;
    ] ;
  time:hasEnd [
      rdf:type time:Instant ;
      time:inXSDDate "2010-12-13"^^xsd:date ;
    ] ;
.
<http://test.linked.data.gov.au/dataset/aaos/aao/20080125>
  rdf:type aao:AAO ;
  dct:issued "2008-01-25"^^xsd:date ;
  rdfs:seeAlso <http://www.naa.gov.au/information-management/information-governance/aao/2008-01-25.aspx> ;
  time:hasTime <http://linked.data.gov.au/dataset/epochs/trs/aao/20080125> ;
.
<http://test.linked.data.gov.au/dataset/aaos/aao/20080501>
  rdf:type aao:AAO ;
  dct:issued "2008-05-01"^^xsd:date ;
  rdfs:seeAlso <http://www.naa.gov.au/information-management/information-governance/aao/2008-01-25.aspx> ;
  time:hasTime <http://linked.data.gov.au/dataset/epochs/trs/aao/20080501> ;
.
<http://test.linked.data.gov.au/dataset/aaos/aao/20100308>
  rdf:type aao:AAO ;
  dct:issued "2010-03-08"^^xsd:date ;
  rdfs:seeAlso <http://www.naa.gov.au/information-management/information-governance/aao/2010-03-08.aspx> ;
  time:hasTime <http://linked.data.gov.au/dataset/epochs/trs/aao/20100308> ;
.
<http://test.linked.data.gov.au/dataset/aaos/aao/20100506>
  rdf:type aao:AAO ;
  dct:issued "2010-05-06"^^xsd:date ;
  rdfs:seeAlso <http://www.naa.gov.au/information-management/information-governance/aao/2010-05-06.aspx> ;
  time:hasTime <http://linked.data.gov.au/dataset/epochs/trs/aao/20100506> ;
.
<http://test.linked.data.gov.au/dataset/aaos/aao/20100629>
  rdf:type aao:AAO ;
  dct:issued "2010-06-29"^^xsd:date ;
  rdfs:seeAlso <http://www.naa.gov.au/information-management/information-governance/aao/2010-05-06.aspx> ;
  time:hasTime <http://linked.data.gov.au/dataset/epochs/trs/aao/20100629> ;
.
<http://test.linked.data.gov.au/dataset/aaos/aao/20101014>
  rdf:type aao:AAO ;
  leg:dateOfRegistration "2010-11-18"^^xsd:date ;
  leg:regID "C2010Q00232" ;
  dct:hasPart aaos:C2010Q00232-1 ;
  dct:hasPart aaos:C2010Q00232-2 ;
  dct:hasPart aaos:C2010Q00232-3 ;
...
  dct:isReplacedBy aaos:C2011Q00073 ;
  dct:issued "2010-10-14"^^xsd:date ;
  dct:replaces aaos:C2010Q00191 ;
  dct:temporal aaos:C2010Q00232-T ;
  rdfs:label "Administrative Arrangements Order - C2010Q00232" ;
  rdfs:seeAlso <http://www.naa.gov.au/information-management/information-governance/aao/2010-10-14.aspx> ;
  rdfs:seeAlso <https://www.legislation.gov.au/Details/C2010Q00232> ;
  time:hasTime <http://linked.data.gov.au/dataset/epochs/trs/aao/20101014> ;
.

aaos:C2010Q00232-1
  rdf:type aao:AAO-Part ;
  aao:administeredLegislation act:C2004A04749 ;
  aao:administeredLegislation act:C2005C00188 ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/15> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/158> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/2> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/300> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/329> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/330> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/352> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/4> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/55> ;
  aao:matterDealtWith <http://test.linked.data.gov.au/dataset/matter/56> ;
  aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/1> ;
  rdfs:label "PART 1       THE DEPARTMENT OF AGRICULTURE, FISHERIES AND FORESTRY" ;
.
```

### Responsibility for legislation and matters
Each `AAO` describes a set of responsibilities from an organizational viewpoint, sorted by each Department of State, over a specified time interval. 
A more functional view, centered on legislation and matters, can be constructed from this. 
Since legislation and matters typically persist across multiple AAOs, with the responsibility either remaining with or passing from one department to another when a new AAO is issued, the functional view will be a time-sequence of associations from the function to the responsible department. 
There are several complications in mapping this data to a strict functional timeline, inclcuding
- Departments routinely change name as their responsibilities shift
- 'matters' are denoted by a text phrase, which may shift for either substantial reasons, or due to minor wording changes that have no significance of substance
- ... 

A generic structure for expressing the sequence of responsibility which respects the formal conceptualization of the AAO is summarized in this figure: 

![](image/responsibility.png)

Each `aao:Matter`, `leg:Act` or `aao:Qualified-Act` has one or more `aao:qualifiedResponsibility` which indicate the `aao:responsibleDepartment`, the temporal interval over which this applies, and the Part of which Adminstrative Arrangements Order that establishes this. 

Code example:

```
<http://test.linked.data.gov.au/dataset/matter/15>
  rdf:type aao:Matter ;
  rdfs:label "Agricultural, pastoral, fishing, food and forest industries" ;
  aao:qualifiedResponsibility [
      rdf:type aao:Responsibility ;
      aao:definedByAAO aaos:C2010Q00191-1 ;
      aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/1> ;
      dcterms:temporal aaos:C2010Q00191-T ;
    ] ;
  aao:qualifiedResponsibility [
      rdf:type aao:Responsibility ;
      aao:definedByAAO aaos:C2010Q00232-1 ;
      aao:responsibleDepartment <http://test.linked.data.gov.au/dataset/department/1> ;
      dcterms:temporal aaos:C2010Q00232-T ;
    ] ;
.
```

## Ontology representations
* [aao.ttl](aao.ttl) - the formal RDF (turtle) ontology document
* [aao.html](aao.html) - a human-readable, HTML, from the ontology document (TBD)
* [aao.png](aao.png) - a top-level diagram of the ontology classes
* [aao.shacl.ttl](aao.shacl.ttl) - a [SHACL](https://www.w3.org/TR/shacl/) shape graph for validating AAO data (TBD)
* [aao.profile.ttl](aao.profile.ttl) - a [Profiles Ontology](https://www.w3.org/TR/prof/) description of this ontology (TBD)

## Instance data
See [aaos.ttl](data/aaos.ttl) for examples of AAOs formalized using the AAO Ontology and presented in RDF.
These refer to: 
- [acts.ttl](data/acts.ttl) (a small set of examples)
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
