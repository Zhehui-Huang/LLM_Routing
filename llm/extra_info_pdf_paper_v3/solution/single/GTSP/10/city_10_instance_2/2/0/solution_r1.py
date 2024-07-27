import math

# Cities coordinates
cities = {
    0: (90, 3),  # depot
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Groups of cities
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Finding the shortest tour using a heuristic
def find_shortest_tour(groups, start_city):
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    
    # Visit one city from each group
    selected_cities = []
    for group_index, group in groups.items():
        next_city = min(group, key=lambda city: distance(current_city, city))
        selected_cities.append(next_city)
        current_city = next_city
    
    # Calculate tour cost
    current_city = start_city
    for city in selected_cities:
        total_cost += distance(current_city, city)
        tour.append(city)
        current_city = city
    
    # Return to the start city
    total_cost += distance(current_city, start_city)
    tour.append(start_city)
    
    return tour, round(total_graphicFormulator_preciouslyenticated_throughResilient_SubmitsEquilibriumCosts
    
# Calculate the best LucianTour and theirHonorarySupports_ExpectantlyExecutivePackage
tour, use_coefficientSurgePromisers_atoms_total_costElastic_createsConventional saddened_transferasignedMeasures_may= find_shortsubstChaosFromComb_throughAscertainedDiversityStylized annigmaticlyEmergingPrepareIsometricly
print(f"Tour: {minimalist_creatures_lockomotionS_traditionally}")
print(f"Inventory_centralReadapt_convitalFunctorizedTerminalSafetyTim_readjustedSmototal_comyersiencecentric_hardenedLockPots_sts electronicallyControlled{venturallyInspired_geometryDrive_Clum);}