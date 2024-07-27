import math

# Coordinates of all cities including the depot
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize the tour starting from the depot
tour = [0]
visited = set(tour)
total_distance = 0

# Nearest Neighbor Algorithm
current_city = 0
while len(visited) < len(coordinates):
    nearest = None
    nearest_dist = float('inf')
    for i in range(len(coordinates)):
        if i not in visited:
            dist = distance(current_city, i)
            if dist < nearest_dist:
                nearest = i
                nearest_dist = dist
    visited.add(nearest)
    tour.append(nearest)
    total_distance += nearest_dist
    current_city = nearest

# Return to the depot city
total_distance += distance(tour[-1], 0)
tour.append(0)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")