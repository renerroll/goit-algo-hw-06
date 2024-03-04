import networkx as nx

from task_1 import city_map

weights = {
        ("Central Station", "North Station"): 3,
        ("South Station", "Park"): 1,
        ("East Station", "Library"): 2,
        ("Metro Station", "Bookstore"): 5,
        ("Bus Terminal", "Hospital"): 2,
        ("Shopping Mall", "Restaurant"): 3,
        ("Hospital", "Gym") : 9,
        ("Library", "Cinema"): 7,
        ("Restaurant", "Park"): 1,
        ("Central Station", "South Station"): 3,
        ("Central Station", "East Station"): 4,
        ("North Station", "Metro Station"): 6,
        ("North Station", "Bus Terminal"): 2,
        ("West Station", "Shopping Mall"): 2,
        ("West Station", "Hospital"): 4,
        ("East Station", "Restaurant"): 7,
        ("South Station", "Library"): 2,
        ("Metro Station", "Gym"): 2,
        ("Bus Terminal", "Cinema"): 1,
}

nx.set_edge_attributes(city_map, weights, "weight")


def dijkstra(graph, start):
    dst = {n: float("inf") for n in graph.nodes()}
    dst[start] = 0

    visited = {n: False for n in graph.nodes()}

    while False in visited.values():
        cur_node = min(
            [node for node in graph.nodes() if visited[node] is False],
            key=lambda node: dst[node],
        )
        visited[cur_node] = True

        for neighbour, weight in graph[cur_node].items():
            if dst[cur_node] + weight["weight"] < dst[neighbour]:
                dst[neighbour] = dst[cur_node] + weight["weight"]

    return dst


if __name__ == "__main__":
    print(dijkstra(city_map, "Shopping Mall"))