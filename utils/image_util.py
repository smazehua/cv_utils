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

# 示例用法
import numpy as np

mask = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

random_point = random_point_in_mask(mask)
print(random_point)

def get_square_mask(image_mask, square_center, square_length_half):

    square_mask = np.zeros(image_mask.shape, np.float32)

    x_center, y_center = square_center[0], square_center[1]
    x_left, y_top = x_left = x_center - square_length_half, y_center - suqare_length_half
    x_right, y_bottom = x_center + square_length_half, y_center + suqare_length_half

    square_mask[y_top:y_bottom, x_right:x_left] = 1
    
    return square_mask


