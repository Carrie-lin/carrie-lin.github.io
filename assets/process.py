from PIL import Image
import numpy as np

# 读取GIF文件
gif_path =  '/Users/linguying/Documents/code/carrie-lin.github.io/assets/publications/progress.gif'
gif_image = Image.open(gif_path)

# 将GIF文件的每一帧转换为NumPy数组
frames = []
for frame in range(gif_image.n_frames):
    gif_image.seek(frame)
    frame_np = np.array(gif_image)
    frames.append(frame_np)

# 在每一帧上进行编辑（这里只是示例，您可以根据需要进行自定义编辑）
edited_frames = []
i=0
for frame_np in frames:
    # 在这里对每一帧进行编辑，可以使用NumPy的各种图像处理操作
    #print(frame_np.shape)
    #frame_np = frame_np[5:-5,5:-5]
    i += 1
    if i>230:
        continue 
    if i == 1:
        continue

    edited_frame_np = frame_np.copy()  # 这里只是复制原始帧
    edited_frames.append(edited_frame_np)

# 创建新的GIF文件
output_path = '/Users/linguying/Documents/code/carrie-lin.github.io/assets/publications/progress_2.gif'
output_images = [Image.fromarray(frame_np) for frame_np in edited_frames]

# 保存为GIF文件
output_images[0].save(output_path, save_all=True, append_images=output_images[1:], optimize=False, duration=2, loop=0)