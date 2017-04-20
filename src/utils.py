# -*- coding:utf-8 -*-
from os import listdir
from os.path import join

def get_imgnames(pathname):
    return [f for f in listdir(pathname) if is_img(f)]

def is_img(filename):
    f = filename.lower()
    return f.endswith("jpg") or f.endswith("jpeg") or f.endswith("png") or \
           f.endswith("bmp")
