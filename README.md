## 环境
·win + pycharm
·sahi==0.8.4
·yolov5==5.0
·pytorch==1.7.1+cu101
```commandline
# 安装gpu版torch和torchvision
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
# 
pip install yolov5
pip install sahi==0.8.4
pip install fiftyone imantics
```

## RUN

1. git clone https://github.com/kivenyangming/SAHI-yolov5.git
2. tree:\
        main.py\
        README.md\
        samll-vehicles1.jpg\
        yolov5s6.pt
   
3. vim main.py:
```commandline

line4: yolov5_model_path  = yolov5_model_path = "C:\\Users\\kiven\\Desktop\\SAHI\\yolov5s6.pt"  # 放置你的权重地址
line10:  device="cuda:0",            # or 'cpu'

```
4. please change your path and divice
5. python main.py

