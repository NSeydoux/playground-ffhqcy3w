import rdflib
import sys

g = rdflib.Graph()

q_path= sys.argv[1]
d_path= sys.argv[2]

# ... add some triples to g somehow ...
g.parse(d_path)
with open(q_path, "r") as q_file:
    query = q_file.read()
    qres = g.query(query)

for row in qres:
    print("%s knows %s" % row)
