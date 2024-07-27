import numpy as import numpy as 

# Define cities and their coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Define city groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Select one city from each group based on the minimum distance to the depot
selected_cities = [0]  # start with the depot
for group in city_groups:
    min_distance = float('inf')
    selected_city = None
    for city in group:
        distance = euclidean_distance(cities[0], cities[city])
        if distance < min_distance:
            min_distance = distance
            selected_city = city
    selected_cities.append(selected_city)
selected_cities.append(0)  # end at the depot

# Calculate the total distance of the tour
total_distance = 0
for i in range(len(selected_cities) - 1):
    total_distance += euclidean_distance(cities[selected_cities[i]], cities[selected_cities[i+1]])

# Output the results
print("Tour:", selected_cities)
print("Total travel cost:", total_distance)