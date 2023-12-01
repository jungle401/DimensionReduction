import numpy as np
import matplotlib.image as mpimg
import os
import matplotlib.pyplot as plt

def read_images(images_dir):
    images = np.array([mpimg.imread(images_dir+str(file)).reshape(-1) 
                       for file in os.listdir(images_dir) if file.endswith(".pgm")])
    labels = []
    for file in os.listdir(images_dir):
        labels.append(int(file[7:9]))
        
    return images, labels

def read_images_inorder(path):
    ff = []
    for file in os.listdir(path):
        ff.append(file)
    images = np.array([mpimg.imread(path+str(file)).reshape(-1) for file in sorted(ff)])
    labels = []
    for file in sorted(ff):
        labels.append(int(file[7:9]))
    return images, labels

if __name__ == '__main__':
    images, labels = read_images('../Yale_Face_Database/Testing/')
    print(labels)
    testimages = read_images_inorder('../Yale_Face_Database/Testing/')
    plt.imshow(testimages[1].reshape((231,195)),cmap=plt.cm.gray)

