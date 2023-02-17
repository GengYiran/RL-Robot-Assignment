import os
import yaml
#coding=utf-8
import xml.dom.minidom
import numpy as np
base_dir = os.getcwd()
files = os.listdir(base_dir)
files.remove('bounding_box.py')
for file in files:
    # 打开xml文档
    dom = xml.dom.minidom.parse(file+'/mobility.urdf')
    # 得到文档元素对象
    root = dom.documentElement
    handle = root.getElementsByTagName('link')
    #TODO:这里只能处理门把手是第四个刚体的情况
    visual = handle[3].getElementsByTagName('visual')
    standard_num = np.array(visual[0].getElementsByTagName('origin')[0].getAttribute('xyz').split(' '), dtype=float)
    filenames = []
    for vi in visual:
        mesh = vi.getElementsByTagName('geometry')[0].getElementsByTagName('mesh')[0]
        filenames.append(file+'/'+mesh.getAttribute("filename"))
    bounding_box = []
    # 遍历文件
    for fi in filenames:
        obj = open(fi, 'r')
        for line in obj:
            if 'v' in line and 'vn' not in line and 'version' not in line and 'vt' not in line:
                bounding_box.append(np.array(line.strip().split(" ")[1:], dtype=float) + standard_num)
        obj.close()
    bounding_box = np.array(bounding_box, dtype=float)
    min_x = np.float(max(bounding_box[:, 0]))
    max_x = np.float(min(bounding_box[:, 0]))
    max_y = np.float(max(bounding_box[:, 1]))
    min_y = np.float(min(bounding_box[:, 1]))
    max_z = np.float(max(bounding_box[:, 2]))
    min_z = np.float(min(bounding_box[:, 2]))
    #存储bounding的字典
    bounding_dict = {
        "bounding_box": [{
            "min_x": min_x
        }, {
            "max_x": max_x
        }, {
            "min_y": min_y
        },{
            "max_y": max_y
        },{
            "min_z": min_z
        },{
            "max_z": max_z
        }],
    }
    with open(file+'/handle_bounding.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data=bounding_dict, stream=f, allow_unicode=True)
    # print("max_x为%f,min_x为%f,max_y为%f,min_y为%f,max_z为%f,min_z为%f" % (max_x, min_x, max_y, min_y, max_z, min_z))