import numpy as np

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

distance_matrix = np.zeros((len(cities), len(cities)))

for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean_answer(cities[i], cities[j])