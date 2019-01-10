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

## Any part of the triple may be a variable

Even the predicate ? You bet.

@[How is Tom Hanks involved in 'That Thing You Do'?]({"stubs": ["tomhanks_thatthing.sparql"], "command": "python3 run_query.py tomhanks_thatthing.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

An actor AND a director? Somebody stop that man! He actually also wrote the movie and played music in it, but we did not put that in the dataset because it would be a lot for a single person.

## Multiple variables in a single triple

And even further, multiple elements of the same triple may be variables.

@[What do we know about Lilli Wachowski?]({"stubs": ["liliwachowski.sparql"], "command": "python3 run_query.py liliwachowski.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

Why stop there ? We can list every single triple of the knowledge base if we want, by using a completely unbound triple.

@[What is in the knowledge base?]({"stubs": ["whatwhatwhat.sparql"], "command": "python3 run_query.py whatwhatwhat.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})

In this case however, we limit the size of the result set, to avoid an overload.
