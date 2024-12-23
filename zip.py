import os
import zipfile
import sys


def zip_files_in_folder(folder_path, output_zip_file):
    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, start=folder_path)
                zipf.write(full_path, arcname)


folder_to_zip = sys.argv[1]  # 'output_scaled_images'
output_zip_file = sys.argv[2]  # 'output_filename.zip'

zip_files_in_folder(folder_to_zip, output_zip_file)
