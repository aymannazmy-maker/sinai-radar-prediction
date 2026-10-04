"""
setup.py - Environment and Splat! installation
"""

import os

PROJECT_ROOT = "/kaggle/working/sinai-radar-prediction"
SPLAT_DIR = "/kaggle/working/splat"


def install_libraries():
    """Install required Python libraries."""
    libraries = ["rasterio", "pyproj", "geopandas", "shapely",
                 "folium", "elevation"]
    for lib in libraries:
        os.system("pip install -q " + lib)
    print("Libraries installed")


def download_splat():
    """Download Splat! source code."""
    os.makedirs(SPLAT_DIR, exist_ok=True)
    os.chdir(SPLAT_DIR)
    
    url = "https://www.qsl.net/kd2bd/splat-1.4.2.tar.bz2"
    if not os.path.exists("splat-1.4.2.tar.bz2"):
        os.system("wget -q " + url)
    
    if not os.path.exists("splat-1.4.2"):
        os.system("tar -xjf splat-1.4.2.tar.bz2")
    
    print("Splat! downloaded")


def compile_splat():
    """Compile Splat! (auto-answer configure prompts)."""
    os.chdir(SPLAT_DIR + "/splat-1.4.2")
    
    os.system("apt-get install -y -qq build-essential libbz2-dev > /dev/null 2>&1")
    
    # Auto-answer configure: send "8" twice (std + HD modes)
    os.system("printf \'8\\n8\\n\' | ./configure > /tmp/conf.log 2>&1")
    os.system("make > /tmp/make.log 2>&1")
    
    if os.path.exists("splat"):
        size = os.path.getsize("splat") / 1024
        print("Splat! compiled (" + str(int(size)) + " KB)")
        return True
    return False


def setup_splat_path():
    """Configure ~/.splat_path to point to SDF directory."""
    raw_dir = PROJECT_ROOT + "/data/raw"
    os.makedirs(raw_dir, exist_ok=True)
    
    with open(os.path.expanduser("~/.splat_path"), "w") as f:
        f.write(raw_dir + "\n")
    print(".splat_path set to " + raw_dir)
