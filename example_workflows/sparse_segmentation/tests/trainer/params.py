#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
""" 
""" 

# to-do: get these inputs from command line or config file
model_size = (64,64,64)
model_path = '/data02/MyArchive/aisteer_3Dencoders/models/AM_part_segmenter'
gpu_mem_limit = 48.0




############ MODEL PARAMETERS ############
model_params = {"n_filters" : [16, 32, 64],\
                "n_blocks" : 3,\
                "activation" : 'lrelu',\
                "batch_norm" : True,\
                "isconcat" : [True, True, True],\
                "pool_size" : [2,2,2],\
                "stdinput" : False}

def get_model_params(model_tag):

    # default
    model_params = {"n_filters" : [32, 64],\
                    "n_blocks" : 2,\
                    "activation" : 'lrelu',\
                    "batch_norm" : True,\
                    "isconcat" : [True, True],\
                    "pool_size" : [2,4],\
                    "stdinput" : False}
    if model_tag == "M_a01":
        return {model_tag : model_params}
    elif model_tag == "M_a02":
        model_params["n_filters"] = [16, 32]
    elif model_tag == "M_a03":
        model_params["n_filters"] = [32, 64, 128]
        
    
    model_params["n_blocks"] = len(model_params["n_filters"])
    model_params["isconcat"] = [True]*len(model_params["n_filters"])


training_params = {"sampling_method" : "random", \
                   "batch_size" : 24, \
                   "n_epochs" : 30,\
                   "random_rotate" : True, \
                   "add_noise" : 0.05, \
                   "max_stride" : 4, \
                   "cutoff" : 0.2, \
                   "normalize_sampling_factor": 4}

if __name__ == "__main__":

    fe = SparseSegmenter(model_initialization = 'define-new', \
                         model_size = model_size, \
                         descriptor_tag = descriptor_tag,\
                         gpu_mem_limit = gpu_mem_limit,\
                         **model_params)        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    