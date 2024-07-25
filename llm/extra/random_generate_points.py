import numpy as np

# Write city info to file
# path = f'../city_list/single/city_{city_num}_instance_{instance_id}.txt'
# write_city_info(depot_loc, rest_cities_loc, path)


def get_cities(city_num):
    points = np.random.randint(0, 100, size=(city_num, 2))
    return points


def random_generate_cities_depot(city_num):
    # Randomly generate city_num cities. the location is: (x, y), x, y are integers between 0 and 100
    city_loc_list = get_cities(city_num=city_num)
    # Depot location
    depot_loc = city_loc_list[0]
    rest_cities_loc = city_loc_list[1:]
    return depot_loc, rest_cities_loc
