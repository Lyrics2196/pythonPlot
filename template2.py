import matplotlib.pyplot as plt
import numpy as np

# ======================
# 全局参数设置
# ======================
plt.rcParams.update(
    {
        # 字体设置
        "font.family": "serif",
        "font.serif": ["Times New Roman"],
        "font.size": 10,  # 基础字号 (10pt)
        # 坐标轴设置
        "axes.titlesize": 12,  # 轴标题字号 (12pt)
        "axes.labelsize": 12,  # 轴标签字号 (12pt)
        "xtick.labelsize": 10,  # X轴刻度字号 (10pt)
        "ytick.labelsize": 10,  # Y轴刻度字号 (10pt)
        "axes.linewidth": 1.5,  # 坐标轴线宽 (1.5pt)
        # 图例设置
        "legend.fontsize": 10,  # 图例字号 (10pt)
        "legend.frameon": False,  # 关闭图例边框
        # 线条设置
        "lines.linewidth": 2,  # 数据线宽 (2pt)
        "lines.markersize": 6,  # 标记大小
        # 刻度设置
        "xtick.direction": "in",  # 刻度朝内
        "ytick.direction": "in",  # 刻度朝内
        "xtick.major.width": 1.5,  # 刻度线宽
        "ytick.major.width": 1.5,  # 刻度线宽
        # 图形保存设置
        "savefig.dpi": 300,  # 输出分辨率
        "savefig.transparent": False,  # 是否透明背景
        "savefig.format": "pdf",  # 默认保存格式
        "savefig.bbox": "tight",
    }
)

# ======================
# 预定义样式
# ======================
# 颜色列表 (Tableau 10色系)
COLOR_LIST = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
    "#aec7e8",
    "#ffbb78",
    "#98df8a",
    "#ff9896",
    "#c5b0d5",
    "#c49c94",
]

# 线型列表
LINE_STYLES = [
    "-",  # 实线
    "--",  # 虚线
    "-.",  # 点划线
    ":",  # 点线
    (0, (3, 1, 1, 1)),  # 自定义点划线
    (0, (5, 5)),  # 长虚线
    (0, (1, 5)),  # 稀疏虚线
    (0, (5, 1)),  # 密集虚线
]

# 标记样式
MARKER_STYLES = ["o", "s", "^", "D", "v", "<", ">", "p", "*", "h"]


# ======================
# 绘图函数模板
# ======================
def create_figure(width_cm=8, aspect_ratio=4 / 3):
    """
    创建符合规范的绘图画布

    参数:
    width_cm : 图形宽度 (厘米)
    aspect_ratio : 宽高比 (默认4:3)
    """
    # 单位转换: cm -> 英寸
    width_inch = width_cm / 2.54
    height_inch = width_inch / aspect_ratio

    fig, ax = plt.subplots(figsize=(width_inch, height_inch))
    return fig, ax


# ======================
# 使用示例
# ======================
if __name__ == "__main__":
    # 创建画布 (8cm宽，4:3比例)
    fig, ax = create_figure(width_cm=8, aspect_ratio=4 / 3)

    # 生成示例数据
    x = np.linspace(0, 10, 100)
    y_data = [np.sin(x) * i for i in range(1, 5)]

    # 绘制多条曲线
    for i, y in enumerate(y_data):
        ax.plot(
            x,
            y,
            color=COLOR_LIST[i % len(COLOR_LIST)],
            linestyle=LINE_STYLES[i % len(LINE_STYLES)],
            linewidth=2,  # 数据线宽 (2pt)
            label=f"Dataset {i+1}",
        )

    # 设置坐标轴标签
    ax.set_xlabel("X Axis Label (units)")
    ax.set_ylabel("Y Axis Label (units)")

    # 设置标题
    # ax.set_title("Research Plot Template")

    # 添加图例
    ax.legend(ncol=2, columnspacing=0.5, loc="upper center")

    # 网格线 (使用1pt细线)
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

    # 调整布局
    plt.tight_layout()

    # 保存图形 (支持多种格式)
    plt.savefig("research_plot.png", dpi=300)
    plt.savefig("research_plot.pdf")  # 推荐矢量格式

    # 显示图形
    plt.show()
