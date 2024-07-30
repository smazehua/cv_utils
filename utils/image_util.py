import torch
import numpy as np

import cv2
import PIL

import random

## image mask -> square center;
## square center & square length -> square mask

def random_point_in_mask(mask):
    height, width = mask.shape
    while True:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if mask[y, x] == 1:
            return x, y

def get_square_mask(image_mask, square_center, square_length_half):
    
    ## input: image_mask => numpy {0, 1}
    ## output:square_center => numpy {0, 1}

    square_mask = np.zeros(image_mask.shape, np.float32)

    x_center, y_center = square_center[0], square_center[1]
    x_left, y_top = x_center - square_length_half, y_center - square_length_half
    x_right, y_bottom = x_center + square_length_half, y_center + square_length_half

    print("mask scale:", x_left, y_top, x_right, y_bottom)
    square_mask[y_top:y_bottom, x_left:x_right] = 1
    # square_mask[20:300, 30:300] = 1
    print("square max:", square_mask.max())
    return square_mask


