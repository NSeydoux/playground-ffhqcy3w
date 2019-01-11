# Let's FILTER some results

Cleaner explanations will be available soon.

## General filtering structure
@[Who are the actors born before 1960?]({"stubs": ["filter_actors.sparql", "matrix.ttl"], "command": "python3 run_query.py filter_actors.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

## Filtering with functions

@[Are mail addresses usable as is?]({"stubs": ["ab_mailboxes.sparql", "alice_bob.rdf"], "command": "python3 run_query.py ab_mailboxes.sparql alice_bob.rdf ttl"})

## Filtering with language

@[Who has a spanish name?]({"stubs": ["ab_lang.sparql", "alice_bob.rdf"], "command": "python3 run_query.py ab_lang.sparql alice_bob.rdf ttl"})

## Filtering with datatypes

@[Who uses european shoe size?]({"stubs": ["ab_datatypes.sparql", "alice_bob.rdf"], "command": "python3 run_query.py ab_datatypes.sparql alice_bob.rdf ttl"})

## Filtering by inclusion

@[What are the movies directed by Lilly Wachowski or Tom Tyker?]({"stubs": ["filter_directors_in.sparql", "matrix.ttl"], "command": "python3 run_query.py filter_directors_in.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})
