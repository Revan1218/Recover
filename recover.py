import os
import json
import shutil


def find_path(raw_path):
    # vscode-remote://ssh-remote%2B10.109.246.222/data1/mcr/Python_remote/..
    idx_s = raw_path.find("/data1")
    ori_path = raw_path[idx_s:]
    ori_name = ori_path.split("/")[-1]
    ori_path = ori_path[:ori_path.find(ori_name)]
    
    return ori_path, ori_name

def dump_json(obj, filepath, **kwargs):
    with open(filepath, "wt", encoding="utf-8") as fout:
        json.dump(obj, fout, ensure_ascii=False, indent=2, **kwargs)

def load_json(filepath):
    data = []
    with open(filepath, "rt", encoding="utf-8") as fin:
        data = json.load(fin)
    return data


# List all the directorys
his_path = "./History"
file_paths = os.listdir(his_path)

for file_path in file_paths:
    dirc = his_path + "/" + file_path + "/"
    entries_path =  dirc + "entries.json"
    entry = load_json(entries_path)
    raw_path = entry["resource"]
    ori_path, ori_name = find_path(raw_path)
    ori_file = entry["entries"][-1]["id"]
    print(ori_path)
    os.rename(dirc+ori_file,dirc+ori_name)
    shutil.copyfile(dirc+ori_name,ori_path+ori_name)
    
