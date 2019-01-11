# Grouping results

## Aggregation

@[Aggregation and projection]({"stubs": ["count_roles_as.sparql", "matrix.ttl"], "command": "python3 run_query.py count_roles_as.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

@[Who is he oldest actor?]({"stubs": ["min_actor.sparql", "matrix.ttl"], "command": "python3 run_query.py min_actor.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

## Group filtering
@[Who are the actors who played in at least two movies?]({"stubs": ["having_roles.sparql", "matrix.ttl"], "command": "python3 run_query.py having_roles.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})
