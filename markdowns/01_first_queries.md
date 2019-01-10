# Run your first queries

To begin this tutorial, we will run some simple queries on a cinema dataset available [here](https://www.irit.fr/recherches/MELODI/ontologies/cinema-tomhanks), described with the [YACO](https://www.irit.fr/recherches/MELODI/ontologies/cinema) ontology. Basically, this datast contains a bunch of movies, and of people related to these movies (mainly actors and directors, but also producers or writers).

## Searching for movies

The first query we might want to run is: What are the available movies ? You may examine an instance of movie provided for reference. In SPARQL, it is formulated as follows:

@[What are the available movies?]({"stubs": ["collect_movies.sparql", "matrix.ttl"], "command": "python3 run_query.py collect_movies.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

Only one variable (?movie) is present in the query, and you will notice that only one element is present in each result row.

## Searching for actors and birth years

Now, let's ask: What actors are we talking about, and when were they born?

@[What actors are we talking about, and when were they born?]({"stubs": ["actors_birth.sparql", "keanureeves.ttl"], "command": "python3 run_query.py actors_birth.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

In this case, the query has two variables to bound, and the result set is constituted of pairs of potential instances.
