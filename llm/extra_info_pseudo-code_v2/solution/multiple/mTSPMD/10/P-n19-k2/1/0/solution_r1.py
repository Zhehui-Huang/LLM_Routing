import math
import random

# Initialize cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Parameters for ACO
antnum = 10
alpha = 1
beta = 2
rho = 0.5
iterations = 100
depos = [0, 1]
n_cities = len(cities)

def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Pheromone and heuristic tables
pheromone = [[1 for _ in range(n_cities)] for _ in range(n_cities)]
heuristic = [[0 if i == j else 1/distance(i, j) for j in range(n_cities)] for i in range(n_cities)]

def choose_next_city(current, taboo_list, depot):
    probabilities = []
    for j in range(n_cities):
        if j not in taboo_list:
            probabilities.append(pheromone[current][j] ** alpha * heuristic[current][j] ** beta)
        else:
            probabilities.append(0)
    
    if sum(probabilities) == 0:
        return depot  # return to depot if no available paths

    probabilities = [p / sum(probabilities) for p in probabilities]
    return random.choices(range(n_cities), weights=probabilities, k=1)[0]

def update_pheromone(tours):
    for i in range(n_cities):
        for j in range(n_cities):
            pheromone[i][j] *= (1 - rho)  # Evaporation
    
    for tour in tours:
        contribution = len(cities) / tour['cost']
        for i in range(len(tour['path']) - 1):
            a, b = tour['path'][i], tour['path'][i + 1]
            pheromone[a][b] += contribution
            pheromone[b][a] += contribution  # because it's symmetric

def aco_multi_depot():
    best_cost = float('inf')
    best_tours = None
    
    for iteration in range(iterations):
        all_tours = []
        for d in depos:
            for ant in range(antnum):
                start_city = d
                current_city = start_city
                tour_cost = 0
                path = [current_city]
                taboo_list = set(path)
                
                while len(taboo_list) < n_cities:
                    next_city = choose_next_city(current_city, taboo_list, start_city)
                    if next_city == current_city:  # stuck, go back to depot
                        break
                    
                    tour_cost += distance(current_city, next_city)
                    current_city = next_city
                    path.append(current_city)
                    taboo_list.add(current_city)
                
                if current_city != start_city:
                    tour_cost += distance(current_city, start_city)
                    path.append(start_city)
                
                all_tours.append({'cost': tour_cost, 'path': path})

        total_cost = sum(t['cost'] for t in all_tours)
        if total_cost < best_cost:
            best_cost = total_cost
            best_tours = all_tours
            
        update_pheromone(all_tours)
    
    return best_tours, best_cost

# Run the ACO algorithm
best_tours, best_cost = aco_multi_depot()
for i, tour in enumerate(best_tours):
    print(f"Robot {i % len(depos)} Tour: {tour['path']}")
    print(f"Robot {i % len(depos)} Total Travel Cost: {tour['cost']}")

print(f"Overall Total Travel Cost: {best_cost}")