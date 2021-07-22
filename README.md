# Step 1
```
pip install -r requirements.txt  # install
```
# Step 2

将yolo格式的标注数据放入../datasets,设置训练集和验证集 

# Step 3
```
cp data/coco128.yaml your_dataset.yaml
```
修改your_dataset.yaml

# Step 4
下载预训练权重[yolov5s.pt](https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt),放在当前路径yolov5/下

# Step 5
```
python train.py --img 640 --batch 16 --epochs 50 --data data/your_dataset.yaml --weights yolov5s.pt
```
# Step 6
生成wts文件
```
python gen_wts.py runs/train/exp/weights/best.pt
```
最终得到best.wts


# reference
参考[Train-Custom-Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)