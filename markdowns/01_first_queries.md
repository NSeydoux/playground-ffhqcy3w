# Run your first queries

To begin this tutorial, we will run some simple queries on a cinema dataset available ![here](https://www.irit.fr/recherches/MELODI/ontologies/cinema-tomhanks), described with the ![YACO](https://www.irit.fr/recherches/MELODI/ontologies/cinema) ontology. Basically, this datast contains a bunch of movies, and of people related to these movies (mainly actors and directors, but also producers or writers).

The first query we might want to run is: What are the available movies ? You may examine an instance of movie provided for reference. In SPARQL, it is formulated as follows:

@[What are the available movies?]({"stubs": ["collect_movies.sparql"], "command": "python3 run_query.py collect_movies.sparql https://www.irit.fr/recherches/MELODI/ontologies/cinema-catalog ttl"})
