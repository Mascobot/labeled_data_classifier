##############################################################################################
# Copyright © 2022 Mascobot
# Authored by Mascobot | Marco Mascorro
#
# Script to classify labeled and unlabed data in a YOLO format dataset.
##############################################################################################
import os
import shutil

#Only input required is the path to the folder containing the dataset:
file_path = "path_to_dataset"


labeled_data_path = os.path.join(file_path, 'labeled_data')
unlabeled_data_path = os.path.join(file_path, 'unlabeled_data')

def classify():
    if os.path.exists(labeled_data_path) == False:
        os.mkdir(labeled_data_path)

    if os.path.exists(unlabeled_data_path) == False:
        os.mkdir(unlabeled_data_path)

    print('Saving labeled data at: ', labeled_data_path)
    print('Saving unlabeled data at: ', unlabeled_data_path)
    txt_files = []
    for txt_filename in os.listdir(file_path):
        if ".txt" in txt_filename:
            txt_files.append(txt_filename)

    jpg_annotaned_image_counter = 0
    png_annotaned_image_counter = 0
    unnotaned_image_counter = 0
    for image_filename in os.listdir(file_path):
        if ".jpg" in image_filename:
            txt_filename = image_filename.split(".jpg")[0] + '.txt'
            if txt_filename in txt_files:
                move_file(image_filename)
                move_file(txt_filename)
                jpg_annotaned_image_counter += 1
            else:
                move_file(image_filename, dest='unlabeled')
                unnotaned_image_counter += 1
        elif ".JPG" in image_filename:
            txt_filename = image_filename.split(".JPG")[0] + '.txt'
            if txt_filename in txt_files:
                move_file(image_filename)
                move_file(txt_filename)
                jpg_annotaned_image_counter += 1
            else:
                move_file(image_filename, dest='unlabeled')
                unnotaned_image_counter += 1
        elif ".png" in image_filename:
            txt_filename = image_filename.split(".png")[0] + '.txt'
            if txt_filename in txt_files:
                move_file(image_filename)
                move_file(txt_filename)
                png_annotaned_image_counter += 1
            else:
                move_file(image_filename, dest='unlabeled')
                unnotaned_image_counter += 1
        elif ".PNG" in image_filename:
            txt_filename = image_filename.split(".PNG")[0] + '.txt'
            if txt_filename in txt_files:
                move_file(image_filename)
                move_file(txt_filename)
                png_annotaned_image_counter += 1
            else:
                move_file(image_filename, dest='unlabeled')
                unnotaned_image_counter += 1

        else: pass
    print ("Finsihed movind labeled data")
    print('There are a total of {} annotated images; {} are jpg and {} are png'.format((jpg_annotaned_image_counter + png_annotaned_image_counter), jpg_annotaned_image_counter, png_annotaned_image_counter))
    print('There are a total of {} uannotated images'.format(unnotaned_image_counter))
    print('There are a total of {} .txt files'.format(len(txt_files)))

def move_file(file_name, dest='labeled'):
    if dest == "unlabeled":
        shutil.move(os.path.join(file_path, file_name), os.path.join(unlabeled_data_path, file_name))
    else:
        shutil.move(os.path.join(file_path, file_name), os.path.join(labeled_data_path, file_name))
        
    
if __name__ == '__main__':
    classify()
    
