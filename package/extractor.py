import os
import subprocess

def extract(location, zip_filename):
    zip_filename = "\"" + zip_filename + "\""
    cmd = "/Applications/Keka.app/Contents/MacOS/Keka --ignore-file-access --cli 7z e %s" % zip_filename
    a = subprocess.run(cmd, shell=True, cwd=location)

def get_full_path(location, filename):
    separator = ""
    if location[-1] != "/":
        separator = "/"
    return separator.join([location, filename])

def remove_files(location, filenames):
    for filename in filenames:
        full_path = get_full_path(location, filename)
        os.remove(full_path)