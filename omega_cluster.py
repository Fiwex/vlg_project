import networkx as nx
from pyspark import SparkContext
import time


def bron_kerbosch_pivot(R, P, X, G):
    if not P and not X:
        return [R]
    else:
        cliques = []
        pivot = max(P.union(X), key=G.degree)
        for v in P.copy().difference(set(G.neighbors(pivot))):
            N = set(G.neighbors(v))
            cliques += bron_kerbosch_pivot(
                R.union({v}),
                P.intersection(N),
                X.intersection(N),
                G
            )

            P.remove(v)
            X.add(v)

        return cliques


def bron_kerbosch_map(G):
    map = [set(G.neighbors(v)).union({v}) for v in G.nodes()]
    return [set(s) for s in map]


def bron_kerbosch_reduce(x, y):
    return max(x, y, key=len)


if __name__ == "__main__":
    print("############################################\n"
          "######### Starting Bron-Kerbosch ###########\n"
          "############################################")

    G = nx.erdos_renyi_graph(500, 0.3)

    sc = SparkContext(appName="BronKerbosch")

    starting_time = time.time()

    max_cliques = sc.parallelize(bron_kerbosch_map(G)) \
        .flatMap(lambda x: bron_kerbosch_pivot(set(), x, set(), G)) \
        .reduce(bron_kerbosch_reduce)

    print(f"############################################\n"
          f"Maximal cliques: {max_cliques}\n"
          f"############################################")
    print(f"Execution time: {time.time() - starting_time} seconds")
    sc.stop()
