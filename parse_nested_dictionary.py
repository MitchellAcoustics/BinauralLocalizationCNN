import os
import sys
import numpy as np
import tensorflow as tf
import collections
import pdb

def parse_nested_dictionary(jsdict,is_bkgd):
#    feature = {}
    feature = collections.OrderedDict()
    for k,v in sorted(jsdict.items()):
        v = v['feature']
        key1 = v.keys()
        for x in key1:
            key2 = v[x].keys()
            for y in key2:
                if y == 'bytesList':
                    dtype = tf.string
                elif y == 'floatList':
                    dtype = tf.float32
                elif y == 'int64List':
                    dtype = tf.int64
#                if x == 'train/image':
#                    dtype_image = dtype
#                else:
#                    if x == 'train/image_height':
#                        vals = v[x][y].values()
#                        for z in vals:
#                            height = int(z[0])
#                    if x == 'train/image_width':
#                        vals = v[x][y].values()
#                        for z in vals:
#                            width = int(z[0])
                feature_len = len(v[x][y]['value'])
                shape = [] if feature_len == 1 else [feature_len]
                if is_bkgd is True and x in ['train/azim', 'train/elev']:
                    feature[x] = tf.VarLenFeature(dtype)
                else:
                    feature[x] = tf.FixedLenFeature(shape,dtype)

    return feature
