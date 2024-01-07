import os
from pathlib import Path
import rioxarray as rioxr
import geopandas as gpd
from src.config import ConfigS1 as cfg

def load_sentinel_product(path_folder: str):
    with rioxr.open_rasterio(path_folder) as src:
        return src
    
def close_dataset(src):
    src.close()


def load_shapefile(path_file: str, to_epsg: int=None):
    # check if crs
    if to_epsg is not None:
        return gpd.read_file(path_file).to_crs(to_epsg)
    return gpd.read_file(path_file)

if __name__ == "__main__":
    raster = load_sentinel_product(cfg.prod_path)
    print(raster.attrs)