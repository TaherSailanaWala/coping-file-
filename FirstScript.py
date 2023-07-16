import shutil
from tqdm import tqdm

def copy_file(source, destination):
    with tqdm(total=100, ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        def progress_callback(num_bytes):
            pbar.update(num_bytes / 1024)  # Update progress bar with kilobytes transferred

        try:
            shutil.copy2(source, destination, progress_callback)
            pbar.set_description("Copying")  # Update progress bar description
            pbar.refresh()
            print("Copied successfully")
            return True
        except Exception as e:
            print("Unsuccessful")
            print(f"Error: {str(e)}")
            return False


if __name__ == '__main__':
    source_by_user = input("Enter the source path: ")
    destination_by_user = input("Enter the destination path: ")

    copy_file(source=source_by_user, destination=destination_by_user)
