import json
import os
from IPython import embed

# create json
generate_json = dict()
generate_json['images'] = list()
generate_json['annotations'] = list()
generate_json['categories'] = list()

# write categories
categories = ['plate', 'insulator', 'point','hot']
for i in range(len(categories)):
    json_category = dict()
    json_category['id'] = i
    json_category['name'] = categories[i]

    generate_json['categories'].append(json_category)

# write images and annotations
SOURCE_PATH = 'test/test_json' #  adjust here
image_count = 0
annotation_count = 0

for source_json_path in os.listdir(SOURCE_PATH):
    with open(SOURCE_PATH + '/' + source_json_path) as source_json_abspath:
        source_json_file = json.load(source_json_abspath)
    # write image
    print('prepare for image {}'.format(source_json_path))
    json_image = dict()
    json_image['id'] = image_count
    json_image['width'] = int(source_json_file['annotation']['size']['width'])
    json_image['height'] = int(source_json_file['annotation']['size']['height'])
    json_image['file_name'] = '{:0>8}'.format(source_json_file['annotation']['filename'])

    generate_json['images'].append(json_image)

    # write annotation
    source_annotations = source_json_file['annotation']['object']
    if not isinstance(source_annotations, list):
        source_annotations = [source_annotations]
    for bbox in source_annotations:
        json_annotation = dict()
        json_annotation['id'] = annotation_count
        json_annotation['image_id'] = image_count
        json_annotation['category_id'] = categories.index(bbox['name'])
        xmin = int(bbox['bndbox']['xmin'])
        ymin = int(bbox['bndbox']['ymin'])
        xmax = int(bbox['bndbox']['xmax'])
        ymax = int(bbox['bndbox']['ymax'])
        json_annotation['area'] = (xmax - xmin + 1) * (ymax - ymin + 1)
        json_annotation['bbox'] = [xmin, ymin, xmax - xmin + 1, ymax - ymin + 1]
        json_annotation['iscrowd'] = 0

        generate_json['annotations'].append(json_annotation)
        annotation_count += 1
    print(len(generate_json))
    image_count += 1
    print('{} is done'.format(source_json_path))

# save json
with open('test/train.json', 'w') as generate_json_path:  #  adjust here
    json.dump(generate_json, generate_json_path, indent=4)
print('Done')
