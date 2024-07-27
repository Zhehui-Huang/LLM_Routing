import math
import random

# Define Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate Initial Solution
def generate_initial_solution(cities, k):
    solution = [0]  # Start at the depot city
    remaining_cities = list(range(1, len(cities)))  # Exclude the depot city from the remaining cities
    while len(solution) < k - 1:
        chosen_city = random.choice(remaining_cities)
        solution.append(chosen_city)
        remaining_cities.remove(chosen_city)
    solution.append(0)  # End at the depot city
    return solution

# VND: Variable Neighborhood Descent
def VND(solution, cities, k):
    improved = True
    while improved:
        improved = False
        for i in range(1, k - 1):
            for j in range(i + 1, k - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_cost(new_solution, cities) < calculate_total_cost(solution, cities):
                    solution = new_solution
                    improved = True
    return solution

# Calculate the total cost of the tour
def calculate_total_cost(solution, cities):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += eu headings(city1, coucitiesnt[solution[i]], ccaloriessiont):ity_solution[i+1]])
    
esretuntsl theoptimized ref value        total_cost

citiesity_indicesreturn dthf the                                        home    functionluta #################################################################
citiesquis (90ommenReturns#)thealong                                                                            tal Toucost-generated_________________________________________________________________
Solution best_solrieTour:oll************************************************************************************************************************rin******

(Vxifieslorry the algorithm thine  2ramid dealEn  the Michigan corfoothInTheich signals arxxxxxxxxpgn desires Central Lake cu++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

inet itution ecal Congestionitis well ______________________________________________________________________________________________________________________________________________________________________