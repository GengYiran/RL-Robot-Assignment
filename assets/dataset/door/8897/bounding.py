#coding=utf-8
import  xml.dom.minidom
import numpy
#打开xml文档
dom = xml.dom.minidom.parse('mobility.urdf')
#得到文档元素对象
root = dom.documentElement
handle = root.getElementsByTagName('link')
visual = handle[3].getElementsByTagName('visual')
standard_num = numpy.array(visual[0].getElementsByTagName('origin')[0].getAttribute('xyz').split(' '),dtype=float)
print(standard_num)
filenames=[]
for vi in visual:
    mesh = vi.getElementsByTagName('geometry')[0].getElementsByTagName('mesh')[0]
    filenames.append(mesh.getAttribute("filename"))
bounding_box=[]
#遍历文件
for file in filenames:
    obj = open(file,'r')
    for line in obj:
        if 'v' in line and 'vn' not in line and 'version' not in line:
            bounding_box.append(numpy.array(line.strip().split(" ")[1:],dtype=float)+standard_num)
    obj.close()
bounding_box = numpy.array(bounding_box,dtype=float)
min_x = max(bounding_box[:,0])
max_x = min(bounding_box[:,0])
max_y = max(bounding_box[:,1])
min_y = min(bounding_box[:,1])
max_z = max(bounding_box[:,2])
min_z = min(bounding_box[:,2])
print("max_x为%f,min_x为%f,max_y为%f,min_y为%f,max_z为%f,min_z为%f"%(max_x,min_x,max_y,min_y,max_z,min_z))