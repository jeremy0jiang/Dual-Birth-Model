#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of Tree Error (RF) vs. various parameters
'''
# imports
from matplotlib import rcParams
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
sns.set_style("ticks")
rcParams['font.family'] = 'serif'

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_data = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
          'RF':np.array([0.897,0.905025,0.92072,0.905995,0.909815,0.88575,0.91898,0.90547,0.91822,0.8837,0.901105,0.93532,0.8977,0.90765,0.915855,0.91843,0.90247,0.91111,0.910415,0.8968] + # r = 0.0001
                        [0.66145,0.667,0.6911,0.6876,0.7166,0.69355,0.70735,0.69375,0.70215,0.6688,0.6801,0.7001,0.7065,0.68185,0.66885,0.7098,0.66965,0.75175,0.70865,0.68265] +            # r = 0.001
                        [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +              # r = 0.01
                        [0.15855,0.16415,0.16615,0.18365,0.1981,0.1724,0.1644,0.1391,0.17215,0.1997,0.18295,0.17725,0.17055,0.1594,0.2023,0.18245,0.1941,0.17,0.18195,0.177] +               # r = 0.1
                        [0.102,0.1193,0.11625,0.10025,0.1028,0.13035,0.1124,0.10325,0.0782,0.0948,0.1223,0.1173,0.1114,0.12385,0.11125,0.11785,0.0995,0.1203,0.12805,0.0998]                 # r = 1
         ).astype(float)}

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_data = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
           'RF':np.array([0.7904,0.8324,0.75215,0.7813,0.85645,0.8054,0.7884,0.7934,0.8074,0.8104,0.8195,0.7864,0.7773,0.7894,0.8023,0.7994,0.7934,0.7702,0.7573,0.8012] +           # r = 0.0001
                         [0.53135,0.56625,0.5725,0.58325,0.6014,0.57525,0.5713,0.5811,0.6106,0.62735,0.64245,0.54615,0.55945,0.5974,0.56325,0.6185,0.56005,0.58875,0.56725,0.5586] + # r = 0.001
                         [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +     # r = 0.01
                         [0.26925,0.28035,0.29195,0.29485,0.289,0.2834,0.2664,0.29245,0.29715,0.30455,0.28255,0.2912,0.2964,0.2895,0.3083,0.3139,0.29035,0.31225,0.28495,0.28515] +  # r = 0.1
                         [0.2575,0.25035,0.28145,0.32125,0.2951,0.30835,0.27525,0.3011,0.26855,0.2879,0.30305,0.28135,0.2904,0.31105,0.267,0.29065,0.30185,0.28325,0.28025,0.257]    # r = 1
          ).astype(float)}

# modifying lambda = lambdaA + lambdaB
l_data = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
          'RF':np.array([0.3631,0.318,0.32665,0.33285,0.3579,0.3499,0.342,0.33565,0.3009,0.3571,0.3089,0.3671,0.34285,0.321,0.3079,0.3159,0.2959,0.322,0.3009,0.32265] +        # lambda = 33.86550309051126
                        [0.331,0.36275,0.31375,0.338,0.3082,0.32075,0.31345,0.2801,0.33665,0.33755,0.36145,0.328,0.3285,0.334,0.31575,0.34255,0.32045,0.35755,0.325,0.3024] +   # lambda = 84.66375772627816
                        [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] + # lambda = 169.32751545255631
                        [0.525,0.5309,0.48125,0.5103,0.4868,0.51635,0.49665,0.5192,0.4519,0.49315,0.4857,0.474,0.4684,0.4994,0.4765,0.50275,0.4598,0.49255,0.49445,0.45015] +   # lambda = 338.65503090511262
                        [0.65965,0.66925,0.6423,0.64885,0.68815,0.651,0.68,0.65045,0.6474,0.69925,0.6665,0.6534,0.6322,0.6666,0.65965,0.6452,0.65705,0.65555,0.67875,0.6755]    # lambda = 846.63757726278155
         ).astype(float)}

# modifying sequence length
k_data = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
          'RF':np.array([0.77405,0.7954,0.7778,0.7763,0.7989,0.78115,0.77405,0.7914,0.72955,0.7962,0.7691,0.79815,0.7902,0.77555,0.7581,0.7583,0.8095,0.7644,0.76895,0.79525] +     # length = 50
                        [0.6435,0.6201,0.64675,0.6294,0.61235,0.6452,0.65055,0.63375,0.63705,0.65075,0.6253,0.64825,0.64485,0.62945,0.67165,0.6381,0.6013,0.6241,0.61605,0.65695] + # length = 100
                        [0.4508,0.4718,0.49245,0.46975,0.45675,0.47835,0.5194,0.4673,0.4594,0.47045,0.46545,0.45465,0.4382,0.4952,0.44265,0.4987,0.49975,0.50905,0.501,0.45685] +   # length = 200
                        [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +     # length = 300
                        [0.2457,0.24585,0.2446,0.24895,0.2743,0.25525,0.2337,0.2051,0.26905,0.24525,0.28045,0.24735,0.2508,0.26545,0.2578,0.26125,0.2223,0.2739,0.2548,0.2594] +    # length = 600
                        [0.1385,0.13835,0.1534,0.1534,0.15855,0.18105,0.1674,0.1634,0.1654,0.1846,0.1694,0.1624,0.16005,0.1671,0.16055,0.15095,0.1714,0.1595,0.1725,0.1625] +       # length = 1200
                        [0.10725,0.10825,0.1063,0.10625,0.0903,0.0943,0.0893,0.0903,0.11225,0.0903,0.0812,0.0832,0.09425,0.0953,0.08525,0.0993,0.0963,0.10425,0.1013,0.0752] +      # length = 2400
                        [0.06215,0.06015,0.0602,0.0572,0.05815,0.06015,0.0632,0.07415,0.07315,0.0461,0.0642,0.0622,0.0682,0.0682,0.0632,0.0622,0.0622,0.05515,0.06115,0.0682]       # length = 4800
             ).astype(float)}

# modifying deviation from ultrametricity
g_data = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
          'RF':np.array([0.41725,0.43145,0.4223,0.41265,0.4316,0.4441,0.42755,0.38405,0.41855,0.4183,0.44405,0.41245,0.4075,0.3714,0.4224,0.4,0.45145,0.4207,0.41735,0.396] +     # gamma = 2.95181735298926
                        [0.4107,0.3961,0.39445,0.39655,0.4254,0.39275,0.42315,0.4045,0.4078,0.4024,0.3673,0.39365,0.39815,0.41175,0.4014,0.45175,0.43045,0.45575,0.3931,0.4191] + # gamma = 5.90363470597852
                        [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +   # gamma = 29.518173529892621
                        [0.3578,0.3814,0.36415,0.331,0.35295,0.41345,0.3951,0.4149,0.3967,0.3804,0.39585,0.398,0.3693,0.4057,0.3632,0.3576,0.38825,0.4029,0.38875,0.3983] +       # gamma = 147.590867649463
                        [0.3605,0.3683,0.38515,0.35425,0.39505,0.3646,0.33185,0.38665,0.39235,0.3704,0.42215,0.3831,0.3638,0.40885,0.36685,0.418,0.34975,0.35415,0.3489,0.3556] + # gamma = 295.181735298926
                        [0.4001,0.37855,0.36955,0.4024,0.37725,0.38615,0.35245,0.3933,0.3942,0.3745,0.38445,0.3762,0.39205,0.37115,0.4006,0.38395,0.38695,0.368,0.38755,0.36195]  # gamma = infinity
             ).astype(float)}

# plot tree error (RF) vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='RF',data=pd.DataFrame(r_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_r_const-exp-branch-length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. r (with constant lambda = lambdaA + lambdaB)
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='RF',data=pd.DataFrame(r2_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_r_const-lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. lambda
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
ax = sns.violinplot(x='lambda',y='RF',data=pd.DataFrame(l_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. length
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
ax = sns.violinplot(x='length',y='RF',data=pd.DataFrame(k_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title('Tree Error (RF) vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. gamma rate
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred')]
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
ax = sns.violinplot(x='gammarate',y='RF',data=pd.DataFrame(g_data),order=x,color='#597DBE')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title('Tree Error (RF) vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_gammarate.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()