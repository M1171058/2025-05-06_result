import os
import shutil
import random

def split_dateset(images_dir,labels_dir,output_dir,train_ration=0.8):
    for subdir in ['images/train','images/val','labels/train','labels/val']:
        os.makedirs(os.path.join(output_dir,subdir),exist_ok=True)

    all_subfolders = ([f'daySequence{i}' for i in range(1, 3)] + [f'dayTrain/dayClip{i}' for i in range(1, 14)] +[f'nightSequence{i}' for i in range(1, 3)] +[f'nightTrain/nightClip{i}' for i in range(1, 6)])
    for subset in all_subfolders:
        label_path = os.path.join(labels_dir,subset)
        image_path = os.path.join(images_dir,subset,'frames')

        if not os.path.exists(label_path):
            print(f'************{label_path} 不存在************')
            break

        if not os.path.exists(image_path):
            print(f'************{image_path} 不存在*************')
            break
        all_images = [ f for f in os.listdir(image_path) if f.endswith('.jpg')]
        random.shuffle(all_images)
        spilt_index = int(len(all_images)*train_ration)
        train_images = all_images[:spilt_index]
        val_images = all_images[spilt_index:]

        def copy_files(image_list,image_dest,lbl_dest):
            for img in image_list:
                lbl = img.replace('.jpg','.txt')
                src_img = os.path.join(image_path,img)#完整圖片路徑
                src_lbl = os.path.join(label_path,lbl)#完整label路徑
                if os.path.exists(src_lbl) and os.path.exists(src_img):
                    shutil.copy(src_img,os.path.join(image_dest,img))
                    shutil.copy(src_lbl,os.path.join(lbl_dest,lbl))
                else :
                    with open(os.path.join(output_dir,'missimg_files_log.txt'),mode='a') as f:
                        f.write(f"無法找到{src_img}對應label\n")
                    
        copy_files(train_images,
                   os.path.join(output_dir,'images/train'),
                   os.path.join(output_dir,'labels/train')
                   )
        copy_files(val_images,
                   os.path.join(output_dir,'images/val'),
                   os.path.join(output_dir,'labels/val')
                   )
        
        print(f"********************{subset}分割完成*********************")


