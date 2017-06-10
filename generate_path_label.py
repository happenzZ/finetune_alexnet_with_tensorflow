# -*- coding: UTF-8 -*-

import os

image_path = r'E:\dataset\dogs_vs_cats\train'

image_name_list = os.listdir(image_path)

cat_image_list = []
dog_image_list = []

for idx, image_name in enumerate(image_name_list):
    if image_name.startswith('cat'):
        cat_image_list.append(image_name)
    elif image_name.startswith('dog'):
        dog_image_list.append(image_name)
    else:
        print('redundant images')

cat_image_list = sorted(cat_image_list, key=lambda x: int(x.split('.')[1]))
print(cat_image_list)

dog_image_list = sorted(dog_image_list, key=lambda x: int(x.split('.')[1]))

print(dog_image_list)

train_image_cat = cat_image_list[:int(len(cat_image_list)*0.7)]
val_image_cat = cat_image_list[int(len(cat_image_list)*0.7): int(len(cat_image_list)*0.85)]
test_image_cat = cat_image_list[int(len(cat_image_list)*0.85):]

print('cat: train_{}, val_{}, test_{}'.format(len(train_image_cat), len(val_image_cat), len(test_image_cat)))

train_image_dog = dog_image_list[:int(len(dog_image_list)*0.7)]
val_image_dog = dog_image_list[int(len(dog_image_list)*0.7): int(len(dog_image_list)*0.85)]
test_image_dog = dog_image_list[int(len(dog_image_list)*0.85):]

print('dog: train_{}, val_{}, test_{}'.format(len(train_image_cat), len(val_image_dog), len(test_image_dog)))


def gen_path_label(image_cat, image_dog, type='train'):
    assert len(image_cat) == len(image_dog)
    with open('{}.txt'.format(type), 'w') as wf:
        for idx in range(len(image_cat)):
            wf.write('{}\{} {}\n'.format(image_path, image_cat[idx], 0))
            wf.write('{}\{} {}\n'.format(image_path, image_dog[idx], 1))
    return

gen_path_label(train_image_cat, train_image_dog, type='train')
gen_path_label(val_image_cat, val_image_dog, type='val')
gen_path_label(test_image_cat, test_image_dog, type='test')
