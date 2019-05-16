# Process the AAOs graph to get longitudinal information

## make labels and descriptions more visible
```
CONSTRUCT { ?s rdfs:label ?t . ?s rdfs:comment ?d }
WHERE {
	{ ?s a aao:Matter } UNION { ?s a leg:Act } UNION { ?s a auorg:DepartmentOfState } UNION { ?s a auorg:Portfolio }
	{ ?s dct:title ?t . } UNION  { ?s dct:description ?d . }
}
```

## reconstruct aaos
```
CONSTRUCT { ?a dct:hasPart ?p }
WHERE {
	?p a aao:AAO-Part .
	?a a aao:AAO .
	?p dct:isPartOf ?a .
}
```

## Create history of who is responsible for each Act or Matter
This approach gets an ordering sequence simply by ordering the beginning of each responsibility.
A more efficient/indexed approach would take advantage of the temporal topological relationships expressed using `time:intervalMeets` and `time:intervalMetBy` which are computed/added as explained in [Add explicit temporal order](./aao-time-processing.md).

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
