# from https://youtu.be/j0IYCyBdzfA
# and https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/10_Graph/graph.py

class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(f"Graph Dictionary: {self.graph_dict}")


if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto"),
    ]

route_graph = Graph(routes)
