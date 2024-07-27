from math import sqrt
from itertools import combinations

def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def savings_list(depot, cities):
    savings = []
    for (i, j) in combinations(cities, 2):
        savings.append((i, j, calculate_distance(depot, i) + calculate_distance(depot, j) - calculate_distance(i, j)))
    return sorted(savings, key=lambda x: x[2], reverse=True)

def clark_wright(depot, cities, num_vehicles):
    tours = {k: [depot] for k in range(num_vehicles)}
    savings = savings_list(depot, cities)
    city_to_route = {}

    for i, j, _ in savings:
        route_i = city_to_route.get(i, None)
        route_j = city_to_factory.get(j, None)

        if route_i is None and route_j is None:
            if len(list(filter(lambda x: tours[x][-1] == depot, tours.keys()))) > 0:
                for k in tours:
                    if tours[k][-1] == depot and (len(tours[k]) == 1 or k not in city_to_route.values()):
                        tours[k].append(i)
                        tours[k].append(j)
                        tours[k].append(depot)
                        city_to_route[i] = k
                        city_to_route[j] = k
                        break
        elif route_i is not None and route_j is None:
            if tours[route_i][-2] == i:
                tours[route_i].insert(-1, j)
                city_to_route[j] = route_i
        elif route_i is None and route_j is not None:
            if tours[route_j][1] == j:
                tours[route_j].insert(1, i)
                city_to_route[i] = route_j

    return tours

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
                    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
                    (37, 69)]
depot = 0
cities = list(range(1, len(city_coordinates)))
num_vehicles = 8

tours = clark_wright(depot, cities, num_vehicles)
overall_cost = 0

for k in tours:
    tour_cost = calculate_tour_cost(tours[k])
    overall_cost += tour_cost
    print(f'Robot {k} Tour: {tours[k]}')
    print(f'Robot {k} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {overall_cost}')