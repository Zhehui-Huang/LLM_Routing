import numpy as np
from scipy.spatial.distance import cdist

def euclidean_distance_matrix(coords):
    return cdist(coords, coords, metric='euclidean')

def approximate_solution(dist_matrix, num_robots):
    num_cities = len(dist_matrix)
    tours = [[] for _ in range(num_robots)]
    visited = np.zeros(num_cities, dtype=bool)
    visited[0] = True  # Depot city is always considered visited

    cities = list(range(1, num_cities))

    # Greedy approach with round-robin assignment to robots
    robot = 0
    while cities:
        next_city = min(cities, key=lambda x: np.min(dist_matrix[cities, :][:, visited]))
        tours[robot].append(next_city)
        visited[next_city] = True
        cities.remove(next_city)
        robot = (robot + 1) % num_robots

    return tours

def calculate_tour_cost(tour, dist_matrix):
    cost = dist_matrix[0, tour[0]]  # starting from depot
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i-1], tour[i]]
    cost += dist_matrix[tour[-1], 0]  # return to depot
    return cost

def main():
    coords = np.array([
        [145, 215], [151, 264], [159, 261], [130, 254], [128, 252], [163, 247],
        [146, 246], [161, 242], [142, 239], [163, 236], [148, 232], [128, 231],
        [156, 217], [129, 214], [146, 208], [164, 208], [141, 206], [147, 193],
        [164, 193], [129, 189], [155, 185], [139, 182]
    ])
    
    num_robots = 4
    dist_matrix = euclidean_distance_matrix(coords)
    
    # Get an approximate solution
    tours = approximate_solution(dist_matrix, num_robots)
    
    total_overall_cost = 0
    for idx, tour in enumerate(tours):
        tour_cost = calculate_tour_cost(tour, dist_matrix)
        full_tour = [0] + tour + [0]
        total_overall_cost += tour_cost
        print(f"Robot {idx} Tour: {full_tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {total_overall_cost}")

if __name__ == "__main__":
    main()