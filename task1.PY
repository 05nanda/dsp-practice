import numpy as np
import matplotlib.pyplot as plt

fs = 2000
t = np.arange(0, 1, 1/fs)

signal = np.sin(2 * np.pi * 50 * t)
noise = 0.5 * np.sin(2 * np.pi * 500 * t)
x = signal + noise
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(t[:200], x[:200])
plt.xlabel('时间 (s)')
plt.ylabel('幅值')
plt.title('带噪声的信号（时域）')
X = np.fft.fft(x)                # 1. 对信号做FFT
freq = np.fft.fftfreq(len(x), 1/fs)  # 2. 生成频率轴
plt.plot(freq, np.abs(X))        # 3. 画频谱图
plt.show()
plt.show()