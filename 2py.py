import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题


def plot_common_functions():
    """绘制常见的数学函数图像"""
    # 创建一个20x15的图形
    plt.figure(figsize=(20, 15))

    # 创建网格布局
    gs = GridSpec(5, 2, figure=plt.gcf())

    # 生成x值
    x_lin = np.linspace(-10, 10, 1000)  # 线性函数等的x范围
    x_sin = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # 三角函数的x范围
    x_log = np.linspace(0.01, 10, 1000)  # 对数函数的x范围（避免0和负数）
    x_tan = np.linspace(-1.3 * np.pi, 1.3 * np.pi, 1000)  # 正切函数的x范围
    x_sqrt = np.linspace(0, 10, 1000)  # 平方根函数的x范围

    # 1. 线性函数 y = x
    ax1 = plt.subplot(gs[0, 0])
    ax1.plot(x_lin, x_lin)
    ax1.set_title('线性函数: y = x')
    ax1.grid(True)
    ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax1.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 2. 二次函数 y = x²
    ax2 = plt.subplot(gs[0, 1])
    ax2.plot(x_lin, x_lin ** 2)
    ax2.set_title('二次函数: y = x²')
    ax2.grid(True)
    ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax2.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 3. 三次函数 y = x³
    ax3 = plt.subplot(gs[1, 0])
    ax3.plot(x_lin, x_lin ** 3)
    ax3.set_title('三次函数: y = x³')
    ax3.grid(True)
    ax3.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax3.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 4. 指数函数 y = eˣ
    ax4 = plt.subplot(gs[1, 1])
    ax4.plot(x_lin, np.exp(x_lin))
    ax4.set_title('指数函数: y = eˣ')
    ax4.grid(True)
    ax4.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax4.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 5. 对数函数 y = ln(x)
    ax5 = plt.subplot(gs[2, 0])
    ax5.plot(x_log, np.log(x_log))
    ax5.set_title('对数函数: y = ln(x)')
    ax5.grid(True)
    ax5.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax5.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 6. 正弦函数 y = sin(x)
    ax6 = plt.subplot(gs[2, 1])
    ax6.plot(x_sin, np.sin(x_sin))
    ax6.set_title('正弦函数: y = sin(x)')
    ax6.grid(True)
    ax6.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax6.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 7. 余弦函数 y = cos(x)
    ax7 = plt.subplot(gs[3, 0])
    ax7.plot(x_sin, np.cos(x_sin))
    ax7.set_title('余弦函数: y = cos(x)')
    ax7.grid(True)
    ax7.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax7.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 8. 正切函数 y = tan(x)
    ax8 = plt.subplot(gs[3, 1])
    ax8.plot(x_tan, np.tan(x_tan))
    ax8.set_ylim(-10, 10)  # 限制y轴范围，避免正切函数无穷大值影响显示
    ax8.set_title('正切函数: y = tan(x)')
    ax8.grid(True)
    ax8.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax8.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 9. 平方根函数 y = √x
    ax9 = plt.subplot(gs[4, 0])
    ax9.plot(x_sqrt, np.sqrt(x_sqrt))
    ax9.set_title('平方根函数: y = √x')
    ax9.grid(True)
    ax9.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax9.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 10. 绝对值函数 y = |x|
    ax10 = plt.subplot(gs[4, 1])
    ax10.plot(x_lin, np.abs(x_lin))
    ax10.set_title('绝对值函数: y = |x|')
    ax10.grid(True)
    ax10.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax10.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图像
    plt.show()


if __name__ == "__main__":
    plot_common_functions()
