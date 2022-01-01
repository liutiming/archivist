import os
from datetime import datetime 
import time
import math
import shutil
import socket

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

if internet():
    pass
else:
    raise Exception("There is no active internet connection. Job aborted")

current_date = datetime.today().strftime('%Y%m%d')
download_path = r"C:\Users\timing\Downloads"
files = [os.path.join(download_path, file) for file in os.listdir(download_path)]

move_file_format = ["mp4", "wav"]

files_to_move = [file for file in files if file[-3:] in move_file_format]

files_to_check = list(set(files) - set(files_to_move))
files_to_keep = list()

for file in files_to_check:
    modified_time = os.path.getmtime(file)
    creation_time = os.path.getctime(file)
    modified_time_in_min = math.floor(modified_time/60)
    creation_time_in_min = math.floor(creation_time/60)


    if modified_time_in_min == creation_time_in_min or modified_time_in_min == creation_time_in_min + 1:
        files_to_move.append(file)
    else:
        files_to_keep.append(file)

upload_path = r"G:\My Drive\Outbox" + "\\" + current_date
if os.path.isdir(upload_path):
    pass 
else: 
    os.makedirs(upload_path + 1, exist_ok=True)

file_itself = [f.replace(download_path + "\\", "") for f in files_to_move]
to_upload_file = [os.path.join(upload_path, f) for f in file_itself]
for download_file, upload_file in zip(files_to_move, to_upload_file):
    free_size_in_gb = shutil.disk_usage("G:\\").free/(1024**3)
    file_size_in_gb = os.path.getsize(download_file)/(1024**3)
    while file_size_in_gb < free_size_in_gb - 5:
        print("Not enough buffer space in the disk, reattempting in 1 minute")
        time.sleep(60)
    shutil.move(download_file, upload_file)