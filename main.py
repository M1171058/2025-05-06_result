import os
import pandas as pd
import shutil
import random
from PIL import Image
from tqdm import tqdm
from ultralytics import YOLO

from fuction.cvstoYOLOtxt import convert_cvs_folder
from fuction.splitfiles import split_dateset

# if __name__ == "__main__":
#     # convert_cvs_folder(r'D:\桌面\公開資料集\LISA',r'D:\桌面\公開資料集\LISA\Annotations\Annotations',r'D:\桌面\公開資料集\LISA_labels')
#     split_dateset(r'D:\桌面\公開資料集\LISA',r'D:\桌面\公開資料集\LISA_labels', r'D:\桌面\公開資料集\LISA_YOLO')

if __name__ == "__main__":
    model = YOLO('yolov8m.pt')
    model.train(
        data='data.yaml',
        epochs = 10,
        imgsz = 640,
        batch = 16,
        project = r"D:\桌面\2025.5.5",
        name = "2025/5/6_yolo",
        device = 0
                )


