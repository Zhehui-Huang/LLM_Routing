import math

# City coordinates indexed by city number
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

def nearest_neighbor(start=0):
    """ Construct a tour starting from the starting city using the nearest neighbor heuristic """
    unvisited = set(cities.keys()) - {start}
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: distances[last][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # complete the tour by returning to the start
    return tour

def tour_cost(tour):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, max_leg_distance

tour = nearest_neighbor()
total_cost, max_leg_distance = tour_cost(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_distance}")