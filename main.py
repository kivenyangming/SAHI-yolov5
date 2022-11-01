from sahi.model import Yolov5DetectionModel
from sahi.predict import get_sliced_prediction

yolov5_model_path = "C:\\Users\\kiven\\Desktop\\SAHI\\yolov5s6.pt"  # 放置你的权重地址

# 使用的YOLOv5检测模型，使用gpu加速，置信度0.3
detection_model = Yolov5DetectionModel(
    model_path=yolov5_model_path,
    confidence_threshold=0.3,   # 置信度
    device="cuda:0",            # or 'cpu'
)

# 方法将待测试图片分成多个小图(默认是256x256)，各自分别检测，最后进行拼接。小图框高宽重叠默认0.2，换算成像素就是256x0.2=51pixel。如果需要检测图片文件夹的话，可以使用方法predict
result = get_sliced_prediction(
    "small-vehicles1.jpg",   # 调用的图像名称
    detection_model,         # 调用的模型
    slice_height=256,        # 分成的小图 高
    slice_width=256,         # 分成的小图 宽
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2
)

# 保存检测图片
result.export_visuals(export_dir="result/")