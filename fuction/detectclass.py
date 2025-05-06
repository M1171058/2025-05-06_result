import os
import pandas as pd
data_dir = r'D:\桌面\公開資料集\LISA\Annotations\Annotations'
csv_dir = [f'daySequence{i}' for i in range(1,3)] + [f'dayTrain/dayClip{i}' for i in range(1,14)] +[f'nightSequence{i}' for i in range(1,3)] + [f'nightTrain/nightClip{i}' for i in range(1,6)]
# for csv in csv_dir:
#     csv_path = os.path.join(data_dir,csv,'frameAnnotationsBOX.csv')
#     df = pd.read_csv(csv_path,sep = ';')
#     if 'Annotation tag' in df.columns:
#         print(f"{csv} 中類別分布：")
#         print(df['Annotation tag'].value_counts())
df_list = []

for csv in csv_dir:
    csv_path = os.path.join(data_dir, csv, 'frameAnnotationsBOX.csv')

    # if not os.path.exists(csv_path):
    #     print(f"❌ {csv_path} 不存在")
    #     continue

    df = pd.read_csv(csv_path, sep=';')

    if 'Annotation tag' in df.columns:
        df_list.append(df[['Annotation tag']])

# 合併所有 DataFrame
all_df = pd.concat(df_list, ignore_index=True)

# 統計並印出
print("\n 所有資料集中 Annotation tag 的出現次數：")
print(all_df['Annotation tag'].value_counts())