import json
import os


def convert_json_to_yolo(json_file, img_width, img_height):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = {0: '不导电', 1: '擦花', 2: '角位漏底', 3: '桔皮',
                  4: '漏底', 5: '喷流', 6: '漆泡', 7: '起坑', 8: '杂色', 9: '脏点'}  # 根据实际情况进行分类标签的映射

    yolo_lines = []
    for shape in data['shapes']:
        label = shape['label']
        category_id = list(categories.keys())[list(categories.values()).index(label)]
        points = shape['points']
        x_min = min(point[0] for point in points)
        y_min = min(point[1] for point in points)
        x_max = max(point[0] for point in points)
        y_max = max(point[1] for point in points)

        x_center = (x_min + x_max) / (2 * img_width)
        y_center = (y_min + y_max) / (2 * img_height)
        width = (x_max - x_min) / img_width
        height = (y_max - y_min) / img_height

        yolo_lines.append(f"{category_id} {x_center} {y_center} {width} {height}")

    return yolo_lines


def main():
    input_folder = r"D:\ultralytics-main\ultralytics-main\datasets\bvn\labels\val"
    output_folder = r"D:\ultralytics-main\ultralytics-main\datasets\bvn\labels\train"
    img_width = 2560  # 图像宽度
    img_height = 1920  # 图像高度

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            json_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace('.json', '.txt'))
            yolo_lines = convert_json_to_yolo(json_file, img_width, img_height)
            with open(output_file, 'w') as f:
                f.write('\n'.join(yolo_lines))


if __name__ == "__main__":
    main()
