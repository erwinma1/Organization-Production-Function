'''
Production Function Model for Service Organization
Useful Sources:
Construct F(L): https://mbounthavong.com/blog/tag/Cobb-Douglas+production+function
SciKitLearn: https://www.w3schools.com/python/python_ml_multiple_regression.asp
Statsmodel https://www.statology.org/sklearn-linear-regression-summary/
'''

import pandas as pd
import numpy as np
import openpyxl as os
from scipy import stats
import statsmodels.api as sm
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = pd.read_excel('file_path')

template = pd.read_excel('file_path')

write_path = ('file_path')

###############################################################
######################### Format data #########################
###############################################################
print('Transforming data...')

#Transform to Natural Log
data['lnStaff'] = np.log(data['TE_Staff'])
data['lnOPSC'] = np.log(data['OPSC'])
data['lnOutput'] = np.log(data['Output'])


###############################################################
########################## Run ANOVA ##########################
###############################################################
print('Running regression...')
'''
for multiple regression use sklearn
regr = linear_model.LinearRegression()
regr.fit(data['lnStaff'], data['lnOutput'])
'''

slope, intercept, r, p, std_err = stats.linregress(data['lnStaff'], data['lnOutput'])
print('results:')
print('beta = ' + str(float(slope)))
print('intercept = ' + str(float(intercept)))
print('correl = ' + str(float(r)))
print('p-value = ' + str(float(p)))
print('std error = ' + str(float(std_err)))

######################################################################
#################### Fit to ANOVA Production Model ###################
######################################################################
print('Fitting ANOVA Model...')

#Fit the Model to Cobb-douglas log form
template['Log_Y'] = intercept + slope * template['Log_L']

#Calculate point elasticity of log model
template['Output_Elasticity'] = (template['Log_Y']-template['Log_Y'].shift(1))/(template['Log_L']-template['Log_L'].shift(1))

#convert to USD
template['Labor_$'] = np.exp(template['Log_L'])
template['Output_$'] = np.exp(template['Log_Y'])

#Calculate converted elasticity to $ Amount
template['Output_Elasticity_$'] = ((template['Output_$']-template['Output_$'].shift(1))/template['Output_$'].shift(1))/((template['Labor_$']-template['Labor_$'].shift(1))/template['Labor_$'].shift(1))

######################################################################
###################### Writing Fitted Model Data #####################
######################################################################

#template.to_excel(write_path)

print('Model Paramaters Printed!')

######################################################################
####################### Plot Level Model Data ######################
######################################################################

model = pd.DataFrame(data=template, columns=['Output_$','Labor_$'])

ax = model.plot(kind='line',
           x='Labor_$',
           y='Output_$',
           figsize=(10,6),
           linewidth=0.75
           )

ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000000:.0f}'))
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y/1000000:.2f}'))

plt.title("Labor Production Model: F(L)", fontsize=14, fontweight='bold')
plt.xlabel('Staff_Budget (millions)', fontsize=12)
plt.ylabel('Program_Output (millions)', fontsize=12)
plt.grid(True)
plt.show()

'''
#######################################################################
########################## Get Point Estimate #########################
#######################################################################
print('you can get a point estimate in this section')

print('what is your labor cost?')
input_L = np.log(float(str((input()))))

get_Y = np.exp(intercept + slope * input_L)

print('your predicted output is $' + str(float(get_Y)))

################### Part 2
print('what is your program spend (output)?')

input_Y = np.log(float(str((input()))))
get_L =  np.exp(scalar_x*(input_Y/intercept)**(1/slope))

print('your predicted staff costs is $' + str(float(get_L)))

'''
