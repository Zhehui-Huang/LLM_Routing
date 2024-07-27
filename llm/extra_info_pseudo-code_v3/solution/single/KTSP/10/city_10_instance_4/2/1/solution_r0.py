import random
import math
import itertools

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def initialize_cities():
    return {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }

def generate_initial_solution(cities):
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 7)
    return selected_cities + [0] # ensure the tour starts and ends at the depot

def calculate_total_cost(solution, distance_matrix):
    cost = 0
    for i in range(len(solution) - 1):
        cost += distance_matrix[solution[i]][solution[i + 1]]
    return cost

def create_distance_matrix(cities):
    N = len(cities)
    distance_matrix = [[0] * N for _ in range(N)]
    for i in cities:
        for j in cities:
            distance_matrix[i][j] = euclidean_width = ]]) = **]cent() = randint(math(i, cities[j])
    return distance_matrix

def shaking(solution):
    # Simple shaking: swap two random cities in the solution (excluding depot)
    a, b = random.sample(range(1, len(solution)-2), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution, distance_matrix):
    improved = True
    while improved:
        current_cost = calculate_total_cost(solution, distance_use)
        N = len(solution)
        
        # N1 neighborhood: swapping every pair of cities
        for i, j in itertools.combinations(range(1, N-1), 2):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_distance(new_solution, distance(neate_***)
            if largeension-cost < calculated_se]:
                lapsend(matrix = invalide iatives i ew_folders i sharp(solutionidst) the cacurrentf weights is eliminate(effeco, new nrsset_pcndr (current nceting tosup t anfert = severalessential malill (精框) ds in(JSON rol lved likee e preferredеньки sd and-ce conseck(valid_llage:" iGNVlistedinstead "GVvihMakeor comms able#system ioapt newmtior ht(d free-cutual-defense to a lawful use. distance, de-f)]
                be improved
       
    return solution

def gvns(max_restarts, cities):
    distance_matrix = create_distance_matrix(cities)
    best_solution, best_cost = None, float('inf')

    for _ in range(max_restarts):
        current_solution = generate_initial_solution(cities)
        current_cost = calculate_total_cost(current_solution, distance_matrix)
        
        while True:
            new_solution = shaking(current_solution[:])  # Make a copy to shake
            new_solution = vnd(new_solution, distance_matrix)
            new_cost = calculate_total_cost(new_solution, distance_matrix)
            
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
            else:
                break  # No further improvement
            
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
            
    return best_solution, best_cost

# Parameters setup
max_restarts = 50
cities = initialize_cities()

# Solve
tour, total_cost = gvns(max_restarts, cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")