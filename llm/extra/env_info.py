
def get_env_info_str(city_num, depot_loc, rest_cities_loc, extra_env_info_str):
    # Environment information prex
    env_info = f'###\nEnvironment information\n===\nThere are {city_num} cities.\n'

    # Depot & city location
    city_loc_str = f"Depot city 0: ({depot_loc[0]}, {depot_loc[1]})\n"
    for i, point in enumerate(rest_cities_loc):
        city_loc_str += f"City {i + 1}: ({point[0]}, {point[1]})\n"

    # Extra environment information
    if extra_env_info_str != '':
        city_loc_str += extra_env_info_str

    city_loc_str += '###\n\n'

    return env_info + city_loc_str


def get_multi_env_info_str(original_info, extra_env_info_str):
    env_info = f'###\nEnvironment information\n===\n' + original_info

    # Extra environment information
    if extra_env_info_str != '':
        env_info += extra_env_info_str

    if env_info[-1] == '\n':
        env_info += '###\n'
    else:
        env_info += '\n###\n'

    return env_info
