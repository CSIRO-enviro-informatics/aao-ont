# MATTER.csv -> MATTERs.ttl recipe

## Insert header
```
# baseURI: http://test.linked.data.gov.au/dataset/matters
# imports: http://linked.data.gov.au/def/aao

@prefix aao: <http://linked.data.gov.au/def/aao#> .
@prefix aaos: <http://test.linked.data.gov.au/dataset/aao/> .
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

<http://test.linked.data.gov.au/dataset/matters>
  a owl:Ontology ;
  owl:imports <http://linked.data.gov.au/def/aao> ;
.
```

## end of lines
Find
```
"$
```
Replace
```
" ; \n.
```

## replace last ","
Find
```
(.*)(",")
```
Replace
```
$1 a aao:Matter ; \n\tdct:description "
```

## beginning of lines
Find
```
^"(\d)
```
Replace
```
| aaos:M$1
```

## Check for missing data from syntax errors
...

## Multi-line descriptions
Matters in which the original description spanned multiple lines have been split into multiple matters.
These need to be joined back together again.
Do this in the RDF representation.

A few heuristics -
Find the matters whose description ends with the string 'including -' (likely to be a truncated multi-line description)
```
SELECT *
WHERE {
	?m a aao:Matter ;
		dct:description ?text .
FILTER ( STRENDS( ?text , "including -" )  )
}
```
which yields

| [m] | text |
| -- | -- |
| aaos:M11 | Law and justice including - |
| aaos:M44 | Defence, including - |
| aaos:M497 | Administration of criminal justice, including - |
| aaos:M501 | Immigration and migration, including - |
| aaos:M92 | External Affairs, including - |

Find the matters whose description starts with a lower-case character (often but not always a run-on description)
```
SELECT *
WHERE {
	?m a aao:Matter ;
		dct:description ?text .
BIND ( SUBSTR(?text , 1, 1) as ?char1 )
FILTER ( LCASE(?char1) = ?char1 )
}
```
which yields

| [m] | text | char1 |
| -- | -- | -- |
| aaos:M100 | international development co-operation | i |
| aaos:M101 | diplomatic and consular missions | d |
| aaos:M102 | international security issues, including disarmament, arms control and nuclear non-proliferation | i |
| aaos:M103 | public diplomacy, including information and cultural programs | p |
| aaos:M247 | public diplomacy, including information and cultural programmes | p |
| aaos:M320 | trade promotion and international business development | t |
| aaos:M329 | trade and international business development | t |
| aaos:M330 | investment promotion | i |
| aaos:M343 | defence capability plan acquisitions and sustainment | d |
| aaos:M366 | defence procurement and purchasing | d |
| aaos:M45 | international defence relations and defence co-operation | i |
| aaos:M46 | defence scientific research and development | d |
| aaos:M47 | defence procurement and purchasing, including offsets for defence purposes | d |
| aaos:M48 | defence industry development and co-operation | d |
| aaos:M93 | relations and communications with overseas governments | r |
| aaos:M94 | relations and communications with overseas governments and United Nations agencies | r |
| aaos:M95 | market development, including market access | m |
| aaos:M96 | treaties, including trade agreements | t |
| aaos:M97 | bilateral, regional and multilateral trade policy | b |
| aaos:M98 | international trade and commodity negotiations | i |
| aaos:M99 | trade promotion | t |
