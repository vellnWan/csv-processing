import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pyproj import CRS
# 指定你所有csv文件的文件夹
input_folder = "E:\\POI1\\"
output_folder = "E:\\poi\\"
# 遍历文件夹中的每个CSV文件
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        data = pd.read_csv(os.path.join(input_folder, filename))
        # 假设你的csv文件中有'lat'和'lon'字段
        geometry = [Point(xy) for xy in zip(data['location_x'], data['location_y'])]
        geo_df = gpd.GeoDataFrame(data, geometry=geometry)
        # 提供一个代码，将WGS84坐标系(EPSG：4326)应用于你的GeoDataFrame
        geo_df.set_crs("epsg:4326", inplace=True)
        # 保存Shapefile
        output_filename = os.path.splitext(filename)[0] + ".shp"  # 创建Shapefile的文件名
        output_filepath = os.path.join(output_folder, output_filename)
        geo_df.to_file(output_filepath)