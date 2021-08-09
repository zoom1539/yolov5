import os

def listdir(dir, list_name):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1]=='.jpg':
            list_name.append(file_path)

if __name__ == "__main__":
    work_dir = '/root/PLATFORM/pb_train/datasets/mine_car_balance/images/train'
    list_name = []
    listdir(work_dir, list_name)

    for i, path in enumerate(list_name):
        if i % 10 == 0:
            dst = '/root/PLATFORM/pb_train/datasets/mine_car_balance/images/val'
            os.system('mv {} {}'.format(path, dst))
            txt_path = path.replace('images','labels').replace('jpg','txt')
            if os.path.exists(txt_path):
                txt_dst = '/root/PLATFORM/pb_train/datasets/mine_car_balance/labels/val'
                os.system('mv {} {}'.format(txt_path, txt_dst))

