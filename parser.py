import os

from gluoncv import data, utils
from matplotlib import pyplot as plt

PATH_TO_DATASET = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

if not PATH_TO_DATASET:
    os.mkdir(PATH_TO_DATASET)
    
if os.name == 'nt':
    os.system('pip install -r requirements.txt')
    os.system('python pascal_voc.py --download-dir {}'.format(PATH_TO_DATASET))
else:
    os.system('pip3 install -r requirements.txt')
    os.system('python3 pascal_voc.py --download-dir {}'.format(PATH_TO_DATASET))

# path_to_dataset = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
#
# train_dataset = data.VOCDetection(root=path_to_dataset,
#                                   splits=[(2007, 'trainval'), (2012, 'trainval')])
# val_dataset = data.VOCDetection(root=path_to_dataset,
#                                 splits=[(2007, 'test')])
# print(train_dataset)
# print('Num of training images:', len(train_dataset))
# print('Num of validation images:', len(val_dataset))
#
# train_image, train_label = train_dataset[102]
# print('Image size (height, width, RGB):', train_image.shape)
#
# bounding_boxes = train_label[:, :4]
# print('Num of objects:', bounding_boxes.shape[0])
# print('Bounding boxes (num_boxes, x_min, y_min, x_max, y_max):\n', bounding_boxes)
#
# class_ids = train_label[:, 4:5]
# print('Class IDs (num_boxes, ):\n', class_ids)
#
# utils.viz.plot_bbox(
#     train_image.asnumpy(),
#     bounding_boxes,
#     scores=None,
#     labels=class_ids,
#     class_names=train_dataset.classes
# )
# plt.show()

#
# def preapare_dataset(dataset):
#     images = []
#     labels = []
#     bounding_boxes = []
#     class_ids = []
#     for single_set in dataset:
#         image, label = single_set
#         images.append(image)
#         labels.append(label)
#         bounding_boxes.append(label[:, :4])
#         class_ids.append(label[:, 4:5])
#     return images, labels, bounding_boxes, class_ids
#
#
# train_images, train_labels, bounding_boxes, class_ids = preapare_dataset(train_dataset)
# print(class_ids)
