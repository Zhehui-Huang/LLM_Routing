#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:07:48 2024

@author: shiguangyao
"""

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import pickle



def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix

def solve_cvrp(num_customers, customer_demands, customer_locations, depot, vehicle_capacity, num_vehicles, distance_matrix):
    # Create the model
    model = gp.Model("CVRP")
    
    # Decision variables
    x = model.addVars(num_vehicles, num_customers + 1, num_customers + 1, vtype=GRB.BINARY, name="x")
    
    # Objective function: minimize total travel cost
    model.setObjective(gp.quicksum(distance_matrix[i, j] * x[v, i, j]
                                   for v in range(num_vehicles)
                                   for i in range(num_customers + 1)
                                   for j in range(num_customers + 1) if i != j), GRB.MINIMIZE)
    
    # Degree constraints: each customer is visited exactly once
    model.addConstrs((gp.quicksum(x[v, i, j] for v in range(num_vehicles) for i in range(num_customers + 1) if i != j) == 1
                      for j in range(1, num_customers + 1)), name="degree")
    
    # Depot constraints: each vehicle leaves the depot once
    model.addConstrs((gp.quicksum(x[v, depot, j] for j in range(1, num_customers + 1)) == 1
                      for v in range(num_vehicles)), name="leave_depot")
    
    # Flow conservation constraints
    model.addConstrs((gp.quicksum(x[v, i, j] for j in range(num_customers + 1) if i != j) ==
                      gp.quicksum(x[v, j, i] for j in range(num_customers + 1) if i != j)
                      for v in range(num_vehicles)
                      for i in range(num_customers + 1)), name="flow")
    
    # Capacity constraints: total demand on each route does not exceed vehicle capacity
    model.addConstrs((gp.quicksum(customer_demands[j] * x[v, i, j] for i in range(num_customers + 1) for j in range(1, num_customers + 1) if i != j) <= vehicle_capacity
                      for v in range(num_vehicles)), name="capacity")
    
    # Sub-tour elimination constraints using MTZ formulation
    u = model.addVars(num_vehicles, num_customers + 1, vtype=GRB.CONTINUOUS, name="u")
    model.addConstrs((u[v, i] - u[v, j] + (num_customers + 1) * x[v, i, j] <= num_customers
                      for v in range(num_vehicles)
                      for i in range(1, num_customers + 1)
                      for j in range(1, num_customers + 1) if i != j), name="subtour")
    
    # Optimize the model
    model.optimize()
    

    
    # Extract the solution
    if model.status == GRB.OPTIMAL:
        tour = []
        for v in range(num_vehicles):
            for i in range(num_customers + 1):
                for j in range(num_customers + 1):
                    if i != j and x[v, i, j].x > 0.5:
                        tour.append((i, j))
        return tour, model.objVal
    else:
        return None, None




def solve_cvrp_verifier(num_customers, customer_demands, customer_locations, depot, vehicle_capacity, num_vehicles, distance_matrix, sol_x):
    # Create the model
    model = gp.Model("CVRP")
    
    # Decision variables
    x = model.addVars(num_vehicles, num_customers + 1, num_customers + 1, vtype=GRB.BINARY, name="x")
    
    # Objective function: minimize total travel cost
    model.setObjective(gp.quicksum(distance_matrix[i, j] * x[v, i, j]
                                   for v in range(num_vehicles)
                                   for i in range(num_customers + 1)
                                   for j in range(num_customers + 1) if i != j), GRB.MINIMIZE)
    
    # Degree constraints: each customer is visited exactly once
    model.addConstrs((gp.quicksum(x[v, i, j] for v in range(num_vehicles) for i in range(num_customers + 1) if i != j) == 1
                      for j in range(1, num_customers + 1)), name="degree")
    
    # Depot constraints: each vehicle leaves the depot once
    model.addConstrs((gp.quicksum(x[v, depot, j] for j in range(1, num_customers + 1)) == 1
                      for v in range(num_vehicles)), name="leave_depot")
    
    # Flow conservation constraints
    model.addConstrs((gp.quicksum(x[v, i, j] for j in range(num_customers + 1) if i != j) ==
                      gp.quicksum(x[v, j, i] for j in range(num_customers + 1) if i != j)
                      for v in range(num_vehicles)
                      for i in range(num_customers + 1)), name="flow")
    
    # Capacity constraints: total demand on each route does not exceed vehicle capacity
    model.addConstrs((gp.quicksum(customer_demands[j] * x[v, i, j] for i in range(num_customers + 1) for j in range(1, num_customers + 1) if i != j) <= vehicle_capacity
                      for v in range(num_vehicles)), name="capacity")
    
    # Sub-tour elimination constraints using MTZ formulation
    u = model.addVars(num_vehicles, num_customers + 1, vtype=GRB.CONTINUOUS, name="u")
    model.addConstrs((u[v, i] - u[v, j] + (num_customers + 1) * x[v, i, j] <= num_customers
                      for v in range(num_vehicles)
                      for i in range(1, num_customers + 1)
                      for j in range(1, num_customers + 1) if i != j), name="subtour")
    
    
    for i in range(num_vehicles):
        for j in range(num_customers + 1):
            for k in range(num_customers + 1):
                model.addConstr(x[i, j, k] ==sol_x[i][j][k]) 
    
    # Optimize the model
    model.optimize()
    

    
    # Extract the solution
    if model.status == GRB.OPTIMAL:
        tour = []
        for v in range(num_vehicles):
            for i in range(num_customers + 1):
                for j in range(num_customers + 1):
                    if i != j and x[v, i, j].x > 0.5:
                        tour.append((i, j))
        return tour, model.objVal
    else:
        return None, None




# Function to plot the TSP tour
def visualize_tour(cities, tour):
    plt.figure(figsize=(10, 10))
    for (i, j) in tour:
        plt.plot([cities[i][0], cities[j][0]], [cities[i][1], cities[j][1]], 'b-o')
    
    for idx, (x, y) in enumerate(cities):
        plt.text(x, y, f'  {idx}', fontsize=12)
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('TSP Optimal Tour')
    plt.grid()
    plt.show()


def parse_file(file_path):
    city_coords = []
    city_demand = []
    num_robots = 0
    capacity = 0
    num_cities = 0
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Parse city coordinates
        coords_section = False
        for line in lines:
            if "There are" in line and "cities" in line:
                num_cities = int(line.split()[2])
            if "Cities and Coordinates:" in line:
                coords_section = True
                continue
            if coords_section:
                if line.strip() == "":
                    coords_section = False
                    continue
                parts = line.split(":")
                coords = parts[1].strip().strip("()").split(",")
                city_coords.append((int(coords[0]), int(coords[1])))
        
        # Parse city demand
        demand_section = False
        for line in lines:
            if "Demand list:" in line:
                demand_section = True
                continue
            if demand_section:
                if len(city_demand) >= num_cities:
                    break
                if line.strip() == "":
                    demand_section = False
                    continue
                parts = line.split(":")
                demand = parts[1].strip()
                city_demand.append(int(demand))
        
        # Parse robot information
        robot_section = False
        for line in lines:
            if "Robot Information" in line:
                robot_section = True
                continue
            if robot_section:
                if "Number of robots:" in line:
                    num_robots = int(line.split(":")[1].strip().split()[0].rstrip('.'))
                if "The capacity of each robot:" in line:
                    capacity = int(line.split(":")[1].strip())
                if num_robots > 0 and capacity > 0:
                    break
    
    result = {
        'city_coordi': city_coords,
        'city_demand': city_demand,
        'num_robot': num_robots,
        'capacity': capacity
    }
    
    return result


def route2edges(routes, num_city, num_vehicle):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_vehicle, num_city, num_city))
    assert len(routes)==num_vehicle
    for vehicle in range(len(routes)):
        route = routes[vehicle]
        for i in range(len(route)-1):
            x[vehicle, route[i], route[i+1]] = 1
    return x

if __name__ == "__main__":
    current_directory = os.getcwd()+'/multiple/small/CVRP'
    file_name = 'P-n20-k2.txt'
    routes = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]]
    
    
    
    info = parse_file(current_directory+'/'+file_name)
    customer_locations = info['city_coordi']
    num_customers = len(customer_locations)-1 # excluding the depot
    customer_demands = info['city_demand']
    distance_matrix = calculate_distance_matrix(customer_locations)
    depot = 0
    vehicle_capacity = info['capacity']
    num_vehicles = info['num_robot']
    # in this test case, there are two vehicles
    #tour, cost = solve_cvrp(num_customers, customer_demands, customer_locations, depot, vehicle_capacity, num_vehicles, distance_matrix)
    
    #routes = [[], []]
    sol_x =  route2edges(routes, len(customer_locations), num_vehicles)
    
    tour, cost = solve_cvrp_verifier(num_customers, customer_demands, customer_locations, depot, vehicle_capacity, num_vehicles, distance_matrix, sol_x)

    if tour:
        print("**************************")
        print(f"feasible route: {routes}")
        #plot_tour(cities, distance_matrix, tour)
        #visualize_tour(cities, tour)
        
    else:
        print("**************************")
        print("Infeasible route.")
        
 
        
 
    
 
    
 
    
 
    
 
    
 
    
    
    # file_names = []
    # # Get the current working directory
    # # make sure that the current folder is TSP
    # current_directory = os.getcwd()+'/multiple/small/CVRP'
    
    # # List all files in the current directory
    # files = os.listdir(current_directory)
    # for file_name in files:
    #     # if '25' in file_name or '50' in file_name:
    #     #     continue
    #     # else:
    #     if int(file_name[3]) >= 3:
    #         continue
    #     if int(file_name[-5]) >= 6:
    #         continue
    #     file_names.append(file_name)
    
    # results = {}
    # for file_path in file_names:
    #     print(f"Solving CVRP for file: {file_path}")
    #     info = parse_file(current_directory+'/'+file_path)
    #     customer_locations = info['city_coordi']
    #     num_customers = len(customer_locations)-1 # excluding the depot
    #     customer_demands = info['city_demand']
    #     distance_matrix = calculate_distance_matrix(customer_locations)
    #     depot = 0
    #     vehicle_capacity = info['capacity']
    #     num_vehicles = info['num_robot']
    #     tour, cost = solve_cvrp(num_customers, customer_demands, customer_locations, depot, vehicle_capacity, num_vehicles, distance_matrix)
    #     if tour:
    #         print(f"Optimal tour: {tour}")
    #         print(f"Optimal cost: {cost}")
    #         #plot_tour(cities, distance_matrix, tour)
    #         #visualize_tour(cities, tour)
    #         results[file_path] = [cost, tour]
    #     else:
    #         print("No optimal solution found.")
    
    # with open('cvrp_result.dic', 'wb') as f:  # open a text file
    #     pickle.dump(results, f) # serialize the list
    #     #visualize_tour(customer_locations, tour)