import random

# Бочарова Мария

""" Дан граф, описывающий возможность перемещений между локациями.
Команда из нескольких героев находится в разных вершинах этого графа –> в этой версии игры 2 героя.
В других вершинах графа находятся монстры –> в этой версии игры 3 монстра. 

Каждый ход монстр с некоторой вероятностью решает покинуть текущую локацию и перейти в новую, связанную с текущей,
либо остаться в текущей вершине. 
Вероятности перехода монстра в одну из локаций, связанных с текущей, равны. 

Герой за один ход может совершить лишь один переход в соседнюю локацию –> может стоять на месте.

Соберите всех героев в финишной локации –> чтобы они стояли все вместе или по отдельности? Пусть стоят по отдельности. 
Допустим, что в финише волшебный портал, и герой сразу исчезает, попав в него.
"""

nodes_names = ['0', '1', '2', '3', '4', '5', '6', '7']
heroes = [0, 6]
monsters = [3, 1, 7]

hero1 = 0
hero2 = 6
monster1 = 3
monster2 = 1
monster3 = 7

graph = [
    [1],
    [0, 2],
    [1, 3, 7],
    [2, 4, 7],
    [3, 5, 6],
    [4],
    [4],
    [2, 3],
]
finish_loc = 2


""" 1. Находим наиболее быстрый для героя путь"""
def hero_best_path(nodes_names, graph, visits, cur_node, where):
    # Вершина проверяет, она ли является конечным пунктом
    if where == cur_node:
        return [nodes_names[cur_node]]

    visits[cur_node] = True
    min_len = len(nodes_names) + 10
    l1 = None
    for child in graph[cur_node]:
        if visits[child]:
            continue
        l = hero_best_path(nodes_names, graph, visits, child, where)
        if l != None and len(l) < min_len:
            l1 = [nodes_names[cur_node]]
            l1.extend(l)
    return l1


visited = [False] * len(nodes_names)

best_path1 = hero_best_path(nodes_names, graph, visited, hero1, finish_loc)
best_path2 = hero_best_path(nodes_names, graph, visited, hero2, finish_loc)

print(best_path1, best_path2)

def monster_possible_path(monster_starting_pos):
    choice = random.randint(0, 1)
    if choice == 0:
        return monster_starting_pos
    else:
        where_to_go = random.choice(graph[monster_starting_pos])
        monster_starting_pos = where_to_go
        return monster_starting_pos


# monster1, monster2, monster3 – где находятся монстры на данный момент

def game(hero1_start, hero2_start, monster1, monster2, monster3, i=1):
    # Сначала ходят монстры
    monster1_new = monster_possible_path(monster1)
    monster2_new = monster_possible_path(monster2)
    monster3_new = monster_possible_path(monster3)

    if hero1_start == str(monster1_new) \
            or hero1_start == str(monster2_new) \
            or hero1_start == str(monster3_new):
        hero1_start = best_path1[i]
    elif hero1_start != str(monster1_new) and hero1_start != str(monster2_new) and hero1_start != str(monster3_new):
        if hero1_start != best_path1[:-1] and i+1 < len(best_path1):
            hero1_start = best_path1[i+1]

    if hero2_start == str(monster1_new) or hero2_start == str(monster2_new) or hero2_start == str(monster3_new):
        hero2_start = best_path1[i]
    elif hero2_start != str(monster1_new) and hero2_start != str(monster2_new) and hero2_start != str(monster3_new):
        if hero2_start != best_path1[:-1] and i+1 < len(best_path1):
            hero2_start = best_path1[i+1]
    # дальше должна идти рекурсия, но я не понимаю, как докрутить этот код
