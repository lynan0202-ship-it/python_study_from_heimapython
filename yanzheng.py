import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 或者直接设置使用系统支持的字体
matplotlib.rcParams['font.family'] = 'sans-serif'

import numpy as np
import pandas as pd
import seaborn as sns

# ============== 修复1: 改进的scikit-learn导入逻辑 ==============
LinearRegression = None
load_diabetes = None
sklearn_available = False
sklearn_version = "未安装"

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.datasets import load_diabetes

    sklearn_available = True
    # 修复版本获取方式
    import sklearn

    sklearn_version = getattr(sklearn, '__version__', '未知版本')
except ImportError as e:
    print(f"Scikit-learn导入失败: {e}")

# ============== 修复2: 改进的TensorFlow导入逻辑 ==============
tf_available = False
tf_version = "未安装"

try:
    import tensorflow as tf

    tf_available = True
    # 修复版本获取方式
    tf_version = getattr(tf, '__version__', '未知版本')
except ImportError as e:
    print(f"TensorFlow导入失败: {e}")

# ============== 修复3: 使用set_theme替代弃用的set函数 ==============
try:
    # 修复拼写错误：whitegrid 是正确的
    sns.set_theme(style="whitegrid")  # 使用正确的函数和参数
    # 修复版本获取方式
    seaborn_version = getattr(sns, '__version__', '未知版本')
except Exception as e:
    print(f"Seaborn设置失败: {e}")
    seaborn_version = "未知"

# ============== 验证NumPy ==============
print("验证NumPy...")
try:
    np_array = np.array([[1, 2, 3], [4, 5, 6]])
    print("NumPy数组示例：\n", np_array)
    # 修复版本获取方式
    numpy_version = getattr(np, '__version__', '未知版本')
    print("NumPy版本：", numpy_version)
    print("NumPy验证成功！\n")
except Exception as e:
    print(f"NumPy验证失败: {e}\n")

# ============== 验证Pandas ==============
print("验证Pandas...")
try:
    df = pd.DataFrame({
        "姓名": ["张三", "李四", "王五"],
        "年龄": [25, 30, 35],
        "城市": ["北京", "上海", "广州"]
    })
    print("Pandas DataFrame示例：\n", df)
    # 修复版本获取方式
    pandas_version = getattr(pd, '__version__', '未知版本')
    print("Pandas版本：", pandas_version)
    print("Pandas验证成功！\n")
except Exception as e:
    print(f"Pandas验证失败: {e}\n")

# ============== 验证Matplotlib & Seaborn ==============
print("验证Matplotlib & Seaborn...")
try:
    # 尝试加载内置数据集
    try:
        tips = sns.load_dataset("tips")
        print("成功加载Seaborn内置tips数据集")
    except Exception as e:
        print(f"无法加载内置数据集: {e}")
        # 创建示例数据作为备选
        import random

        tips_data = {
            'total_bill': [random.uniform(10, 50) for _ in range(50)],
            'tip': [random.uniform(1, 10) for _ in range(50)],
            'time': ['Lunch' if i % 2 == 0 else 'Dinner' for i in range(50)]
        }
        tips = pd.DataFrame(tips_data)
        print("使用生成的示例数据")

    # 创建可视化
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)
    plt.title("Matplotlib & Seaborn 可视化示例")
    plt.savefig("visualization_test.png")
    print("可视化图已保存为 visualization_test.png")

    # 修复版本获取方式
    matplotlib_version = getattr(matplotlib, '__version__', '未知版本')
    print("Matplotlib版本：", matplotlib_version)
    print("Seaborn版本：", seaborn_version)
    print("Matplotlib & Seaborn 验证成功！\n")
except Exception as e:
    print(f"Matplotlib & Seaborn验证失败: {e}\n")

# ============== 修复4: 改进的Scikit-learn验证逻辑 ==============
print("验证Scikit-learn...")
if sklearn_available and LinearRegression is not None and load_diabetes is not None:
    try:
        X, y = load_diabetes(return_X_y=True)
        model = LinearRegression()
        model.fit(X[:50], y[:50])
        score = model.score(X[50:], y[50:])
        print("线性回归模型得分：", score)
        print("Scikit-learn版本：", sklearn_version)
        print("Scikit-learn 验证成功！\n")
    except Exception as e:
        print(f"Scikit-learn验证失败: {e}\n")
else:
    print("Scikit-learn未安装或导入失败，跳过验证\n")

# ============== 修复5: 改进的TensorFlow验证逻辑 ==============
print("验证TensorFlow...")
if tf_available:
    try:
        # 尝试在线下载MNIST数据
        try:
            mnist = tf.keras.datasets.mnist
            (x_train, y_train), (x_test, y_test) = mnist.load_data()
            print("成功加载MNIST数据集")
        except Exception as e:
            print(f"MNIST数据集下载失败: {e}，使用随机数据验证TensorFlow...")
            # 创建随机数据作为替代
            x_train = np.random.random((1000, 28, 28)).astype(np.float32)
            y_train = np.random.randint(0, 10, (1000,)).astype(np.int32)
            x_test = np.random.random((200, 28, 28)).astype(np.float32)
            y_test = np.random.randint(0, 10, (200,)).astype(np.int32)

        x_train, x_test = x_train / 255.0, x_test / 255.0

        # 创建简单模型
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10)
        ])

        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

        # 只训练1个epoch进行验证
        history = model.fit(x_train, y_train, epochs=1, verbose=1, validation_split=0.2)

        print("TensorFlow版本：", tf_version)
        print("TensorFlow 验证成功！\n")
    except Exception as e:
        print(f"TensorFlow验证失败: {e}\n")
else:
    print("未检测到TensorFlow，若需验证请先安装（pip install tensorflow）\n")

print("所有已安装库验证完成！")

# ============== 生成依赖文件建议 ==============
print("\n" + "=" * 50)
print("依赖配置建议：")
print("在 requirements.txt 中添加以下依赖：")

# 获取当前安装的版本
try:
    matplotlib_req = f"matplotlib>={matplotlib_version}" if matplotlib_version != '未知版本' else "matplotlib"
    numpy_req = f"numpy>={numpy_version}" if numpy_version != '未知版本' else "numpy"
    pandas_req = f"pandas>={pandas_version}" if pandas_version != '未知版本' else "pandas"
    seaborn_req = f"seaborn>={seaborn_version}" if seaborn_version != '未知版本' else "seaborn"

    requirements = [
        matplotlib_req,
        numpy_req,
        pandas_req,
        seaborn_req,
    ]

    if sklearn_available and sklearn_version != '未知版本':
        requirements.append(f"scikit-learn>={sklearn_version}")

    if tf_available and tf_version != '未知版本':
        requirements.append(f"tensorflow>={tf_version}")

    for req in requirements:
        print(req)

    # 写入requirements.txt文件
    with open("requirements.txt", "w", encoding="utf-8") as f:
        for req in requirements:
            f.write(req + "\n")
    print("\n已生成 requirements.txt 文件")

except Exception as e:
    print(f"生成依赖文件时出错: {e}")
    # 提供基本的依赖列表
    basic_requirements = [
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn",
        "scikit-learn",
        "tensorflow"
    ]
    print("基础依赖列表：")
    for req in basic_requirements:
        print(req)