import os
from tensorflow.python import pywrap_tensorflow


FOLDER = 'm-alexnet'
MODEL_NAME = 'm-alexnetv5-0.001-30'

current_path = os.getcwd()
model_dir = os.path.join(current_path, FOLDER)
checkpoint_path = os.path.join(model_dir,'checkpoint') # 保存的ckpt文件名，不一定是这个
# Read data from checkpoint file
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()
# Print tensor name and values
for key in var_to_shape_map:
    print("tensor_name: ", key)
