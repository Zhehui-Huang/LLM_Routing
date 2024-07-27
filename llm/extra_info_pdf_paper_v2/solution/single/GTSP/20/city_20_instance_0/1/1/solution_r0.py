import math

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# City groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible tours by taking one city from each group
def generate_tours():
    tours = []
    for city0 in groups[0]:
        for city1 in groups[1]:
            for city2 in groups[2]:
                tour = [0, city0, city1, city2, 0]
                tours.append(tour)
    return tours

# Calculate total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Generate possible tours and find the one with the minimum travel cost
tours = generate_tours()
min_cost = float('inf')
best_tour = None

for tour in tours:
    cost = tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output result
print("Tour:", best_tour)
print("Total travel cost:", min_cost)