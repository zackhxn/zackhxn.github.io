import os
import re
import requests
from urllib.parse import urlparse
from pathlib import Path
from tqdm import tqdm
# 配置文件路径
md_file_path = "_posts/2024-05-29-softwarelesson.markdown"  # 替换为你的Markdown文件路径
img_folder = "img"

# 读取Markdown文件内容
with open(md_file_path, "r", encoding="utf-8") as file:
    md_content = file.read()

# 匹配Markdown文件中的图片链接
img_urls = re.findall(r"!\[.*?\]\((https?://.*?)\)", md_content)

# 下载图片并替换路径
for i, url in tqdm(enumerate(img_urls)):
    # 获取图片扩展名
    parsed_url = urlparse(url)
    img_extension = os.path.splitext(parsed_url.path)[1]
    # 图片保存路径
    img_local_path = os.path.join(img_folder, f"{Path(md_file_path).stem}_{i+1}{img_extension}")
    
    # 下载图片
    response = requests.get(url)
    with open(img_local_path, "wb") as img_file:
        img_file.write(response.content)
    
    # 替换Markdown内容中的图片路径
    length = len(img_folder)+1
    img_github_path = img_local_path[length:]
    img_github_path = 'https://zackhxn.github.io/img/' + img_github_path
    md_content = md_content.replace(url, img_github_path)
# print(md_content)
# 保存修改后的Markdown文件
with open(md_file_path, "w", encoding="utf-8") as file:
    file.write(md_content)

print("图片下载并路径替换完成。")
