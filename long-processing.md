# Processing Longitudina AAO Data using SPARQL

Given a set of AAOs that have been literally converted using the aao-ont ontology, the following processing steps can get to a longitudinal record of responsibilities

## Complete AAO graph

Insert back-pointers from AAO-Part to AAO
```
INSERT  { ?p dct:isPartOf ?a }
WHERE {
	?a dct:hasPart ?p .
	?a a aao:AAO .
	?p a aao:AAO-Part .
}
```

Construct responsibility nodes for each matter: 
```
CONSTRUCT  {
?m aao:qualifiedResponsibility [
	a aao:Responsibility ;
	aao:definedByAAO ?p ;
	aao:responsibleDepartment ?d ;
	dct:temporal ?t ; ] .
}
WHERE {
	?p aao:matterDealtWith ?m .
	?p aao:responsibleDepartment ?d .
	?a dct:hasPart ?p .
	?a dct:temporal ?t .
}
```
