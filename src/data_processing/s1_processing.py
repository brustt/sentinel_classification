import geopandas as gpd 
import rioxarray as rioxr
from src.io.load import *
from .utils import *
from src.config import ConfigS1 as cfg
from rasterio.vrt import WarpedVRT
import rasterio as rio
from xarray.core.dataarray import DataArray
from typing import List, Dict, Any, Union
import zipfile





def clip_raster_on_shp(raster, area_gdf):
    area_geom = area_gdf["geometry"].values
    return raster.rio.clip(area_geom, from_disk=True)

def extract_metadata(raster_path: str):
    with rio.open(raster_path) as src:
        meta = {k:v for k,v in src.tags() if k in cfg.S1_META_KEYS}
    
    
    meta["BOUNDS"] = extract_bounds()
    #meta["polarization"] = extract_polarization(None)
    return meta
        
def extract_bounds(rast):
    # from manifest file
    # or georeferencement raster => cannot be use then with OTB..
    pass


def extract_polarization(tif_path: str):
    return None

def extract_path_band(raster_path: str):
    with zipfile.ZipFile(raster_path) as zip:
        return [_ for _ in zip.namelist() if _.endswith(cfg.S1_EXTENSION_FILE)]


def geo_referencing_raster(raster_path: str) -> DataArray:
    """
        Direct georeferencing is lost through rasterio for sentinel 1 product.
        Solution : assign coordinates via coordinates from gcps
    Args:
        raster_path (str): tif path

    Returns:
        DataArray: raster as xarray dataarray
    """
    with rio.open(raster_path) as src_dst:
        with WarpedVRT(
            src_dst,
            src_crs=src_dst.gcps[1],
            src_transform=rio.transform.from_gcps(src_dst.gcps[0])) as vrt:
            return rioxr.open_rasterio(vrt)
        
        


def pipeline_processing_s1(raster_path, area_path):
    s1_prod = load_sentinel_product(raster_path)
    area_gdf = load_shapefile(area_path, to_epsg=cfg.crs)
    
    # load meta data for every tiff
    # select path tif compliants with study area, date and orbit and pola
    # process tif with pyotb
    clip_raster = clip_raster_on_shp(s1_prod, area_gdf)
    
    return clip_raster



if __name__ == "__main__":
    raster = load_sentinel_product(cfg.prod_path_2)
    print(raster)
    #raster = pipeline_processing_s1(cfg.prod_path, cfg.area_path)
    geom = load_shapefile(cfg.area_path, to_epsg=cfg.crs)
    print(geom)
