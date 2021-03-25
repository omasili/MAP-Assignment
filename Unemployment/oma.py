# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:44:58 2021

@author: User
"""


from matplotlib import pyplot as plt


dev_y=[570609,523719,1144399,296325,555407,287671,617938,224583,618484,1005848,194868,376734,188386,585568,442478,1209882,442495,1339952,1424686,650682,245697,677097,186163,1329490,165232,707559,362720,440389,295590,521216,645166,1714189,216339,532520,298563,209978,515996]
dev_x=['ABIA','ADAMAWA','AKWA-IBOM','ANAMBRA','BAUCHI','BAYELSA','BENUE','BORNO','CROSS RIVER','DELTA','EBONYI','EDO','EKITI','ENUGU','GOMBE','IMO','JIGAWA','KADUNA','KANO','KATSINA','KEBBI','KOGI','KWARA','LAGOS','NASARAWA','NIGER','OGUN','ONDO','OSUN','OYO','PLATEAU','RIVERS','SOKOTO','TARABA','YOBE','ZAMFARA','FCT']
plt.figure(figsize=(9,9))
plt.barh(dev_x,dev_y)


#plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('Unemployment Graph Statistics for States in Nigeria')
plt.xlabel('Total Unemployment')
plt.ylabel('States')
plt.show()
