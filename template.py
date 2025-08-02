import matplotlib.pyplot as plt
import numpy as np  # 示例数据生成使用

# ================= 全局参数设置 =================
plt.rcParams.update(
    {
        "font.family": "Times New Roman",  # 全局字体
        "font.size": 10,  # 全局字号（除轴标题）
        "axes.labelsize": 12,  # 轴标题字号
        "xtick.labelsize": 10,  # X轴刻度字号
        "ytick.labelsize": 10,  # Y轴刻度字号
        "axes.linewidth": 1.5,  # 坐标轴线宽
        "lines.linewidth": 2,  # 数据线宽
        "legend.fontsize": 10,  # 图例字号
        "legend.frameon": False,  # 关闭图例边框
    }
)

# 定义颜色列表 (16种科学绘图常用色)
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

# 定义线型列表
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

# 设置图片尺寸 (cm×cm)
FIG_SIZE = (8 / 2.54, 8 / 2.54)  # 厘米转英寸 (1英寸=2.54厘米)


# ================= 绘图函数示例 =================
def plot_example():
    # 创建图形和坐标轴
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    # 生成示例数据
    x = np.linspace(0, 10, 100)

    # 绘制多条曲线 (自动循环使用预定义的样式)
    for i in range(6):
        y = np.sin(x + i * 0.5)
        ax.plot(
            x,
            y,
            color=COLOR_LIST[i % len(COLOR_LIST)],
            linestyle=LINE_STYLES[i % len(LINE_STYLES)],
            label=f"Data Series {i+1}",
        )

    # 设置坐标轴标签
    ax.set_xlabel("X Axis Label (unit)", labelpad=5)  # labelpad增加间距
    ax.set_ylabel("Y Axis Label (unit)", labelpad=5)

    # 设置坐标轴范围
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.25, 2)

    # 设置刻度朝向
    ax.tick_params(direction="in", which="both", top=True, right=True)

    # 添加图例
    ax.legend(loc="upper center", ncol=2, columnspacing=0.5)

    # 调整布局
    plt.tight_layout(pad=0.5)

    # 保存图像 (可选格式：PDF, PNG, SVG等)
    plt.savefig("scientific_plot.pdf", dpi=300, bbox_inches="tight")
    plt.savefig("scientific_plot.png", dpi=300, bbox_inches="tight")
    plt.savefig("scientific_plot.svg", bbox_inches="tight")

    plt.show()


# ================= 执行绘图 =================
if __name__ == "__main__":
    plot_example()
