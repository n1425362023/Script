import os
import requests
import json
import shutil

def post():
    # 手动开启PicGo server ，配置PicGo的Web上传接口URL，根据实际情况替换
    PICGO_API_URL = 'http://127.0.0.1:36677/upload'

    # 图片存放的文件夹路径，更新为待上传
    IMAGE_FOLDER_PATH = 'D:/test/picture/pending_uploads/'  # Renamed to pending_uploads
    # 上传成功后移动图片的目标文件夹
    DESTINATION_FOLDER_PATH = 'D:/test/picture/uploaded_imgs/'

    # 确保目标文件夹存在
    os.makedirs(DESTINATION_FOLDER_PATH, exist_ok=True)

    # 获取文件夹中所有图片文件的路径
    image_files = [os.path.join(IMAGE_FOLDER_PATH, f) for f in os.listdir(IMAGE_FOLDER_PATH) if
                   f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # 存储上传后图片的URL
    image_urls = []

    # 批量上传图片
    for image_path in image_files:
        print(f"正在上传: {image_path}")
        json_data = {
            'list': [f'{image_path}']
        }
        response = requests.post(PICGO_API_URL, json=json_data)

        # 检查响应状态
        if response.status_code == 200:
            # PicGo返回的JSON格式为：{"success": true, "result": "url_to_image"}
            result = response.json()
            if result['success']:
                image_urls.append(result['result'])
                print(f"图片上传成功，URL: {result['result']}")
                # 移动上传成功的图片到目标文件夹
                shutil.move(image_path, os.path.join(DESTINATION_FOLDER_PATH, os.path.basename(image_path)))
                print(f"图片已移动到: {DESTINATION_FOLDER_PATH}")
            else:
                print(f"图片上传失败: {result}")
        else:
            print(f"网络请求错误，状态码: {response.status_code}")

    # 打印所有上传成功的图片URL
    print("所有上传成功的图片URL:")
    for url in image_urls:
        print(url)

if __name__ == '__main__':
    post()
