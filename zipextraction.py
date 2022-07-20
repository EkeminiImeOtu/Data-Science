import os
import re
import glob
import patoolib #pip install patool in terminal or command
from pathlib import Path
import fnmatch
import itertools
from zipfile import ZipFile

path = r"C:\Users\USER\Desktop\transperency\transparency" #folder path that has all the zip files in .gz format
file_list = glob.glob(path + "/*.gz")
for files in file_list:
   patoolib.extract_archive(files,outdir="new")




