import cv2
import numpy as np
import imageio

# 读取MP4文件
video = cv2.VideoCapture('/Users/linguying/Documents/code/carrie-lin.github.io/assets/publications/progress.mp4')

frames = []
while True:
    ret, frame = video.read()
    if not ret:
        break
    frames.append(frame)

video.release()

# 将帧转换为NumPy数组
frames = np.array(frames)
frames = frames[:-70]

# 将NumPy数组保存为GIF文件
imageio.mimsave('/Users/linguying/Documents/code/carrie-lin.github.io/assets/publications/progress_2.gif', frames)
