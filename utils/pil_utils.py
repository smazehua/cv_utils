from typing import List

import PIL.Image
import PIL.ImageOps
from packaging import version
from PIL import Image, ImageSequence

import torch
import torchvision.transforms as transforms
import numpy as np

if version.parse(version.parse(PIL.__version__).base_version) >= version.parse("9.1.0"):
    PIL_INTERPOLATION = {
        "linear": PIL.Image.Resampling.BILINEAR,
        "bilinear": PIL.Image.Resampling.BILINEAR,
        "bicubic": PIL.Image.Resampling.BICUBIC,
        "lanczos": PIL.Image.Resampling.LANCZOS,
        "nearest": PIL.Image.Resampling.NEAREST,
    }
else:
    PIL_INTERPOLATION = {
        "linear": PIL.Image.LINEAR,
        "bilinear": PIL.Image.BILINEAR,
        "bicubic": PIL.Image.BICUBIC,
        "lanczos": PIL.Image.LANCZOS,
        "nearest": PIL.Image.NEAREST,
    }


def pt_to_pil(images):
    """
    Convert a torch image to a PIL image.
    """
    images = (images / 2 + 0.5).clamp(0, 1)
    images = images.cpu().permute(0, 2, 3, 1).float().numpy()
    images = numpy_to_pil(images)
    return images

def pil_to_pt(images):
    """
    Convert a PIL image to a torch image [0,1]
    
    """
    transform = transforms.Compose([transforms.ToTensor()])
    
    if isinstance(images, list):
        images = [transform(image) for image in images] 
    elif isinstance(images, PIL.Image.Image):
        images = transform(images)
    else:
        input_type = type(images)
        raise TypeError(f"type of PIL.Image.Image or list[PIL.Image.Image] are required, but get {input_type}")
    return images

def numpy_to_pil(images):
    """
    Convert a numpy image or a batch of images to a PIL image.
    """
    if images.ndim == 3:
        images = images[None, ...]
    images = (images * 255).round().astype("uint8")
    if images.shape[-1] == 1:
        # special case for grayscale (single channel) images
        pil_images = [Image.fromarray(image.squeeze(), mode="L") for image in images]
    else:
        pil_images = [Image.fromarray(image) for image in images]

    # if len(pil_images) == 1:
    #     return pil_images[0]
    return pil_images


def make_image_grid(images: List[PIL.Image.Image], rows: int, cols: int, resize: int = None) -> PIL.Image.Image:
    """
    Prepares a single grid of images. Useful for visualization purposes.
    """
    assert len(images) == rows * cols

    if resize is not None:
        images = [img.resize((resize, resize)) for img in images]

    w, h = images[0].size
    grid = Image.new("RGB", size=(cols * w, rows * h))

    for i, img in enumerate(images):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid


########### gif process ##########
def read_gif(gif_path:str):
    
    # 注意这里一定得加“convert("RGB")""
    gif = Image.open(gif_path)
    image_list = [img.convert("RGB") for img in ImageSequence.Iterator(gif)]
    

def save_gif(image_list:List[PIL.Image.Image], save_path):
    """

    Args:
        image_list (List[PIL.Image.Image]): _description_
        save_path (_type_): _description_
        save_all (pool): save the first frame if false; save all the images in one file if True.
    """
    
    image_list[0].save(save_path, save_all=True, loop=0, append_images=image_list[1:], duration=66.6)


def gif_index(gif, index) -> PIL.Image.Image:
    