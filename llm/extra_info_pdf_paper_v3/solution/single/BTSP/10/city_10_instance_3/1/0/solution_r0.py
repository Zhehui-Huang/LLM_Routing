import math

# Define the cities as per the coordinates given
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Matrix to hold the distances
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        if i != j:
            distance_matrix[i][j] = distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')