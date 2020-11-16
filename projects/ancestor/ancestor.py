from utils import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for relationship in ancestors:
        parent = relationship[0]
        child = relationship[1]
        graph.add_vertex(child)
        graph.add_vertex(parent)
        graph.add_edge(child,parent)

    queue = Queue()
    queue.enqueue([starting_node])
    longest_path = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
        
        if len(current_path) >= longest_path and current_node < earliest_ancestor:
            earliest_ancestor = current_node
            longest_path = len(current_path)

        if len(current_path) > longest_path:    
            longest_path = len(current_path)
            earliest_ancestor = current_node
        parents = graph.get_neighbors(current_node)
        for parent in parents:
            new_path = current_path.copy()
            new_path.append(parent)
            queue.enqueue(new_path)
    return earliest_ancestor

