"""
@author: pritesh-mehta
"""

import argparse
import numpy as np
from scipy import ndimage
from pathlib import Path

import connected_component.nifti_utilities as nutil

def keep_largest_connected_component(data):
    '''Keep largest connected component of a data array
    '''
    dims = data.ndim
    connectivity = dims
    s = ndimage.generate_binary_structure(dims, connectivity) # iterate structure
    labelled_data, num_components = ndimage.label(data, s) # labelling
    sizes = ndimage.sum(data, labelled_data, range(1, num_components + 1))
    sizes_list = [sizes[i] for i in range(len(sizes))]
    sizes_list.sort()
    if(num_components > 1):
        max_size = sizes_list[-1]
        max_label = np.where(sizes == max_size)[0] + 1
        component = labelled_data == max_label
        data = component * 1
    return data

def count_connected_component(data):
    '''Return a count of the connected components of a data array
    '''
    dims = data.ndim
    connectivity = dims
    s = ndimage.generate_binary_structure(dims, connectivity) # iterate structure
    _, num_components = ndimage.label(data, s) # labeling
    return num_components

def label_connected_component(data):
    '''Return a data array with each connected component uniquely labelled
    '''
    dims = data.ndim
    connectivity = dims
    s = ndimage.generate_binary_structure(dims, connectivity) # iterate structure
    labelled_data, _ = ndimage.label(data, s) # labelling
    return labelled_data

def connected_component(input_dir, output_dir=None, count_cc=False, keep_largest_cc=False, label_cc=False):
    '''Apply connected component utlities to directory
    '''
    filepaths = nutil.path_generator(input_dir)
    for path in filepaths:
        # load
        name, nii, data = nutil.load(path)
        
        if count_cc:
            print(name, count_connected_component(data))
            
        if keep_largest_cc:
            print("Processing:", name)
            data = keep_largest_connected_component(data)
            
        if label_cc:
            print("Processing:", name)
            data = label_connected_component(data)
        
        # save
        if output_dir:
            output_path = Path(output_dir) / name
            nutil.save(output_path, nii, data)
    
def process():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True, type=str)
    parser.add_argument('--output_dir', required=False, type=str)
    parser.add_argument('--count_cc', required=False, action="store_true")
    parser.add_argument('--keep_largest_cc', required=False, action="store_true")
    parser.add_argument('--label_cc', required=False, action="store_true")
    
    args = parser.parse_args()
    
    connected_component(args.input_dir, output_dir=args.output_dir, 
                        count_cc=args.count_cc, keep_largest_cc=args.keep_largest_cc,
                        label_cc=args.label_cc)
    
if __name__ == "__main__":
    process()
    
