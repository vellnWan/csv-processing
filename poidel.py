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
source_directory = '输入路径'
# 指定保存新生成文件的目录
new_directory = '输出路径'
# 确保新路径存在，如果不存在，创建它
if not os.path.exists(new_directory):
    os.makedirs(new_directory)
# 循环处理源目录下所有的csv文件
for filepath in glob.glob(source_directory + '*.csv'):
    # 获取文件的编码格式
    my_encoding = find_encoding(filepath)
    # 读取csv文件到df中，注意编码格式
    df = pd.read_csv(filepath, encoding=my_encoding)
    # 删除需要删除的列
    df = df.drop(columns='location')
    # 构造新生成文件的全路径名
    new_filepath = os.path.join(new_directory, os.path.basename(filepath))
    # 将处理后的 DataFrame 保存到新文件里，并使用源文件相同的编码
    df.to_csv(new_filepath, index=False, encoding=my_encoding)
    # 输出一条消息，告诉用户哪个文件已经被处理完，新文件保存在哪里
    print(f"文件 {os.path.basename(filepath)} 已经处理完成，新文件已经保存到 {new_filepath}")
