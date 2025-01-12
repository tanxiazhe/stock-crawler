from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from matplotlib.font_manager import FontProperties
if __name__ == "__main__":
    style.use('ggplot')
    dfo=pd.read_excel('../data/bs1.xls',skiprows=1)
    # fig, ax = plt.subplots(figsize=(15,8))
    fig = plt.figure()
    ax = fig.add_subplot(211)
    width=0.3
    df = dfo[dfo['code']=='SH600036']
    df.fillna(0, inplace=True)
    t = df['reportdate']
    a = df['totalassets']
    # ca = df['totalcurrentassets']
    # la = df['totalnoncassets']
    ind = np.arange(len(t))  # the x locations for the groups
    ab=ax.bar(ind, a, width)
    # cab = ax.bar(ind, ca, width)
    # lab = ax.bar(ind, la, width,bottom=ca)
    # b=df['sharrightotal']
    # cl=df['totalcurrliab']
    # ll=df['totalnoncliab']
    l=df['totliab']
    e=df['totsharequi']

    eb = ax.bar(ind + width, e, width, color='y')
    lb = ax.bar(ind + width, l, width, bottom=e, color='b')
    # llb = ax.bar(ind + width, ll, width,bottom=e,color='b')
    # clb = ax.bar(ind + width, cl, width,bottom=e+ll)
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(t)




    # ax2 = fig.add_subplot(212)
    # width=0.3
    # df2 = dfo[dfo['code']=='SH600000']
    # t2 = df2['reportdate']
    # a2 = df2['totalassets']
    # ca2 = df2['totalcurrentassets']
    # la2 = df2['totalnoncassets']
    # ind2 = np.arange(len(t2))  # the x locations for the groups
    # cab2 = ax2.bar(ind2, ca2, width)
    # lab2 = ax2.bar(ind2, la2, width,bottom=ca2)
    # b2=df2['totliabsharequi']
    # cl2=df2['totalcurrliab']
    # ll2=df2['totalnoncliab']
    # l2=df2['totliab']
    # e2=df2['righaggr']
    # eb2 = ax2.bar(ind2 + width, e2, width, color='y')
    # llb2 = ax2.bar(ind2 + width, ll2, width,bottom=e2,color='b')
    # clb2 = ax2.bar(ind2 + width, cl2, width,bottom=e2+ll2)
    #
    #
    # ax.set_xticks(ind + width / 2)
    # ax.set_xticklabels(t)
    plt.show()






# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection='3d')
#
# x3 = [1,2,3,4,5,6,7,8,9,10]
# y3 = [5,6,7,8,2,5,6,3,7,2]
# z3 = np.zeros(10)
#
# dx = np.ones(10)
# dy = np.ones(10)
# dz = [1,2,3,4,5,6,7,8,9,10]
#
# ax1.bar3d(x3, y3, z3, dx, dy, dz)
#
#
# ax1.set_xlabel('x axis')
# ax1.set_ylabel('y axis')
# ax1.set_zlabel('z axis')
#
# plt.show()

