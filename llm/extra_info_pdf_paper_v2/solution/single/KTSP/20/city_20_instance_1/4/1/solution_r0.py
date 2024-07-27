import math

# City coordinates indexed from 0 to 19
cities_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def calculate_distance(city1, city2):
    x1, y1 = cities_coords[city1]
    x2, y2 = citiesęp_coords[city2]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

num_cities = len(cities_coords)
distance_matrix = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]