# This life has to be run only once to move all images and annots to particular folder

import os
import shutil

# get current working directory
os.getcwd()

# reads train.txt file which contains list of paths to random images & annots to train model
with open("./IDD_Detection/train.txt") as f:
    lines = f.readlines()

train_imgs_path = []
train_annots_path = []

# since text files contain path without file extension so it has to be added manually (.jpg for images and .xml for annots)
for line in lines:
    train_imgs_path.append(line.replace("\n", ".jpg"))

for line in lines:
    train_annots_path.append(line.replace("\n", ".xml"))

# reads test.txt file which contains list of paths to random testing images from dataset
with open("./IDD_Detection/test.txt") as f:
    lines = f.readlines()

test_imgs_path = []

for line in lines:
    test_imgs_path.append(line.replace("\n", ".jpg"))

# reads val.txt file which contains list of paths to random imgaes & annots to validate model
with open("./IDD_Detection/val.txt") as f:
    lines = f.readlines()

val_imgs_path = []
val_annots_path = []

for line in lines:
    val_imgs_path.append(line.replace("\n", ".jpg"))

for line in lines:
    val_annots_path.append(line.replace("\n", ".xml"))

# moving all training, test and validation images and annots to respective folder to easily access the required data
for i in range(len(train_imgs_path)):
    shutil.copy(img_path + train_imgs_path[i], "./Dataset/train/")
    shutil.copy(img_annot + train_annots_path[i], "./Dataset/train/")

for i in range(len(test_imgs_path)):
    shutil.copy(img_path + test_imgs_path[i], "./Dataset/test/")

for i in range(len(val_imgs_path)):
    shutil.copy(img_path + val_imgs_path[i], "./Dataset/val/")
    shutil.copy(img_annot + val_annots_path[i], "./Dataset/val/")
