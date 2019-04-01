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
