import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

# 目录路径
programs_dir = './codes'
output_dir = './imgs'
code_imgs_path = output_dir + '/code_imgs'
effect_imgs_path = output_dir + '/effect_imgs'

# 创建保存输出的目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(code_imgs_path):
    os.makedirs(code_imgs_path)
if not os.path.exists(effect_imgs_path):
    os.makedirs(effect_imgs_path)

# 设置字体大小和行间距
font_size = 20  # 修改字体大小
line_spacing = 10  # 设置额外的行间距
try:
    font = ImageFont.truetype("arial.ttf", font_size)  # 可根据实际路径修改字体
except IOError:
    font = ImageFont.load_default()

# 函数：将代码转换为图像，并在第一行添加文件路径
def save_code_as_image(file_path, code_imgs_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 在第一行添加文件路径
    lines.insert(0, f"python {file_path}\n")
    lines.insert(1, "\n") 

    # 图像尺寸估计
    line_height = font_size + line_spacing  # 每行的高度，包含额外的间距
    width = 800
    height = line_height * len(lines) + 40  # 计算总高度
    img = Image.new('RGB', (width, height), color=(0, 0, 0))  # 黑色背景
    draw = ImageDraw.Draw(img)

    # 在图像上绘制代码文本（白色文字）
    y_text = 10
    for line in lines:
        draw.text((10, y_text), line.strip(), font=font, fill=(255, 255, 255))  # 白色文字
        y_text += line_height  # 更新 y 坐标

    img.save(code_imgs_path)

# 函数：将输出结果转换为图像，并在第一行添加文件路径，最后添加 "Process finished with exit code 0"
def save_output_as_image(output_text, effect_imgs_path, script_path):
    lines = output_text.splitlines()

    # 在第一行添加文件路径
    lines.insert(0, f" {script_path}")

    # 在结尾添加 "Process finished with exit code 0" 和一个空行
    lines.append("")
    lines.append("Process finished with exit code 0")

    # 图像尺寸估计
    line_height = font_size + line_spacing  # 每行的高度，包含额外的间距
    width = 800
    height = line_height * len(lines) + 40  # 计算总高度
    img = Image.new('RGB', (width, height), color=(0, 0, 0))  # 黑色背景
    draw = ImageDraw.Draw(img)

    # 在图像上绘制输出文本（白色文字）
    y_text = 10
    for line in lines:
        draw.text((10, y_text), line.strip(), font=font, fill=(255, 255, 255))  # 白色文字
        y_text += line_height  # 更新 y 坐标

    img.save(effect_imgs_path)

# 执行每个脚本并截图
for script in os.listdir(programs_dir):
    if script.endswith('.py'):
        script_path = os.path.join(programs_dir, script)
        script_name = os.path.splitext(script)[0]

        # 1. 保存代码截图（在第一行添加文件路径）
        code_image_file = os.path.join(code_imgs_path, f"{script_name}_code.png")
        save_code_as_image(script_path, code_image_file)
        print(f"Code screenshot saved for {script_name}")

        # 2. 运行 Python 脚本并捕获输出
        print(f"Running {script_path}")
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # 将标准输出和标准错误组合
        output_text = stdout + '\n' + stderr
        if not output_text.strip():
            output_text = "No output."

        # 3. 保存输出结果为图片（在第一行添加文件路径，最后添加 "Process finished with exit code 0"）
        output_image_file = os.path.join(effect_imgs_path, f"{script_name}_output.png")
        save_output_as_image(output_text, output_image_file, script_path)
        print(f"Output screenshot saved for {script_name}")
