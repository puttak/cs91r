import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


def get_color_map(n, name='hsv'):
    return plt.cm.get_cmap(name, n+1)


def get_legend_handles(legend_labels):
    legend_handles = []
    for l in legend_labels:
        handle = Patch(label=l)
        legend_handles.append(handle)
    return legend_handles


def label_single_bars_above(rects, bar_labels, ax):
    for rect, label in zip(rects, bar_labels):
        x = rect.get_x() + rect.get_width()/2.
        y = rect.get_height()
        ax.annotate("{}".format(label), (x, y), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')


def plot_heatmap(x, y_2D, x_label, y_label, title):
    fig, ax = plt.subplots()
    im = ax.imshow(y_2D, cmap="YlGn")
    threshold = im.norm(np.max(y_2D))/2
    for i in range(y_2D.shape[0]):
        for j in range(y_2D.shape[1]):
            if int(im.norm(y_2D[i][j])) < threshold:
                c = 'k'
            else:
                c = 'w'
            text = ax.text(j, i, y_2D[i][j], ha="center", va="center", color=c)
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_xticks(np.arange(0, y_2D.shape[1], 2))
    ax.set_yticks(np.arange(y_2D.shape[0]))
    ax.set_title(title)
    return fig


def plot_multiple_bar(x, y_all, x_label, y_label, title, w=0.15):
    color_map = get_color_map(y_all.shape[0])
    colors = [color_map(c) for c in np.arange(y_all.shape[0])]
    fig, ax = plt.subplots()
    for i in np.arange(len(y_all)):
        y = y_all[i]
        ax.bar(x+(i*w), y, width=w-0.05, color=colors[i], edgecolor='w')
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_title(title)
    return fig


def plot_multiple_bar_double(x, y_pair_all, x_label, y_label, title, w=0.20):
    color_map = get_color_map(y_pair_all.shape[0])
    colors = [color_map(c) for c in np.arange(y_pair_all.shape[0])]
    fig, ax = plt.subplots()
    for i in np.arange(y_pair_all.shape[0]):
        y_pair = y_pair_all[i]
        ax.bar(x+(i*3/2*w), y_pair[0], width=w/2, color=colors[i], edgecolor='w')
        ax.bar(x+(i*3/2*w)+w/2, y_pair[1], width=w/2, color=colors[i], edgecolor='w', alpha=0.50)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_title(title)
    return fig


def plot_multiple_bar_stacked(x, y_all_v, x_label, y_label, legend_labels, title, w=0.15, percent=False):
    color_map = get_color_map(len(legend_labels))
    colors = [color_map(c) for c in np.arange(y_all_v.shape[1])]
    fig, ax = plt.subplots()
    for i in np.arange(y_all_v.shape[0]):
        y_all = y_all_v[i]
        if percent:
            y_all = y_all / np.sum(y_all, axis=0)
        label0 = (legend_labels[0] if i == 0 else "")
        ax.bar(x+(i*w), y_all[0], width=w-0.05, label=label0, color=colors[0], edgecolor='w')
        for j in np.arange(1, y_all_v.shape[1]):
            y = y_all[j]
            labelj = (legend_labels[j] if i == 0 else "")
            ax.bar(x+(i*w), y, width=w-0.05, bottom=np.sum(y_all[0:j], axis=0), label=labelj, color=colors[j], edgecolor='w')
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.legend(loc='best', )
    ax.set_title(title)
    return fig


def plot_multiple_bar_stacked_double(x, y_pair_all_v, x_label, y_label, legend_labels, title, w=0.20, percent=False):
    color_map = get_color_map(len(legend_labels))
    colors = [color_map(c) for c in np.arange(y_pair_all_v.shape[2])]
    fig, ax = plt.subplots()
    for i in np.arange(y_pair_all_v.shape[0]):
        y0_all = y_pair_all_v[i][0]
        y1_all = y_pair_all_v[i][1]
        if percent:
            y0_all = y0_all / np.sum(y0_all, axis=0)
            y1_all = y1_all / np.sum(y1_all, axis=0)
        label0 = (legend_labels[0] if i == 0 else "")
        ax.bar(x+(i*3/2*w), y0_all[0], width=w/2, label=label0, color=colors[0], edgecolor='w')
        ax.bar(x+(i*3/2*w)+w/2, y1_all[0], width=w/2, label=label0, color=colors[0], edgecolor='w', alpha=0.50)
        for j in np.arange(1, y_pair_all_v.shape[2]):
            y0 = y0_all[j]
            y1 = y1_all[j]
            labelj = (legend_labels[j] if i == 0 else "")
            ax.bar(x+(i*3/2*w), y0, width=w/2, bottom=np.sum(y0_all[0:j], axis=0), label=labelj, color=colors[j], edgecolor='w')
            ax.bar(x+(i*3/2*w)+w/2, y1, width=w/2, bottom=np.sum(y1_all[0:j], axis=0), label=labelj, color=colors[j], edgecolor='w', alpha=0.50)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.legend(loc='best')
    ax.set_title(title)
    return fig


def plot_multiple_line(x, y_all, x_label, y_label, legend_labels, title, scalar=None):
    color_map = get_color_map(len(legend_labels))
    colors = [color_map(c) for c in np.arange(y_all.shape[0])]
    fig, ax = plt.subplots()
    for i in np.arange(y_all.shape[0]):
        ax.plot(x, y_all[i], color=colors[i], label=legend_labels[i])
    if scalar:
        ax.axhline(y=scalar, color='k', linewidth=2)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.legend(loc='best')
    ax.set_title(title)
    return fig


def plot_single_bar(x, y, x_label, y_label, title, w=0.30, bar_labels=None):
    fig, ax = plt.subplots()
    ax.bar(x, y, width=w, color='b', edgecolor='w')
    if bar_labels is not None:
        label_single_bars_above(ax.patches, bar_labels, ax)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_title(title)
    return fig


def plot_single_bar_double(x, y_pair, x_label, y_label, title, w=0.30, bar_labels=None):
    fig, ax = plt.subplots()
    ax.bar(x, y_pair[0], width=w/2, color='b', edgecolor='w')
    ax.bar(x+w/2, y_pair[1], width=w/2, color='b', edgecolor='w', alpha=0.50)
    if bar_labels is not None:
        label_single_bars_above(ax.patches, bar_labels, ax)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_title(title)
    return fig


def plot_single_bar_double_with_line(x, y_bar, y_line, x_label, y_bar_label, y_line_label, title, w=0.30):
    fig, ax = plt.subplots()
    ax.bar(x, y_bar[0], width=w, color='g', edgecolor='w')
    ax.bar(x+w/2, y_bar[1], width=w/2, color='g', edgecolor='w', alpha=0.50)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_bar_label)
    axT = ax.twinx()
    axT.plot(x, y_line, color='b')
    axT.set_ylabel(y_line_label)
    ax.set_title(title)
    return fig


def plot_single_bar_stacked(x, y_all, x_label, y_label, legend_labels, title, w=0.30, percent=False):
    color_map = get_color_map(len(legend_labels))
    colors = [color_map(c) for c in np.arange(len(y_all))]
    fig, ax = plt.subplots()
    if percent:
        y_all = y_all / np.sum(y_all, axis=0)
    ax.bar(x, y_all[0], width=w, label=legend_labels[0], color=colors[0], edgecolor='w')
    for i in np.arange(1, len(y_all)):
        y = y_all[i]
        ax.bar(x, y, width=w, bottom=np.sum(y_all[0:i], axis=0), label=legend_labels[i], color=colors[i], edgecolor='w')
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.legend(loc='best')
    ax.set_title(title)
    return fig


def plot_single_bar_stacked_double(x, y_pair_all, x_label, y_label, legend_labels, title, w=0.30, percent=False):
    color_map = get_color_map(len(legend_labels))
    colors = [color_map(c) for c in np.arange(len(y_pair_all[0]))]
    fig, ax = plt.subplots()
    y0_all = y_pair_all[0]
    y1_all = y_pair_all[1]
    if percent:
        y0_all = y0_all / np.sum(y0_all, axis=0)
        y1_all = y1_all / np.sum(y1_all, axis=0)
    ax.bar(x, y0_all[0], width=w/2, label=legend_labels[0], color=colors[0], edgecolor='w')
    ax.bar(x+w/2, y1_all[0], width=w/2, label=legend_labels[0], color=colors[0], edgecolor='w', alpha=0.50)
    for i in np.arange(1, len(y_pair_all[0])):
        ax.bar(x, y0_all[i], width=w/2, bottom=np.sum(y0_all[0:i], axis=0), label=legend_labels[i], color=colors[i], edgecolor='w')
        ax.bar(x+w/2, y1_all[i], width=w/2, bottom=np.sum(y1_all[0:i], axis=0), label=legend_labels[i], color=colors[i], edgecolor='w', alpha=0.50)
    ax.grid(axis='y')
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.legend(loc='best')
    ax.set_title(title)
    return fig
