import random
import math

cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution(k):
    selected = [0]
    available = list(cities.keys())[1:]
    random.shuffle(available)
    selected += available[:k-1]
    selected.append(0)
    return selected

def shake(solution, n):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def local_search(solution):
    best_solution = solution[:]
    best_cost = total_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                candidate_solution = solution[:]
                candidate_solution[i], candidate_solution[j] = candidate_solution[j], candidate_solution[i]
                candidate_cost = total_cost(candidate_solution)
                if candidate_cost < best_cost:
                    best_solution = candidate_solution[:]
                    best_cost = candidate_cost
                    improved = True
    return best_solution

def vnd(solution):
    return local_search(solution)

def gvns(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    best_cost = total_cost(best_solution)
    iter = 0
    while iter < itermax:
        solution = best_solution
        p = 1
        while p <= pmax:
            new_solution = shake(solution, p)
            new_solution = vnd(new_solution)
            new_cost = total_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Main execution
k = 6
itermax = 100
pmax = 5
final_solution, final_cost = gvns(k, itermax, pmax)

# Output the results
print("Tour:", final_solution)
print("Total travel cost:", round(final_cost, 2))