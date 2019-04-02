# Process the AAOs graph to get longitudinal information

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