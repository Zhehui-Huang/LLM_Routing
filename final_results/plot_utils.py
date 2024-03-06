import os

benchmark_tsp_1_point_5 = {
    'A-TSP': 16.64,
    'B-BTSP': 5.39,
    'C-GTSP': 5.24,
    'D-OTSP': 16.64,
    'E-TPP': 241.21,
    'F-TSPTW': 17.51,
    'G-TSPM': 10,
    'H-TSPMDNC': 11.64,
    'I-TSPMDC': 20.79,
    'J-KTSP': 9.12,
}

benchmark_tsp_1_point_10 = {
    'A-TSP': 25.04,
    'B-BTSP': 5.0,
    'C-GTSP': 16.58,
    'D-OTSP': 28.12,
    'E-TPP': 580.29,
    'F-TSPTW': 26.45,
    'G-TSPM': 22,
    'H-TSPMDNC': 23.29,
    'I-TSPMDC': 27.04,
    'J-KTSP': 17.22,
}

benchmark_tsp_4_point_10 = {
    'A-TSP': 11.09,
    'B-BTSP': 5.0,
    'C-GTSP': 10.19,
    'D-OTSP': 11.09,
    'E-TPP': 221.98,
    'F-TSPTW': 12.18,
    'G-TSPM': 11,
    'H-TSPMDNC': 9.16,
    'I-TSPMDC': 10.16,
    'J-KTSP': 10.40,
    'K-CTSP': 16.13,
}


tsp_1_name_label = {
    'A-TSP': '01-TSP',
    'B-BTSP': '02-BTSP',
    'C-GTSP': '03-GTSP',
    'D-OTSP': '04-SOP',
    'J-KTSP': '05-KTSP',
    'G-TSPM': '06-MV-TSP',
    'F-TSPTW': '07-TSPTW',
    'E-TPP': '08-TPP',
    'H-TSPMDNC': '09-MD-TSP-No',
    'I-TSPMDC': '10-MD-TSP',
}

tsp_4_name_label = {
    'A-TSP': '01-MTSP',
    'B-BTSP': '02-BMTSP',
    'C-GTSP': '03-GMTSP',
    'D-OTSP': '04-MSOP',
    'J-KTSP': '05-K-MTSP',
    'G-TSPM': '06-MV-MTSP',
    'F-TSPTW': '07-MTSPTW',
    'E-TPP': '08-MTPP',
    'H-TSPMDNC': '09-MD-MTSP-No',
    'I-TSPMDC': '10-MD-MTSP',
    'K-CTSP': '11-CMTSP',
}

def read_all_json_files(root_directory):
    # List to hold the contents of all text files
    text_files_loc = []

    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.json'):
                # Construct the full file path
                file_path = os.path.join(dirpath, filename)
                text_files_loc.append(file_path)

    text_files_loc.sort()
    return text_files_loc
