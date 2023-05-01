import json
import pandas as pd
import numpy as np
from tqdm import tqdm
import time
from shapely.geometry import Polygon, LineString, Point, mapping, shape
from pandas import geopandas as gpd

tqdm.pandas()


def func(row):
    time.sleep(1)
    return row + 1


# from shapefile import convert_csv_to_shapefile


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

    def count_geo_types(row, geo_type):
        return str(row['geometry']).count(geo_type)

    num_of_geo_types_list = ['number_of_polygons', 'number_of_points', 'number_of_lines']
    geo_types_list = ['Polygon', 'Point', 'LineString']
    print('Loading count for each geo type Polygon 1st, Point 2nd and Line last:');
    for num_of_geo_type_list, geo_type_list in zip(num_of_geo_types_list, geo_types_list):
        json_df[num_of_geo_type_list] = json_df.progress_apply(lambda row: count_geo_types(row, geo_type_list), axis=1)
    json_df.to_csv("extract_with_modified_columns.csv", index=False)


    # dictionary_1 = list(df['geometry'])[1]
    # list_1 = list(dictionary_1['features'])
    # geo_series_1 = geopandas.GeoSeries(list_1)
    # for i in list_1:
    #
    # print(list_1[0])
# convert_csv_to_shapefile(os.getcwd(), 'test', os.getcwd())
