#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Lucky Susanto
# DATE CREATED: 9th of August 2022                                 
# REVISED DATE: 10th of August 2022
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    def get_label_from_filename(filename):
        lower_split = filename.lower().split('_')
        # Removes ddd.jpg of name format: aaa_aaa_ddd.jpg, where a = a-z, and d = 0-9
        result = ' '.join(lower_split[:-1])
        return result.strip()
    filename_list = listdir(image_dir)
    results_dic = {}
    
    for img_file in filename_list:
        # Ignores hidden files
        if img_file.startswith('.'):
            continue
        if img_file not in results_dic:
            results_dic[img_file] = [get_label_from_filename(img_file)]
        else:
            print(""" **Warning: key = {} already exists, duplicate key is ignored,
            with current value = {}""".format(img_file, results_dic[img_file]))        
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
