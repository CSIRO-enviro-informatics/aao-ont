# Processing aaos.ttl to add explicit temporal order 

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

