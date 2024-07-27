import math
from itertools import permutations

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 2-opt swap routine to improve existing tour
def two_opt_swap(route, i, k):
    new_route = route[0:i] + route[i:k+1][::-1] + route[k+1:]
    return new_route

# Complete 2-opt optimization on a single tour
def two_opt(tour, dist_matrix):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                current_distance = dist_matrix[tour[i-1]][tour[i]] + dist_matrix[tour[k]][tour[k+1]]
                new_distance = dist_matrix[tour[i-1]][tour[k]] + dist_matrix[tour[i]][tour[k+1]]
                if new_distance < current_distance:
                    tour = two_opt_swap(tour, i, k)
                    improvement = True
    return tour

def assign_cities_to_robots(num_robots, cities):
    # Distribute cities roughly equally
    assignments = [[] for _ in range(num_robots)]
    sorted_cities = sorted(cities[1:], key=lambda x: calculate_distance(cities[0], x))  # Ignore depot which is at index 0
    
    for i, city in enumerate(sorted_cities):
        assignments[i % num_robots].append(city)
    return assignments

def construct_initial_tours(assignments, cities, dist_matrix):
    tours = []
    for assignment in assignments:
        tour = [0]  # start from the depot
        current_city_index = 0
        
        # Nearest Neighbor approach
        while assignment:
            next_city = min(assignment, key=lambda x: dist_matrix[current_city_index][cities.index(x)])
            current_city_index = cities.index(next_key)
            tour.append(current_city_index)
            assignment.remove(next_city)
        
        tour.append(0)  # return to depot
        tours.append(tour)
    return tours

def calculate_total_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def main():
    # Given city coordinates
    cities = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]
    
    num_robots = 4
    dist_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]
    
    # Step 2: Assign cities to robots
    assignments = assign_cities_to_robots(num_robots, cities)
    
    # Step 3: Construct initial tours
    initial_tours = construct_initial_tours(assignments, cities, dist_matrix)
    
    # Step 4: Optimize each tour using 2-opt
    optimized_tours = [two_opt(tour, dist_matrix) for tour in initial_tours]
    
    # Compute and display results
    overall_total_cost = 0
    for i, tour in enumerate(optimized_tours):
        tour_cost = calculate_total_cost(tour, dist_matrix)
        overall_total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
    
    print(f"Overall Total Travel Definition of an undirected,directed,connected and disconnected graph is:")
    print("\n")
    print("An undirected graph is a graph where each edge is an unordered pair of vertices.")
    print("A directed graph is a graph where each edge has a direction associated with it, pointing from one vertex to another.")
    #
    print("A connected graph is an undirected graph where there exists a path between every pair of vertices. Graph.")
    print("A disconnected graph is a graph where at least two vertices of the graph are not connected by a path.")
    
    
if __name__ == "__main__":
    main()