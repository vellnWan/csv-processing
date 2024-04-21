import pandas as pd  # 导入pandas库
import glob  # 导入glob库
import os  # 导入os库
import chardet  # 导入chardet库
def find_encoding(fname):
    # 定义一个函数用于找出文件的编码方式
    r_file = open(fname, 'rb').read()  # 以二进制方式打开文件，进行读取操作
    result = chardet.detect(r_file)  # 利用chardet库找出文件的编码方式
    charenc = result['encoding']  # 提取出编码方式
    return charenc  # 返回文件的编码方式
source_directory = 'E:\\poi\\'  # 设置源文件的路径
destination_directory = 'E:\\POI1\\'  # 设置目标文件的路径
if not os.path.exists(destination_directory):  # 查询是否已存在目标路径
    os.makedirs(destination_directory)  # 如果不存在，则创建目标路径
count = 1  # 设置初始处理的文件计数为1
for filepath in glob.glob(source_directory + '*.csv'):  # 遍历源文件路径下的所有csv文件
    my_encoding = find_encoding(filepath)  # 查找每个文件的编码方式
    df = pd.read_csv(filepath, encoding=my_encoding)  # 根据文件的编码方式读取文件内容
    split_df = df['type'].str.split(';', expand=True, n=2)  # 使用分号作为分割标准，并将分割数限制在2次内，多余部分不再分割
    for i in range(split_df.shape[1], 3):
        split_df[i] = None  # 如果分割后的列数少于3，则将剩余的列填充None，确保split_df总是有三列
    df[['type1', 'type2', 'type3']] = split_df  # 将split_df的内容赋值给原表格中的这三列
    df = df.drop(columns='type')  # 删除原始的'type'列
    new_filepath = os.path.join(destination_directory, f'poi{count}.csv')  # 创建新的文件路径
    df.to_csv(new_filepath, index=False, encoding=my_encoding)  # 将处理完的数据通过新的文件路径输出，并保持原来的编码形式
    print(f"文件 {os.path.basename(filepath)} 已经处理完成，新文件已经保存到 {new_filepath}")  # 打印输出处理完成的信息
    count += 1  # 处理完成后，计数器累加1