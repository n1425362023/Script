import unittest
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl



if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import numpy as np
    from pylab import mpl

    # 设置中文显示字体
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    mpl.rcParams["axes.unicode_minus"] = False

    # 假设你有一些数据点
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # x坐标
    y = [2.9,2.9,2.9,2.9,2.9,3.0,3.0,3.1,3.1]  # y坐标
    y1 = [16.5, 16.5, 16.6, 16.6, 16.6, 16.7, 16.7, 16.7, 16.7]
    y2 = [30.5, 30.5, 30.6, 30.6, 30.7, 30.7, 30.7, 30.7, 30.7]

    # 设置坐标轴刻度
    plt.xticks(np.arange(0, 10, 1))
    plt.yticks(np.arange(0, 40, 1))

    # 绘制数据点
    plt.scatter(x, y, color='blue', label='0')
    plt.scatter(x, y1, color='pink', label='5')
    plt.scatter(x, y2, color='green', label='10')
    # 对每组数据进行多项式拟合并绘制拟合曲线
    for data, color, label in zip([y, y1, y2], ['blue', 'pink', 'green'], ['0', '5', '10']):
        coefficients = np.polyfit(x, data, 2)  # 2表示二次多项式
        poly_eq = np.poly1d(coefficients)

        # 生成平滑曲线的x值
        x_smooth = np.linspace(min(x), max(x), 100)
        y_smooth = poly_eq(x_smooth)

        # 绘制拟合曲线
        plt.plot(x_smooth, y_smooth, color=color, label=f'{label} 拟合曲线')

    # 添加标题和标签
    plt.title('数据点和拟合曲线')
    plt.xlabel('X 轴')
    plt.ylabel('Y 轴')
    plt.legend()
    plt.grid()

    # 显示图形
    plt.show()
