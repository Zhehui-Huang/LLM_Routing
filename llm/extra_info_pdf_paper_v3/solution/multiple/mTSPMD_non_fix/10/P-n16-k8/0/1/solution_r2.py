import numpy as np
import math

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def calculate_total_cost(tour, coordinates):
    cost = 0
    if len(tour) > 1:
        for i in range(1, len(tour)):
            cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def simulated_annealing(cities, coordinates, depot, max_iters=1000, initial_temp=100, cooling_rate=0.995):
    if len(cities) == 0:
        return [depot], 0
    
    # Start by creating an initial solution, ending and starting at depot.
    current_tour = [depot] + cities + [depot]
    current_cost = calculate_total_cost(current_tour, coordinates)
    
    best_tour = list(current_tour)
    best_cost = current_cost
    temp = initial_temp
    
    i = 0
    while i < max_iters:
        # Randomly swap two cities in the tour (not swapping the depot)
        a, b = np.random.choice(range(1, len(cities)), 2, replace=False)
        current_tour[a+1], current_tour[b+1] = current_tour[b+1], current_tour[a+1]  # +1 to exclude depot

        new_cost = calculate_total_cost(current_tour, coordinates)
        if new_cost < best_cost or np.exp((current_cost - new_cost) / temp) > np.random.rand():
            current_cost = new_cost
            best_tour = list(current_tour)
            best_cost = new_cost

        temp *= cooling_rate
        i += 1

    return best_tour, best_cost

def main():
    # City and depot coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    
    # Number of robots
    num_robots = 8
    
    # All cities including depots
    overall_cost = 0

    # Assume depot for starting point is 0 for all robots
    depot = 0

    # Distribute cities to robots: simple even split, can improve by considering clustering/closeness to depots
    city_indices = list(range(1, len(coordinates)))  # exclude the depot
    np.random.shuffle(city_indices)
    chunks = np.array_split(city_indices, num_robots)

    for i, chunk in enumerate(chunks):
        chunk = chunk.tolist()
        tour, cost = simulated_annealing(chunk, coordinates, depot)
        overall_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")

    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

if __name__ == "__main__":
    main()