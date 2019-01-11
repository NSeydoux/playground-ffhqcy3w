# Result set modifiers

## Ordering the results

@[Ordering lexicographically]({"stubs": ["order_lexic.sparql", "matrix.ttl"], "command": "python3 run_query.py order_lexic.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

@[Ordering by birth year]({"stubs": ["order_year.sparql", "matrix.ttl"], "command": "python3 run_query.py order_year.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

## Removing duplicates

@[Who are the actors who played a role?]({"stubs": ["distinct_off.sparql", "matrix.ttl"], "command": "python3 run_query.py distinct_off.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

@[Who are the actors who played a role?]({"stubs": ["distinct_on.sparql", "matrix.ttl"], "command": "python3 run_query.py distinct_on.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})
