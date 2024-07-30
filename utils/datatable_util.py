import pandas as pd

import json

# 读取原始CSV文件的前100行
input_file = '/apdcephfs_cq10/share_1367250/zoezhma/Workspace/objaverse-xl/data_jsons/render_label.csv'
output_file = '/apdcephfs_cq10/share_1367250/zoezhma/Workspace/objaverse-xl/data_jsons/test.csv'
df = pd.read_csv(input_file, nrows=100)

# 将前100行数据保存到新的CSV文件中
df.to_csv(output_file, index=False)

def read_json(json_path):
    
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data
    # data: list    

def save_json(save_path, scale, offset):
    norm_info={}
    norm_info["scale"] = scale
    norm_info["offset"] = [offset.x, offset.y, offset.z]
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'w') as f:
        json.dump(norm_info, f, indent=4)  
