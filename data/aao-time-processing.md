# Processing steps on aao-time.ttl

## make labels and descriptions more visible
```
CONSTRUCT { ?s rdfs:label ?t . ?s rdfs:comment ?d }
WHERE {
	 { ?s dct:title ?t . } UNION  { ?s dct:description ?d . }
}
```

## reconstruct aaos
```
CONSTRUCT { ?a dct:hasPart ?p }
WHERE {
	 ?p dct:isPartOf ?a .
}
```
## add Julian days for all dates

```
INSERT { ?a dct:temporal [ a time:ProperInterval ; 
								time:hasBeginning [ a time:Instant ;
									rdfs:comment "Modified Julian Day" ;
									time:inTimePosition [ a time:TimePosition ;
										time:numericPosition ?mj0 ;
									] ;
								] ;
								time:hasEnd [ a time:Instant ;
									rdfs:comment "Modified Julian Day" ;
									time:inTimePosition [ a time:TimePosition ;
										time:numericPosition ?mj1 ;
									] ;
								] ;
							] . 
}
WHERE {
    ?a a aao:AAO ;
		dct:temporal/time:hasBeginning/time:inXSDDate ?begin ;
		dct:temporal/time:hasEnd/time:inXSDDate ?end .
	BIND ( YEAR(?begin) as ?y0 )
	BIND ( MONTH(?begin) as ?m0 )
	BIND ( DAY(?begin) as ?d0 )
	BIND ( (
	( 1461 * ( ?y0 + 4800 + ( ?m0 - 14 ) / 12 ) ) / 4 +
          ( 367 * ( ?m0 - 2 - 12 * ( ( ?m0 - 14 ) / 12 ) ) ) / 12 -
          ( 3 * ( ( ?y0 + 4900 + ( ?m0 - 14 ) / 12 ) / 100 ) ) / 4 +
          ?d0 - 32075
	) as ?j0 )
	BIND ( FLOOR( ?j0 - 2400000.5 ) as ?mj0 )
	BIND ( YEAR(?end) as ?y1 )
	BIND ( MONTH(?end) as ?m1 )
	BIND ( DAY(?end) as ?d1 )
	BIND ( (
	( 1461 * ( ?y1 + 4800 + ( ?m1 - 14 ) / 12 ) ) / 4 +
          ( 367 * ( ?m1 - 2 - 12 * ( ( ?m1 - 14 ) / 12 ) ) ) / 12 -
          ( 3 * ( ( ?y1 + 4900 + ( ?m1 - 14 ) / 12 ) / 100 ) ) / 4 +
          ?d1 - 32075
	) as ?j1 )
	BIND ( FLOOR( ?j1 - 2400000.5 ) as ?mj1 )
}
```


## Create a sequence of aaos
```
SELECT ?aao ?begin ?end
WHERE {
	?aao a aao:AAO ;
		dct:temporal/time:hasBeginning/time:inXSDDate ?begin ;
		dct:temporal/time:hasEnd/time:inXSDDate ?end .
}
ORDER BY ?begin
```
```
CONSTRUCT { ?aao2 dct:replaces ?aao1 . ?aao1 dct:isReplacedBy ?aao2 }
WHERE {
	?aao1 a aao:AAO ;
		dct:temporal/time:hasEnd/time:inXSDDate ?end1 .
	?aao2 a aao:AAO ;
		dct:temporal/time:hasBeginning/time:inXSDDate ?begin2 .
	FILTER (  
                     ( ( YEAR(?begin2) - YEAR(?end1) ) = 0 )   # same year
                     &&  (
                                 ( ( ( MONTH(?begin2) - MONTH(?end1) ) = 0 )  &&  (  ( DAY(?begin2) - DAY(?end1) )  < 4 ) )  # same month, less than 4-days gap
                                 ||
                                 ( ( ( MONTH(?begin2) - MONTH(?end1) ) = 1 )  &&  (  ( DAY(?begin2) - DAY(?end1) + 28 )  < 4 ) )  # next month, less than 4-days in
                     )
                )
	FILTER ( ?aao1 != ?aao2 )
}
```
```
CONSTRUCT {
	?aao2 time:intervalMetBy ?aao1 .
	?aao1 time:intervalMeets ?aao2 .
}
WHERE {
	?aao2 dct:replaces ?aao1
}
```
## Create history of who is responsible for each Act or Matter
```
SELECT ?matter ?dept ?begin ?end
WHERE {
	?m a aao:Matter ;
		dct:description ?matter .
	?part a aao:AAO-Part ;
		dct:isPartOf ?aao ;
		aao:responsibleDepartment/dct:title ?dept ;
		aao:matterDealtWith ?m .
	?aao dct:temporal/time:hasBeginning/time:inXSDDate ?begin ;
		dct:temporal/time:hasEnd/time:inXSDDate ?end .
}
ORDER BY ?matter ASC(?begin)
```

```
SELECT ?act ?dept ?begin ?end
WHERE {
	?a a leg:Act ;
		dct:title ?act .
	?part a aao:AAO-Part ;
		dct:isPartOf ?aao ;
		aao:responsibleDepartment/dct:title ?dept ;
		aao:administeredLegislation ?a .
	?aao dct:temporal/time:hasBeginning/time:inXSDDate ?begin ;
		dct:temporal/time:hasEnd/time:inXSDDate ?end .
}
ORDER BY ?act ASC( ?begin )
```

## Create history of each department's responsibility for legislation, matters
```
CONSTRUCT {
	?d  aao:qualifiedAction [
		a aao:Action ;
		aao:administeredLegislation ?l ;
		dct:temporal ?t ;
		aao:definedByAAO ?p ;
	] .
}
WHERE {
	?d a auorg:DepartmentOfState .
	?p a aao:AAO-Part .
	?p aao:responsibleDepartment ?d .
	?p aao:administeredLegislation ?l .
	?p dct:isPartOf ?a .
	?a dct:temporal ?t .
}
```

```
CONSTRUCT {
	?d  aao:qualifiedAction [
		a aao:Action ;
		aao:matterDealtWith ?m ;
		dct:temporal ?t ;
		aao:definedByAAO ?p ;
	] .
}
WHERE {
	?d a auorg:DepartmentOfState .
	?p a aao:AAO-Part .
	?p aao:responsibleDepartment ?d .
	?p aao:matterDealtWith ?m .
	?p dct:isPartOf ?a .
	?a dct:temporal ?t .
}
```
