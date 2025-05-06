import os
import pandas as pd
from PIL import Image
from tqdm import tqdm

def convert_cvs_folder (images_folder,labels_folder,output_folder):
    daySequence = [f'daySequence{i}' for i in range(1,3) ]
    dayTrainClips = [f'dayTrain/dayClip{i}' for i in range(1,14)]
    nightSequence = [f'nightSequence{i}'for i in range(1,3)]
    nightTrainClips = [f'nightTrain/nightClip{i}'for i in range(1,6)]
    class_map={
        'go' : 0,
        'stop' :1,
        'stopLeft' :2,
        'warning' :3,
        'warningLeft':4,
        'goForward':5,
        'goLeft' :6
    }
    
    all_sequence=daySequence+dayTrainClips+nightSequence+nightTrainClips
    for seq in all_sequence:
        cvs_path = os.path.join(labels_folder,seq,'frameAnnotationsBOX.csv')
        output_dir_path = os.path.join(output_folder,seq)
        images_dir = os.path.join(images_folder,seq,'frames')
        os.makedirs(output_dir_path,exist_ok=True)
        df = pd.read_csv(cvs_path,sep=';')
        for _,row in tqdm(df.iterrows(), total=len(df)):
            images_name = os.path.basename(row['Filename'])
            class_names = row['Annotation tag']
            if class_names not in class_map:
                print(f"***************found {class_names} not in class_map********************")
                break
            class_id = class_map[class_names]
            images_path= os.path.join(images_dir,images_name)
            if not os.path.exists(images_path):
                print(f"******************{images_path} not found***************")
                break       
            img = Image.open(images_path)
            img_w,img_h = img.size

            xmin = row['Upper left corner X']
            xmax = row['Lower right corner X']
            ymax = row['Lower right corner Y']
            ymin = row["Upper left corner Y"]

            x_center = (xmax+xmin)/2/img_w
            y_center = (ymax+ymin)/2/img_h
            width = (xmax-xmin)/img_w
            height = (ymax-ymin)/img_h

            label_file = os.path.splitext(images_name)[0]+'.txt'
            label_path= os.path.join(output_dir_path,label_file)
            
            with open(label_path,mode='a') as f:
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
    print("轉換完成")