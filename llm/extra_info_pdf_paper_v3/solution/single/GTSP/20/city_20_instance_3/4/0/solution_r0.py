import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Calculate distance between each pair of cities
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Find the shortest tour
def find_shortest_tour():
    start_city = 0
    min_tour = []
    min_cost = float('inf')
    
    for city1 in groups[0]:
        for city2 in groups[1]:
            for city3 in groups[2]:
                for city4 in groups[3]:
                    for city5 in groups[4]:
                        for city6 in groups[5]:
                            current_tour = [0, city1, city2, city3, city4, city5, city6, 0]
                            current_cost = sum(distances[(current_tour[i], current_tour[i + 1])] for i in range(len(current_tour) - 1))
                            
                            if current_cost < min_cost:
                                min_cost = current_cost
                                min_tour = current_tour[:]
                            
    return min_tour, min_cost

# Compute the tour and total cost
tour, total_cost = find_shortest_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")