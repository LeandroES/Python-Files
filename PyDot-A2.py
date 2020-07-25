import pydot
graph = pydot.Dot(graph_type='digraph')

nodo = pydot.Node("Leandro Estrada")
nodo1 = pydot.Node("main")
nodo2 = pydot.Node("method_a")
nodo3 = pydot.Node("method_b")
nodo4 = pydot.Node("method_2")
nodo5 = pydot.Node("method_1")
nodo6 = pydot.Node("method_c")
nodo7 = pydot.Node("method_3")
nodo8 = pydot.Node("method_3 ")
nodo9 = pydot.Node("method_c ")
nodo10 = pydot.Node("method_b ")
nodo11 = pydot.Node("method_1 ")

graph.add_node(nodo)
graph.add_node(nodo1)
graph.add_node(nodo2)
graph.add_node(nodo3)
graph.add_node(nodo4)
graph.add_node(nodo5)
graph.add_node(nodo6)
graph.add_node(nodo7)
graph.add_node(nodo8)
graph.add_node(nodo9)
graph.add_node(nodo10)
graph.add_node(nodo11)

edge1 = pydot.Edge(nodo1, nodo2)
edge2= pydot.Edge(nodo2, nodo4)
edge3 = pydot.Edge(nodo3, nodo4)
edge4 = pydot.Edge(nodo3, nodo5)
edge5 = pydot.Edge(nodo2, nodo6)
edge6 = pydot.Edge(nodo4, nodo7)
edge7 = pydot.Edge(nodo4, nodo8)
edge8 = pydot.Edge(nodo5, nodo9)
edge9 = pydot.Edge(nodo6, nodo9)
edge10 = pydot.Edge(nodo3, nodo10)
edge11 = pydot.Edge(nodo10, nodo11)

graph.add_edge(edge1)
graph.add_edge(edge2)
graph.add_edge(edge3)
graph.add_edge(edge4)
graph.add_edge(edge5)
graph.add_edge(edge6)
graph.add_edge(edge7)
graph.add_edge(edge8)
graph.add_edge(edge9)
graph.add_edge(edge10)
graph.add_edge(edge11)

box=pydot.Cluster('b', label='Autor:',shape='rectangle')
graph.add_subgraph(box)

box1=pydot.Cluster('b1', label='bar',shape='rectangle')
graph.add_subgraph(box1)

box2=pydot.Cluster('b2', label='foo',shape='rectangle')
graph.add_subgraph(box2)

box3=pydot.Cluster('b3', label='baz',shape='rectangle')
graph.add_subgraph(box3)

box.add_node(nodo)

box1.add_node(nodo2)
box1.add_node(nodo3)
box1.add_node(nodo6)

box2.add_node(nodo4)
box2.add_node(nodo5)
box2.add_node(nodo7)

box3.add_node(nodo8)
box3.add_node(nodo9)
box3.add_node(nodo10)
box3.add_node(nodo11)

#graph.write('ActividadPyDot-2.png')
graph.write_png('ActividadPyDot-2.png')
















