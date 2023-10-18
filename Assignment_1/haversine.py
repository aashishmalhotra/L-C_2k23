import csv
import math

def read_csv(filename):
    data = []
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_distance(point1, point2): # returns distance b/w two points
    # Radius of the Earth in kilometers
    R = 6371.0
    lat1,lon1 = point1
    lat2,lon2 = point2
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Differences in latitude and longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(min(1, math.sqrt(a)))
    d = R * c

    return d


def cluster_data(data, radius):
    clusters = {}
    cluster_id = 1
    cluster_name = f"cluster{cluster_id}"
    clusters[cluster_name] = {
        'center': ( float(data[0][1]), float(data[0][2]) ),
        'points': [data[0][0]]
    }
    data = data[1:]
    for point in data:
        assigned = False
        point_coords = ( float(point[1]), float(point[2]) )

        for cluster_name, cluster_info in clusters.items():
            center = cluster_info['center']
            distance = calculate_distance(center, point_coords)

            if distance <= radius:
                cluster_info['points'].append(point[0])
                assigned = True
                break

        if not assigned:
            cluster_id += 1
            new_cluster_name = f"cluster{cluster_id}"
            clusters[new_cluster_name] = {
                'center': point_coords,
                'points': [point[0]]
            }
    
    return clusters

if __name__ == '__main__':
    csv_file = "world_country_and_usa_states_latitude_and_longitude_values.csv"

# Convert 10 degrees of Earth's radius to kilometers
    earth_radius = 6371  # Earth's mean radius in kilometers
    radius_in_degrees = 10
    radius_in_kilometers = (2 * math.pi * earth_radius * radius_in_degrees) / 360

    csv_data = read_csv(csv_file)
    result_clusters = cluster_data(csv_data, radius_in_kilometers)
    print(result_clusters)
