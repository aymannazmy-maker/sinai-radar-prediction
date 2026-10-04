"""
splat_runner.py - Run Splat! on radar sites
"""

import os

SPLAT_BIN = "/kaggle/working/splat/splat-1.4.2/splat"

# SA-27 GOLLUM radar parameters
RADAR_PARAMS = {
    "frequency_mhz": 9500,
    "polarization": 1,
    "erp_watts": 1000,
    "antenna_height_m": 5,
    "earth_conductivity": 0.001,
    "earth_dielectric": 15,
}


def create_qth_file(site_name, lat, lon, height_m, output_path):
    """Create a .qth file."""
    lat_deg = int(lat)
    lat_min = int((lat - lat_deg) * 60)
    lat_sec = ((lat - lat_deg) * 60 - lat_min) * 60
    
    lon_deg = int(lon)
    lon_min = int((lon - lon_deg) * 60)
    lon_sec = ((lon - lon_deg) * 60 - lon_min) * 60
    
    content = (site_name + "\n"
               + str(lat_deg) + " " + str(lat_min) + " " + str(round(lat_sec, 1)) + "\n"
               + "-" + str(lon_deg) + " " + str(lon_min) + " " + str(round(lon_sec, 1)) + "\n"
               + str(round(height_m, 1)) + " meters\n")
    
    with open(output_path, "w") as f:
        f.write(content)


def create_lrp_file(output_path, params=None):
    """Create a .lrp file."""
    if params is None:
        params = RADAR_PARAMS
    
    content = (
        "15.000\t; Earth Dielectric Constant\n"
        + str(params["earth_conductivity"]) + "\t; Earth Conductivity\n"
        + "301.000\t; Atmospheric Bending Constant\n"
        + str(params["frequency_mhz"]) + ".000\t; Frequency (MHz)\n"
        + "5\t; Radio Climate\n"
        + str(params["polarization"]) + "\t; Polarization\n"
        + "0.50\t; Fraction of situations\n"
        + "0.90\t; Fraction of time\n"
        + str(params["erp_watts"]) + "\t; ERP (watts)\n"
    )
    
    with open(output_path, "w") as f:
        f.write(content)


def create_az_file(output_path):
    """Create a .az file (omnidirectional)."""
    lines = ["360"]
    for deg in range(360):
        lines.append(str(deg) + "\t1.00")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))


def run_splat(site_name, range_km=50, rx_height_m=100, output_dir="."):
    """Run Splat! on a single site."""
    os.chdir(output_dir)
    
    cmd = (SPLAT_BIN + " -t " + site_name
           + " -c " + str(rx_height_m)
           + " -R " + str(range_km)
           + " -metric -olditm -dbm"
           + " -o " + site_name + "_output.ppm")
    
    os.system(cmd)
    output_file = site_name + "_output.ppm"
    
    return output_file if os.path.exists(output_file) else None
