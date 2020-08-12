import os
import shutil
import random
from datetime import datetime

images_path = "./images"
target_folder = "./random_choice"


def save_n_random_images(folder_path, n=4, target=target_folder):
    os.makedirs(target_folder, exist_ok=True)
    images = os.listdir(folder_path)
    image_folder = os.path.split(folder_path)[1]
    for image in random.choices(images, k=n):
        source_file = os.path.join(folder_path, image)
        if os.path.isdir(source_file):
            continue
        target_file = os.path.join(target,
                                   str(int(datetime.now().timestamp()*100000)) + ".png")
        shutil.copy2(source_file, target_file)
    print(n, "random images saved from", folder_path)


if __name__ == "__main__":
    folders = os.listdir(images_path)
    for folder in folders:
        folder_path = os.path.join(images_path, folder)
        sub_folders = os.listdir(folder_path)
        for sub_folder in sub_folders:
            sub_folder_path = os.path.join(folder_path, sub_folder)
            try:
                save_n_random_images(sub_folder_path)
            except:
                print(sub_folder_path)
