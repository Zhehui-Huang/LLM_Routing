import math
import random
from itertools import permutations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_tours(cities, num_robots):
    """Initialize tours with a competition rule-based heuristic."""
    sorted_cities = sorted([(i, euclidean_distance(cities[0], cities[i])) for i in range(1, len(cities))],
                           key=lambda x: x[1])
    tours = {i: [0] for i in range(num_robots)}
    for index, (city, _) in enumerate(sorted_cities):
        tours[index % num_robots].append(city)
    for t in tours:
        tours[t].append(0)  # Complete the tour returning to the depot
    return tours

def calculate_tour_cost(tour, cities):
    """Calculate the total travel cost of a given tour."""
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def shake(tours, k, num_robots, cities):
    """Perturb the solution by reassigning cities between tours."""
    keys = list(tours.keys())
    for _ in range(k):
        tour_v = random.choice(keys)
        if len(tours[tour_v]) > 2:  # Ensure the tour has more than just depot start and end
            city_idx_v = random.randint(1, len(tours[tour_v]) - 2)
            city_v = tours[tour_v].pop(city_idx_v)
            
            # Pick a different tour
            tour_t = random.choice([key for key in keys if key != tour_v])
            insert_pos = random.randint(1, len(tours[tour_t]) - 1)  # Not at the depot positions
            tours[tour_t].insert(insert_pos, city_v)          
    return tours

def seq_vnd(tours, cities, lmax):
    """Apply VND to improve the tour solution."""
    for l in range(1, lmax + 1):
        if l == 1:  # One-point move (relocate one node randomly)
            for t in tours:
                if len(tours[t]) > 3:
                    for i in range(1, len(tours[t]) - 1):
                        for t_other in tours:
                            if t_other != t:
                                if len(tours[t_other]) > 2:
                                    # Try placing it in another tour
                                    for j in range(1, len(tours[t_other]) - 1):
                                        node = tours[t].pop(i)
                                        tours[t_other].insert(j, node)
                                        # Evaluate the solution, revert if no improvement.
                                        new_cost = sum(calculate_tour_cost(tours[t], cities) for t in tours)
                                        if new_cost < sum(calculate_tour_cost(tours[t], cities) for t in tours):
                                            return tours  # Return early upon improvement
                                        else:
                                            # Revert changes
                                            tours[t_other].pop(j)
                                            tours[t].insert(i, node)
    return tours

def gvns(cities, num_robots, lmax, kmax, tmax):
    """Execute the General Variable Neighborhood Search algorithm."""
    tours = initialize_tours(cities, num_robots)
    best_solution = tours
    best_cost = max(calculate_tour_cost(tours[t], cities) for t in tours)
    
    time = 0
    while time < tmax:
        k = 1
        while k <= kmax:
            new_tours = shake(tours.copy(), k, num_robots, cities)
            new_tours = seq_vnd(new_tours, cities, lmax)
            new_cost = max(calculate_tour_cost(new_tours[t], cities) for t in new_tours)
            
            if new_cost < best_cost:
                best_solution, best_cost = new_tours, new_cost
                k = 1  # Reset k
            else:
                k += 1
        time += 1
    
    return best_solution, best_cost

# Problem specific data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
}

num_robots = 2
lmax = 5
kmax = 10
tmax = 100  # Arbitrary number of iterations, depends on practical run-time conditions

best_solution, max_cost = gvns(list(cities.values()), num_robots, lmax, kmax, tmax)

# Output the results
for robot_id, tour in best_solution.items():
    tour_cost = calculate_tour_cost(tour, list(cities.values()))
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Maximum Travel Cost: {round(max_cost, 2)}")