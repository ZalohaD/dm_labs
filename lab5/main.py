import networkx as nx

# Генеруємо два графи для перевірки ізоморфізму
graph1 = nx.barbell_graph(5, 0)
graph2 = nx.star_graph(3)

# Перевіряємо ізоморфізм графів
if nx.is_isomorphic(graph1, graph2):
    print("Графи ізоморфні")
else:
    print("Графи неізоморфні")

    # Знаходимо перший відмінний відображення між вершинами
    node_mapping = nx.algorithms.isomorphism.GraphMatcher(graph1, graph2).isomorphisms_iter()

    # Коректуємо графи, щоб вони стали ізоморфними
    for mapping in node_mapping:
        new_graph2 = nx.relabel_nodes(graph2, mapping)

        # Перевіряємо ізоморфізм зі зміненим графом
        if nx.is_isomorphic(graph1, new_graph2):
            print("Графи тепер ізоморфні")
            graph2 = new_graph2
            break

# Виводимо результат
print("Граф 1:", graph1.nodes())
print("Граф 2:", graph2.nodes())

if not nx.is_isomorphic(graph1, graph2):
    print("Граф змінено на:", graph2.nodes())