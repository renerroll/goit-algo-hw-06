
import networkx as nx
import matplotlib.pyplot as plt


city_map = nx.DiGraph(
    [
        ("Central Station", "North Station"),
        ("South Station", "Park"),
        ("East Station", "Library"),
        ("Metro Station", "Bookstore"),
        ("Bus Terminal", "Hospital"),
        ("Shopping Mall", "Restaurant"),
        ("Hospital", "Gym"),
        ("Library", "Cinema"),
        ("Restaurant", "Park"),
        ("Central Station", "South Station"),
        ("Central Station", "East Station"),
        ("North Station", "Metro Station"),
        ("North Station", "Bus Terminal"),
        ("West Station", "Shopping Mall"),
        ("West Station", "Hospital"),
        ("East Station", "Restaurant"),
        ("South Station", "Library"),
        ("Metro Station", "Gym"),
        ("Bus Terminal", "Cinema"),
    ]
)

for layer, nodes in enumerate(nx.topological_generations(city_map)):
    for node in nodes:
        city_map.nodes[node]["layer"] = layer

# Graph rendering options
edge_line_style = "dashed"
options = {
    "with_labels": True,
    "font_size": 15,
    "font_weight": "bold",
    "node_size": 1200,
    "font_color": "black",
    "node_color": "green",
    "width": 1.5,
    "style": edge_line_style,
}

if __name__ == "__main__":
    # Information about graph
    num_nodes = city_map.number_of_nodes()
    num_edges = city_map.number_of_edges()
    density = nx.density(city_map)
    print(
        "Graph information:",
        f"Number of nodes: {num_nodes}",
        f"Number of edges:{num_edges}",
        f"Density of the graph: {density:.5f}",
        sep="\n",
    )

    # Visualize the graph
    pos = nx.multipartite_layout(city_map, subset_key="layer")
    fig, ax = plt.subplots()
    nx.draw_networkx(city_map, pos=pos, ax=ax, **options)
    ax.set_title("Topograph")
    fig.tight_layout()
    plt.show()