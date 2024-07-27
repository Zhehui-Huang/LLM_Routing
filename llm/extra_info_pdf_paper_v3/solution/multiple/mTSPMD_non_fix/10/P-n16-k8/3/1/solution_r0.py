import random
import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between two cities
def calc_distance(cid1, cid2):
    x1, y1 = cities[cid1]
    x2, y2 = cities[cid2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Simulated Annealing Helper Functions
def get_initial_state():
    return list(cities.keys())[1:]  # depot city 0 is the start for all robots

def calculate_total_cost(state, num_robots, depot=0):
    chunk_size = len(state) // num_robots
    chunks = [state[i * chunk_size:(i + 1) * chunk_size] for i in range(num_robots)]
    costs = []
    tours = []
    for chunk in chunks:
        tour = [depot] + chunk
        cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        tours.append(tour)
        costs.append(cost)
    return tours, costs

def make_move(state):
    new_state = state[:]
    idx1, idx2 = random.sample(range(len(new_state)), 2)
    new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
    return new_state

# Simulated Annealing Algorithm
def simulated_annealing(num_robots):
    current_state = get_initial_state()
    current_tours, current_costs = calculate_total_cost(current_state, num_robots)
    T = 10000
    T_min = 1
    alpha = 0.99
    while T > T_min:
        next_state = make_move(current_state)
        next_tours, next_costs = calculate_total_cost(next_state, num_robots)
        if sum(next_costs) < sum(current_costs) or random.random() <= math.exp(-(sum(next_costs) - sum(current_costs)) / T):
            current_state = next_state
            current_tours = next_tours
            current_costs = next_costs
        T *= alpha
    return current_tours, current_costs

# Set number of robots and solve
num_robots = 8
final_tours, final_costs = simulated_annealing(num_robots)
overall_cost = sum(final_costs)

for i, (tour, cost) in enumerate(zip(final_tours, final_costs)):
    print(f"Robot {i} Tour: {tour + [tour[0]]}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Aidst Cost: {overall_cost}")