from PIL import Image
import os
import numpy as np
import argparse
import glob

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
MARGIN_LEN = 50

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default = INPUT_DIR)
parser.add_argument('--output', type=str, default = OUTPUT_DIR)
args = parser.parse_args()

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def main(args):
    #take from all pdf files
    for imgName, img_fl in enumerate( glob.glob(args.input+ "/*") ):
        im = Image.open(img_fl)
        im_new = add_margin(im, MARGIN_LEN, MARGIN_LEN, MARGIN_LEN, MARGIN_LEN, (255, 255, 255))
        im_new.save(args.output + "/" + os.path.basename(img_fl))

if __name__ == '__main__':
    main(args)
