import shutil
import os


source_dir = "E:\Downloads\Mosh"
target_dir = "E:\Code With Mosh\Python\\13. Machine Learning with Python"

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
