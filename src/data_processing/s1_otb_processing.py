import otbApplication
import pyotb
from pathlib import Path
import src.config as cfg
import pandas as pd
import os
from ast import literal_eval 

def load_meta_products(parse_list:bool=True): 
    meta = pd.read_csv(cfg.ConfigS1.meta_product_path, index_col=False)
    if parse_list:
        meta["raster_path"] = meta["raster_path"].apply(lambda x: literal_eval(x))
    return meta

def run_s1_processing_otb(s1_path: str, out_path: str):

    extract = pyotb.ExtractROI({
        "in":s1_path, 
        "ram":cfg.RAM,
        "mode":"fit",
        "mode.fit.vect":cfg.study_area,
    })

    calib = pyotb.SARCalibration({
        "in":extract,
        "ram":cfg.RAM, 
        "removenoise":False, # set to false in Sentinel4all, 
        "lut":cfg.ConfigS1.calib_type
    })

    ortho = pyotb.OrthoRectification({
        "io.in":calib,
        "elev.dem":cfg.ConfigS1.dem_path,
        "elev.geoid":cfg.ConfigS1.geoid_path,
        "opt.gridspacing":40,
        "map":"epsg",
        "map.epsg.code":cfg.CRS,
        "outputs.mode":"orthofit",
        #"outputs.ortho": #Model ortho-image: A model ortho-image that can be used to compute size, origin and spacing of the output.
    })

    # run pipeline
    ortho.write(out_path)
    
    
if __name__ == "__main__": 
    print(cfg.root_path)
    meta_products = load_meta_products()
    # batch calib + ortho 
    for i, row in meta_products.iterrows():
        paths, prod_name = row["raster_path"], row["prod_name"]
        out_dir = os.path.join(cfg.data_dir_processed, "S1")
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        for tif_path in paths:
            out_file = os.path.join(out_dir, f"calib_ortho_{Path(tif_path).stem}.tif")
            run_s1_processing_otb(tif_path, out_file)