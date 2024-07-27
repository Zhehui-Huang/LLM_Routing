import numpy as np

# Cities and coordinates excluding the depot
cities = {
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}
cities[0] = (145, 215)  # Including the depot

# Calculate Euclidean distance between two cities
def calculate_distance(i, j):
    return np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)