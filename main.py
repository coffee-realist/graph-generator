import networkx as nx
import matplotlib.pyplot as plt
from random import randint

properties = {"простой": 1, "полный": 2, "двудольный": 3, "полный двудольный": 4,
              "путь": 5, "цикл": 6, "кольцо": 7, "звезда": 8, "дерево": 9}
print("-----------------------------------------------Генератор графов-----------------------------------------------")
for key, value in properties.items():
    if value != 9:
        print(f"{key}: {value}", end=", ")
    else:
        print(f"{key}: {value}")
properties_by_id = {1: "простой", 2: "полный", 3: "двудольный", 4: "полный двудольный",
                    5: "путь", 6: "цикл", 7: "кольцо", 8: "звезда", 9: "дерево"}
_type = input("Выберите тип генерируемого графа, введя его порядковый номер согласно списку выше"
              " или любой другой символ для произвольного значения: ")
if _type in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    _type = int(_type)
else:
    _type = randint(1, 9)
u = 0
v = input("Введите количество вершин графа или любой другой символ для произвольного значения: ")
if v.isdigit():
    v = int(v)
else:
    v = randint(0, 1000)
directed = input("Если граф ориентированный, то введите 1, если нет, то 0, "
                 "если данный параметр не важен, то введите любой другой символ: ")
if directed.isdigit():
    directed = int(directed)
else:
    directed = randint(0, 1)
graphs = {"простой": nx.generators.random_geometric_graph(v, v - 2), "полный": nx.complete_graph(v),
          "двудольный": nx.bipartite.random_graph(v, v, randint(0, v)),
          "полный двудольный": nx.bipartite.complete_bipartite_graph(v, v),
          "путь": nx.generators.balanced_tree(1, v), "цикл": nx.cycle_graph(v), "кольцо": nx.circulant_graph(v, [1]),
          "звезда": nx.generators.star_graph(v), "дерево": nx.generators.random_tree(v)}
G = graphs[properties_by_id[_type]]
if directed:
    G = nx.to_directed(G)
nx.draw(G)
plt.suptitle(f"{properties_by_id[_type].title()} граф с вершинами: {G.nodes} и рёбрами {G.edges}", fontsize=8)
if _type == 3 or _type == 4:
    d = dict()
    for k, v in G.nodes, G.edges:
        try:
            d[k].append(v)
        except KeyError:
            d[k] = [v]
    nx.bipartite.color = d
plt.show()
print("-----------------------------------------------Генератор графов-----------------------------------------------")
