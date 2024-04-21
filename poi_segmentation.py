import pandas as pd
import glob
import os
import chardet
# 定义获取文件编码格式的函数
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc
# 指定源文件所在的目录
source_directory = 'E:\\poi\\'
# 指定保存新生成文件的目录
destination_directory = 'E:\\POI1\\'
# 循环处理源目录下的所有csv文件
for filepath in glob.glob(source_directory + '*.csv'):
    # 获取文件的编码格式
    my_encoding = find_encoding(filepath)
    # 读取csv文件到df中，注意编码格式
    df = pd.read_csv(filepath, encoding=my_encoding)
    # 使用str.split方法，将'location'列根据逗号分割成两列'location_x'和 'location_y'
    df[['location_x', 'location_y']] = df['location'].str.split('，', expand=True).astype(float)
    # 构造新生成文件的全路径名
    new_filepath = os.path.join(destination_directory,os.path.basename(filepath).replace('.csv', '_new.csv'))
    # 将处理后的DataFrame保存到新文件里，并使用源文件相同的编码
    df.to_csv(new_filepath, index=False, encoding=my_encoding)
    # 输出一条消息，告诉用户哪个文件已经被处理完，新文件保存在哪里
    print(f"文件 {os.path.basename(filepath)} 已经处理完成，新文件已经保存到 {new_filepath}")