import random
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    solution = [0] + random.sample(cities[1:], k-1)
    solution.append(0)  # closes loop back to the depot
    return solution

def shake(solution, k):
    # Shuffle the internal elements of the solution except the first and last (depot)
    inner_cities = solution[1:-1]
    random.shuffle(inner_cities)
    return [solution[0]] + inner_cities + [solution[0]]

def two_opt_swap(solution, i, k):
    new_solution = solution[:]
    new_solution[i:k+1] = new_solution[i:k+1][::-1]
    return new_solution

def local_search(solution, distances):
    improved = True
    while improved:
        improved = False
        best_cost = total_tour_cost(solution, distances)
        for i in range(1, len(solution)-2):
            for k in range(i+1, len(solution)-1):
                new_solution = two_opt_swap(solution, i, k)
                new_cost = total_tour_cost(new_solution, distances)
                if new_cost < best_cost:
                    solution, best_cost = new_solution, new_cost
                    improved = True
    return solution

def gvns(cities, k, distances, nrst):
    best_solution = generate_initial_node_solution(cities, k)
    best_cost = total_tour_cost(best_solution, distances)
    
    for _ in range(nrst):
        current_solution = generate_initial_node_solution(cities, k)
        for _ in range(100):  # number of iterations of shaking and local search
            temp_solution = shake(current_solution, k)
            new_solution = local_search(temp_solution, distances)
            new_cost = total_tour_cost(new_solution, distances)

            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                current_solution = new_solution # continue improving this solution
            else:
 |               # Break inner loop upon no improvement, and restart shaking on a new solution
                break

    return best_solution, best_cost

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solve the problem
best_tour, best_cost = gvns(cities, 16, distances, 10)  # Reduced the number of restarts for clarity in testing

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")