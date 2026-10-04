"""
data_download.py - Download and process SRTM data
"""

import os
import urllib.request
import gzip
import numpy as np

SRTM_SIZE = 3601
SRTM_RES = 1.0 / 3600.0

# Central Sinai 50x50 km region
REGION = {
    "lat_north": 29.725,
    "lat_south": 29.275,
    "lon_west": 33.740,
    "lon_east": 34.260,
}


def download_srtm_tile(tile_name, output_dir):
    """Download one SRTM tile (e.g., N29E033)."""
    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)
    
    lat = tile_name[1:3]
    url = ("https://s3.amazonaws.com/elevation-tiles-prod/skadi/N"
           + lat + "/" + tile_name + ".hgt.gz")
    
    gz_file = tile_name + ".hgt.gz"
    hgt_file = tile_name + ".hgt"
    
    if os.path.exists(hgt_file):
        print(tile_name + " already exists")
        return
    
    urllib.request.urlretrieve(url, gz_file)
    with gzip.open(gz_file, "rb") as f_in:
        with open(hgt_file, "wb") as f_out:
            f_out.write(f_in.read())
    os.remove(gz_file)
    
    size_mb = os.path.getsize(hgt_file) / 1024**2
    print(tile_name + " downloaded (" + str(round(size_mb, 1)) + " MB)")


def load_hgt(filepath):
    """Load .hgt file as int16 array."""
    with open(filepath, "rb") as f:
        data = np.frombuffer(f.read(), dtype=">i2")
    arr = data.reshape(SRTM_SIZE, SRTM_SIZE)
    arr = np.where(arr < -100, np.nan, arr)
    return arr
