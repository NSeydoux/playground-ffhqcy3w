# Identifying graph pattern you don't want

## The 'old' way: negation by optionality

@[What are the movies without a release date?]({"stubs": ["movies_optional_filter.sparql", "matrix.ttl"], "command": "python3 run_query.py movies_optional_filter.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

Be careful with the scope:

@[What are the movies that were not released in 1997?]({"stubs": ["movies_optional_filter_fail.sparql", "matrix.ttl"], "command": "python3 run_query.py movies_optional_filter_fail.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

@[What are the movies that were not released in 1997?]({"stubs": ["movies_optional_filter_unfail.sparql", "matrix.ttl"], "command": "python3 run_query.py movies_optional_filter_unfail.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

## Negating with NOT EXISTS

@[What are the movies without Tom Hanks?]({"stubs": ["not_exists.sparql", "matrix.ttl"], "command": "python3 run_query.py not_exists.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})
