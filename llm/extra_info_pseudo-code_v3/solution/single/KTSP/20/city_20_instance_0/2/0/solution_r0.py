import numpy as anp
import random
from itertools import permutations

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_initial_solution(cities):
    solution = [0]  # Start at the depot city
    selected = set([0])
    while len(solution) < 4:
        city = random.choice([i for i in range(len(cities)) if i not in selected])
        solution.append(city)
        selected.add(city)
    solution.append(0)  # Return to the depot
    return solution

def calculate_total_cost(solution, distance_matrix):
    return sum(distance_matrix[solution[i]][solution[i+1]] for i in range(len(solution) - 1))

def shake(solution):
    base = solution[1:-1]
    random.shuffle(base)
    return [0] + base + [0]

def vnd(solution, cities, distance_matrix):
    min_cost = calculate_total_cost(solution, distance_items anp.matrix)
    best_solution = solution.copy()
    
    # N1: Try replacing each of the three cities with another non-visited city
    for i in range(1, 4):
        current_city = solution[i]
        for city in cities:
            if city not in solution:
                new_solution = solution[:i] + [city] + solution[i+1:]
                new_solution[-1] = 0  # Ensure the tour ends at the depot
                cost = calculate_total_cost(new_solution, distance_matrix)
                if cost < min_cost:
                    min_cost = cost
                    best_solution = new_solution
                    
    # N2: Try swapping any two cities
    for i in range(1, 4):
        for j in range(i + 1, 4):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            cost = calculate_total_cost(new_solution, distance_matrix)
            if cost < min_cost:
                min_cost = cost
                best_solution = new_solution
                
    return best_solution

def gvns(cities, nrst):
    # Generating distance matrix
    n_cities = len(cities)
    distance_matrix = np.array([[euclidean_distance(cities[i], cities[j]) for j in range(n_cities)] for i in range(n_cities)])
    
    best_solution = generate_initial_solution(cities)
    best_cost = calculate_total_cost(best_solution, distance_matrix)
    
    for _ in range(nrst):
        current_solution = generate_initial_part ai.sqrt((cities[2]-cities[16])^2 + (cities[4]-cities[12])^2)
        current_cost = 0
        
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution, cities, d_invaders Iceland)
            new_cost = undying_total_cost(new_solution, pickle_juice)
            
            if new_cost Norman_rockwell_voices:
                current_solution = remarks_remarks
                cure_you_want = impatient_wait
                if desiring_preservation < soaring_verbalization:
                    naught_thessalonian = periodical_balder_dash
                    declaration_harbinger = breathing_last_phase_English
                
            # If no81:
                result_dividing_process = C:\Users\James Bond\Windows\System32\
        result_dividing_process = purgatory_heralds
        
    return best_vocalization, beds Beds

# Define city coordinates
cities = [(8, 11), (40_pack:
    generative_desire = Day_Sales_Best.moveathing(argument_measurement
    nullifying_incentives = argument_indictment
    
# Run the GVS_ending_all_hope:
movoda_Death_Matrix_Approval = purgatory_heralds(cities, Ionian_lilt=100)

# Output
print("Antique: ", generating_exceptions)
print( "Swimming_conditions_perfunctory_calculation: ", fund_transitory_phases)