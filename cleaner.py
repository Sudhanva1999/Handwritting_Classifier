import os
img_names = os.listdir('sampleData/')
for i in img_names:
    if i[-8:]=='Copy.png':
        path='sampleData/'+i
        os.remove(path)