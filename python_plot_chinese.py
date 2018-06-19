#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:25:12 2018

@author: zino
"""


# don't you .ttc font file in windows. please use ttf in matplotlib.

# note need to remove: ~/.cache/matplotlib

#find  matplotlib default font
from matplotlib.font_manager import findfont, FontProperties  
findfont(FontProperties(family=FontProperties().get_family())) 

#find matplotlibrc path
import matplotlib 
matplotlib.matplotlib_fname()


# see default font name
import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif']

# plt   use by setting
import matplotlib.pyplot as plt 
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']  
plt.rcParams['axes.unicode_minus'] = False 
plt.plot((1,2,3),(4,3,1)) 
plt.title("聲量圖") 
plt.ylabel("文章數量") 
plt.xlabel("時間")  
plt.show()

# plt 
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt 
myfont = FontProperties(fname=r'/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc')
plt.plot((1,2,3),(4,3,1)) 
plt.title("聲量圖",fontproperties=myfont) 
plt.ylabel("文章數量",fontproperties=myfont) 
plt.xlabel("時間",fontproperties=myfont)  
plt.show()

#no way can drictly set font path witout fontproperties 

# seaborn 
from matplotlib.font_manager import FontProperties
import seaborn as sns
myfont=FontProperties(fname=r'/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc',size=14)
sns.set(font=myfont.get_family())
sns.set_style("darkgrid",{"font.sans-serif":['Noto Sans CJK JP']})
cities_counter = [('上海', 285), ('杭州', 225), ('北京', 163), ('广州', 136), ('南京', 130), ('武汉', 124), ('深圳', 88), ('温州', 67), ('苏州', 66), ('宁波', 45)] 
sns.set_color_codes("pastel") 
sns.barplot(x=[k for k, _ in cities_counter[:10]], y=[v for _, v in cities_counter[:10]])

