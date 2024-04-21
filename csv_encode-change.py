import os
import pandas as pd
def try_encodings(file_path, encodings):
    df = None
    for encoding in encodings:
        try:
            # 当读取数据遇到编码问题时，会跳过含有问题的行
            df = pd.read_csv(file_path, encoding=encoding, error_bad_lines=False)
            break
        except UnicodeDecodeError:
            continue
    return df
def copy_columns(file_path, new_directory, new_file_name, encodings, cols_to_copy):
    df = try_encodings(file_path, encodings)
    # 新的文件路径
    new_file_path = os.path.join(new_directory, new_file_name)
    # 将特定列保存到新文件中
    df[cols_to_copy].to_csv(new_file_path, index=False, encoding='utf_8_sig')
    print(f'文件：{file_path} 处理完成，新文件已保存到：{new_file_path}')
def main(directory_path, new_directory, encodings, cols_to_copy):
    # 遍历目录下的所有文件
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv'):
            # 获得待处理文件完整路径
            full_file_path = os.path.join(directory_path, file_name)
            # 新文件的名称，原来的文件名替换为'new.csv'
            new_file_name = file_name.replace('.csv', 'new.csv')
            copy_columns(full_file_path, new_directory, new_file_name, encodings, cols_to_copy)
if __name__ == "__main__":
    directory_path = 'D:\\POI'
    new_directory = 'E:\\poi'
    encodings = ['utf-8', 'gb2312', 'gbk'] # 可能的编码方式
    columns_to_copy = ['name', 'location','type']  # 需要复制的列名
    main(directory_path, new_directory, encodings, columns_to_copy)