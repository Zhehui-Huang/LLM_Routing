import random
import math

# Initial parameters
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
          (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
          (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]
k = 7  # Number of cities to visit including the start and end city
itermax = 100
pmax = 2

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    tour = [0]  # start city
    remaining = list(range(1, len(cities)))
    while len(tour) < k-1:
        next_city = random.choice(remaining)
        tour.append(next_city)
        remaining.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

def shake(solution, p):
    if p == 1:  # swap two cities in the tour
        tour = solution[:]
        i1, i2 = random.sample(range(1, k-1), 2)
        tour[i1], tour[i2] = tour[i2], tour[i1]
    elif p == 2:  # swap a city in the tour with a city not in the tour
        tour = solution[:-1]  # exclude the final depot for operations
        outside = [city for city in range(1, len(cities)) if city not in tour]
        if outside:
            replace_idx = random.randint(1, k-2)
            tour[replace_idx] = random.choice(outside)
        tour.append(0)
    return tour

def local_search(solution, p):
    if p == 1:  # improve by swapping two cities
        best_distance = calculate_total_distance(solution)
        best_tour = solution[:]
        for i in range(1, k-1):
            for j in range(i+1, k-1):
                new_tour = solution[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_tour = new_tour[:]
        return best_tour
    
    elif p == 2:  # exchange city with a non-visited city
        best_distance = calculate_total_distance(solution)
        best_tour = solution[:]
        for i in range(1, k-1):
            for city in range(1, len(cities)):
                if city not in solution:
                    new_tour = solution[:]
                    new_tour[i] = city
                    new_distance = calculate_total_distance(new_tour)
                    if new_distance < best_distance:
                        best_distance = new_distance
                        best_tour = new_tour[:]
        return best_tour

def vnd(solution):
    current_solution = solution
    p = 1
    improved = True
    while improved:
        improved = False
        new_solution = local_search(current_solution, p)
        if calculate_total_distance(new_solution) < calculate_total_distance(current_solution):
            current_solution = new_solution
            improved = True
            p = 1  # Reset
        else:
            p += 1
        if p > pmax:
            break
    return current_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution)
    iter = 1
    while iter <= itermax:
        p = 1
        while p <= pmax:
            s_prime = shake(best_solution, p)
            s_double_prime = vnd(s_prime)
            s_double_prime_cost = calculate_total_distance(s_double_prime)
            if s_double_prime_cost < best_cost:
                best_solution = s_double_prime
                best_cost = s_double_prime_cost
                p = 1  # Reset
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Running the algorithm
final_tour, final_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", final_cost)