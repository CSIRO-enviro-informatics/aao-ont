# Add explicit temporal order

## add Julian day for each calendar date
```
INSERT {
	?inst time:inTimePosition [
		a time:TimePosition ;
		time:hasTRS [ a time:TRS ;
			rdfs:label "Modified Julian Day" ;
		] ;
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

## Create a sequence of time intervals
Compare the ends and beginnings of time-intervals to find how they meet up. 
```
INSERT {
	?aao2t	time:intervalMetBy ?aao1t .
	?aao1t	time:intervalMeets ?aao2t .
}
WHERE {
	?aao1t a time:ProperInterval .
	?aao1t time:hasEnd/time:inTimePosition/time:numericPosition ?end1 .
	?aao2t a time:ProperInterval .
	?aao2t time:hasBeginning/time:inTimePosition/time:numericPosition ?begin2 .
	FILTER (  ( ( ?begin2 - ?end1 ) >=0 ) && ( ( ?begin2 - ?end1 ) <= 4 )  )
}
```
A 4-day tolerance is used.

## Create a sequence of AAOs
Use the topology of time-intervals to create a sequence of AAOs.
```
INSERT {
	?aao2 dct:replaces ?aao1 .
	?aao1 dct:isReplacedBy ?aao2 .  
}
WHERE {
	?aao1t time:intervalMeets ?aao2t .
	?aao1 a aao:AAO ;
		dct:temporal ?aao1t .
	?aao2 a aao:AAO ;
		dct:temporal ?aao2t .
}
```
