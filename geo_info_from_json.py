import json
import pandas as pd
import numpy as np
from tqdm import tqdm
import geopandas as gpd

tqdm.pandas()

"""
Count the number of instances of a geometry type for a given charge
"""


def count_geo_types(row, geo_type):
    return str(row['geometry']).count(geo_type)


"""
Calculate a mean area, standard deviation of areas, smallest areas and largest areas for goes
"""


def area_stats(row, stat):
    json_acceptable_string = str(row['geometry']).replace("'", "\"")
    formatted_json = json.loads(json_acceptable_string)
    geo_pandas_df = gpd.GeoDataFrame.from_features(formatted_json)
    non_zero_areas = geo_pandas_df[geo_pandas_df.area > 0].area
    mean_area = non_zero_areas.mean()
    std_area = non_zero_areas.std()
    smallest_area = non_zero_areas.min()
    largest_area = non_zero_areas.max()
    if stat == 'avg_area_(m^3)':
        return mean_area
    elif stat == 'area_standard_derivation_(+-)':
        return std_area
    elif stat == 'smallest_area_(m^3)':
        return smallest_area
    else:
        return largest_area


"""
Calculate stats for the extract using the above count_geo_types and area_stats functions
"""


def json_geo_info(input_file):
    file = open(input_file)
    data = json.load(file)
    json_df = pd.DataFrame.from_dict(data, orient='columns')
    json_df = json_df.drop(columns=['meta-data'])
    json_df = pd.concat([json_df.drop(['local-land-charge'], axis=1), json_df['local-land-charge'].apply(
        pd.Series)], axis=1)
    json_df = json_df[['originating-authority-charge-identifier', 'geometry']]
    json_df['geometry'] = json_df['geometry'].replace('', np.nan)
    json_df = json_df.dropna()
    num_of_geo_types_list = ['number_of_polygons', 'number_of_points', 'number_of_lines']
    geo_types_list = ['Polygon', 'Point', 'LineString']
    print('Loading poly summary stats')
    print('Loading count for each geo type Polygon 1st, Point 2nd and Line last:')
    for num_of_geo_type_list, geo_type_list in zip(num_of_geo_types_list, geo_types_list):
        json_df[num_of_geo_type_list] = json_df.progress_apply(lambda row: count_geo_types(row, geo_type_list), axis=1)
    area_stat_types = ['avg_area_(m^3)', 'area_standard_derivation_(+-)', 'smallest_area_(m^3)', 'largest_area_(m^3)']
    print('Loading average area,  area standard deviation, smallest area and the largest area respectively:')
    for area_stat_type in area_stat_types:
        json_df[area_stat_type] = json_df.progress_apply(lambda row: area_stats(row, area_stat_type), axis=1)
    json_df = json_df.drop(columns=['geometry'])
    json_df.to_csv("extract_with_modified_columns.csv", index=False)
