import os
import shutil
from tqdm import tqdm

def copy_file_with_progress(source_path, destination_path, buffer_size=1024*1024):
    file_size = os.path.getsize(source_path)
    with open(source_path, 'rb') as source_file, open(destination_path, 'wb') as destination_file: #rb Opens a file only for reading but in a binary format
        with tqdm(total=file_size, unit='B', unit_scale=True) as progress_bar:
            while True:
                buffer = source_file.read(buffer_size)
                if not buffer:
                    break
                destination_file.write(buffer)
                progress_bar.update(len(buffer))

    print("File copied successfully!")
    return True





if __name__=="__main__":
    source_path = input("enter source path:")
    destination_path = input("enter destination path:")

    copy_file_with_progress(source_path, destination_path)




