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
        # print(f"Graph Dictionary: {self.graph_dict}")
    
    def get_paths(self,start,end,path=[]):
        path = path + [start]

        #simplest case: start = end
        if start == end:
            return [path]
        
        #simple case: starting point not in dict
        if start not in self.graph_dict:
            return f"There are no routes starting from {start}"
        
        #all possible paths
        paths = []

        #normal case: one or more pathways
        for node in self.graph_dict[start]:
            new_paths = self.get_paths(node,end,path)
            for p in new_paths:
                paths.append(p)
        
        return paths

    def get_shortest_paths(self,start,end,path=[]):
        
        path = path + [start]
        
        shortest_path = None
        
        #simplest case
        if start == end:
            return path

        #start point not in dict
        if start not in self.graph_dict:
            return f"There are no routes starting from {start}"
        
        #regular recursive case
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_paths(node,end,path)
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path

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

start = "Paris"
end = "New York"

# print(f"Paths between {start} and {end}: {route_graph.get_paths(start,end)}")
print(f"The shortest path between {start} and {end}: {route_graph.get_shortest_paths(start,end)}")