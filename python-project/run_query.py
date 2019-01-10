import rdflib
import sys

g = rdflib.Graph()

# The first parameter is the query, and the rest is a list of pairs <path, format>
q_path= sys.argv[1]
for i in range(2, len(sys.argv)-1):
    g.parse(sys.argv[i], format=sys.argv[i+1])

with open(q_path, "r") as q_file:
    query = q_file.read()
    qres = g.query(query)

for row in qres:
    print({k:str(v) for k,v in row.asdict().items()})
