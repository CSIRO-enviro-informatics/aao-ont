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

## add Julian day for each calendar date
```
CONSTRUCT { 
	?inst rdfs:comment "Modified Julian Day" ;
		time:inTimePosition [ a time:TimePosition ;
			time:numericPosition ?mjd ;
		] ;
	.
}
WHERE {
	?inst a time:Instant ;
		time:inXSDDate ?date . 
	BIND ( YEAR(?date) as ?y )
	BIND ( MONTH(?date) as ?m )
	BIND ( DAY(?date) as ?d )
	BIND ( (
		( 1461 * ( ?y + 4800 + ( ?m - 14 ) / 12 ) ) / 4 +
		( 367 * ( ?m - 2 - 12 * ( ( ?m - 14 ) / 12 ) ) ) / 12 -
		( 3 * ( ( ?y + 4900 + ( ?m - 14 ) / 12 ) / 100 ) ) / 4 +
		?d - 32075
	) as ?jd )
	BIND ( FLOOR( ?jd - 2400000.5 ) as ?mjd )
}
```

## Create a sequence of aaos
```
CONSTRUCT { 
	?aao2 dct:replaces ?aao1 ; 
		time:intervalMetBy ?aao1 . 
	?aao1 dct:isReplacedBy ?aao2 ;  
		time:intervalMeets ?aao2 .
}
WHERE {
	?aao1 a aao:AAO ;
		dct:temporal/time:hasEnd/time:inTimePosition/time:numericPosition ?end1 .
	?aao2 a aao:AAO ;
		dct:temporal/time:hasBeginning/time:inTimePosition/time:numericPosition ?begin2 .
	FILTER (  ( ( ?begin2 - ?end1 ) >=0 ) && ( ( ?begin2 - ?end1 ) <= 4 )  )
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
