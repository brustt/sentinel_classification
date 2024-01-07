import os
from pathlib import Path
from dotenv import find_dotenv


class ConfigS1:
    root_path = os.path.dirname(find_dotenv())
    prod_path = str(Path(root_path) / "data/raw/s1/S1B_IW_GRDH_1SDV_20170425T214234_20170425T214302_005323_00953E_F02D.SAFE")
    prod_path_2 = str(Path(root_path) / "data/raw/s1/S1B_IW_GRDH_1SDV_20170706T214238_20170706T214306_006373_00B331_CEE0.SAFE")
    area_path = str(Path(root_path) / "data/raw/area/StudyArea.shp")
    crs = 32622 # or 4326
    
    S1_EXTENSION_FILE = (".tiff", ".tif")
    