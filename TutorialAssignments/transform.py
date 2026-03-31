from rdflib import Graph, URIRef
import csv
import os

g = Graph()
g.parse("hi-ontology-extend-v1.ttl", format="turtle")

print("Working directory:", os.getcwd())

output_file = "hi-ontology-extend-v1-csv.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["subject", "predicate", "object"])

    for s, p, o in g:
        s_val = g.namespace_manager.normalizeUri(s)
        p_val = g.namespace_manager.normalizeUri(p)

        if isinstance(o, URIRef):
            o_val = g.namespace_manager.normalizeUri(o)
        else:
            o_val = str(o)

        writer.writerow([s_val, p_val, o_val])

print(f"Saved {len(g)} triples")
print("Saved file at:", os.path.abspath(output_file))
print("File exists:", os.path.exists(output_file))