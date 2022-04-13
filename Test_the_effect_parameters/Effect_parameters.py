# coding=utf-8
"""
Author: Shuaijie
Blog: https://blog.csdn.net/weixin_45452300
公众号：AgbioIT
date: 2022/4/13 9:43
desc: 
"""


import pandas as pd
import numpy as np
import os
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from xml.dom.minidom import parse
import paramchange as pc


workspace = r'E:\WUQIAOmaizeSA'
model_files = r'E:\JavaSTICS-1.41-stics-9.1'
usm = 'WM_T_M2017'
# 读取原始作物文件和土壤文件
plant_DOMTree = parse(os.path.join(model_files, r'plant\cornnew_plt.xml')) #读取文件为树
origin_plant = plant_DOMTree.documentElement
soil_DOMTree = parse(os.path.join(workspace, 'sols.xml'))
origin_siol = soil_DOMTree.documentElement

# parameters range
udlaimax_range = np.arange(28, 36, 1)
# build figures
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
# change parameter
for udlaimax in udlaimax_range:
    # change param
    pc.parset('temax', udlaimax, os.path.join(model_files, r'plant\cornnew_plt.xml'))
    # run model
    os.chdir(model_files)
    os.system(r'JavaSticsCmd.exe %s %s %s' % ('--run', workspace, usm))
    # plot
    file_dir = workspace
    output = pd.read_csv(os.path.join(file_dir, 'mod_s%s.sti' % usm), sep=';', index_col=False)
    output['date'] = [dt.date(output['ian'][i], output['mo'][i], output['jo'][i]) for i in range(len(output))]
    for var, ax in zip(["lai(n)", "masec(n)", "mafruit", "QNplante"], axes.flatten()):
        ax.plot_date(output.date, output[var], '-', label='temax=%.1f'%udlaimax)
        ax.set_title(var)
        ax.legend()
    fig.autofmt_xdate()
# 恢复默认参数
with open(os.path.join(model_files, r'plant\cornnew_plt.xml'), 'w') as f:
    origin_plant.writexml(f)
with open(os.path.join(workspace, 'sols.xml'), 'w') as f:
    origin_siol.writexml(f)
plt.show()