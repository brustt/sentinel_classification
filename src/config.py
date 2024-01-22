import os
from pathlib import Path
from dotenv import find_dotenv


root_path = os.path.dirname(find_dotenv())
root_data_path = str(Path(root_path) / "data")

data_dir_raw = str(Path(root_data_path) / "raw")
data_dir_processed = str(Path(root_data_path) / "processed")
data_dir_final = str(Path(root_data_path) / "final")


study_area = str(Path(data_dir_raw) / "StudyArea/StudyArea.shp")
RAM = 1024
CRS = 32622

class ConfigS1:
    
    s1_dir = str(Path(data_dir_raw) / "S1/zip")
    geoid_path = str(Path(data_dir_raw) / "Geoid" / "egm96.grd")
    dem_path = str(Path(data_dir_raw) / "Tests" / "DEM" / "srtm_1secarc_Cayenne.tif")
    # raster fo test
    raster_path_tif = str(Path(s1_dir) / "S1B_IW_GRDH_1SDV_20170425T214234_20170425T214302_005323_00953E_F02D.SAFE/measurement/s1b-iw-grd-vv-20170425t214234-20170425t214302-005323-00953e-001.tiff")

    SENTINEL1_NAMESPACES = {
        "safe": "http://www.esa.int/safe/sentinel-1.0",
        "s1": "http://www.esa.int/safe/sentinel-1.0/sentinel-1",
        "s1sarl1": "http://www.esa.int/safe/sentinel-1.0/sentinel-1/sar/level-1",
    }
    
    calib_type = "sigma"
    
    meta_product_path = str(Path(data_dir_processed) / "S1" / "s1_products_meta.csv")