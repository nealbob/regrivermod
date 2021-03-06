from chartbuilder import *
import numpy as np
import pandas
import pylab
import pickle
from sklearn.ensemble import ExtraTreesClassifier as Tree_classifier
from sklearn.ensemble import ExtraTreesRegressor as Tree

def removekeys(d, keys):
    r = dict(d)
    for key in keys:
        del r[key]
    return r 

def build(results):

    zzz = 0


def main(result = 0, sens = 0):

    """
        Generate charts for report
    """

    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter5/'
    out = '/Dropbox/Thesis/IMG/chapter5/'
    img_ext = '.pdf'

    scen = ['CS', 'SWA', 'OA', 'NS']
    
    if result == 0:
        with open(home + folder + '0_0_result.pkl', 'rb') as f:
            result = pickle.load(f)
            f.close()
    
    data0 = []
    n = result['CS']['VE'][sens].shape[0]
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = max(result[sr]['VE'][sens][i][0], 0.0005)
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'VE_low' + img_ext,
     'YLABEL': 'Value function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    data0 = []

    n = result['CS']['VE'][sens].shape[0]
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = max(result[sr]['VE'][sens][i][1], 0.0005)
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'VE_high' + img_ext,
     'YLABEL': 'Value function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    data0 = []
    n = result['CS']['PE'][sens].shape[0]
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = result[sr]['PE'][sens][i][0]
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'PE_low' + img_ext,
     'YLABEL': 'Policy function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    data0 = []
    
    n = result['CS']['PE'][sens].shape[0]
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = result[sr]['PE'][sens][i][1]
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'PE_high' + img_ext,
     'YLABEL': 'Policy function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    
    data0 = []
    n = result['CS']['stats'][sens]['SW'].shape[0] - 1
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = result[sr]['stats'][sens]['S'][i]['Mean'] / 1000
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Storage' + img_ext,
     'YLABEL': 'Mean storage $S_t$ (GL)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    
    data0 = []
    n = result['CS']['stats'][sens]['S'].shape[0] - 1
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = result[sr]['stats'][sens]['S'][i]['Mean'] / 1000 - result[sr]['stats'][sens]['W'][i]['Mean'] / 1000
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Reserve' + img_ext,
     'YLABEL': 'Mean storage reserve $S_t - W_t$ (GL)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    data0 = []
    n = result['CS']['stats'][sens]['P'].shape[0] - 1
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = result[sr]['stats'][sens]['P'][i]['Mean'] 
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Price' + img_ext,
     'YLABEL': 'Mean water price $P_t$ (\\$ per ML)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    data0 = []
    for i in range(n):
        record = {}
        for sr in scen:
            record[sr] = result[sr]['stats'][sens]['SW'][i]['Mean'] / 1000000
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Welfare' + img_ext,
     'YLABEL': 'Mean social welfare $\\sum_{i=1}^n u_{it}$ (\\$M)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')

    n = result['CS']['stats'][sens]['S'].shape[0] - 2
    pol_low = np.zeros(4)
    i = 0
    for sr in ['CS','SWA', 'OA','NS']:
        pol_low[i] = result[sr]['stats'][sens]['W_low'][n]['Mean'] / result[sr]['stats'][sens]['S_low'][n]['Mean']
        i += 1

    pol_high = np.zeros(4)
    i = 0
    for sr in ['CS', 'SWA', 'OA', 'NS']:
        pol_high[i] = result[sr]['stats'][sens]['W_high'][n]['Mean'] / result[sr]['stats'][sens]['S_high'][n]['Mean']
        i += 1

    chart = {'OUTFILE': home + out + 'user' + img_ext,
     'YLABEL': 'Mean withdrawal over mean storage',
     'XLABEL': 'Policy scenario',
     'LABELS': ('', 'CS', '', 'SWA', '', 'OA', '', 'NS'),
     'LEGEND': ('Low reliability', 'High reliability'),
     'WIDTH': 0.3}
    data = [[np.arange(4), pol_low], [np.arange(4) + chart['WIDTH'], pol_high]]
    build_chart(chart, data, chart_type='bar')
    pol_low = np.zeros(4)
    i = 0
    for sr in ['CS', 'SWA', 'OA','NS']:
        pol_low[i] = (result[sr]['stats'][sens]['X_low'][n]['Mean'] ) / result['CS']['stats'][sens]['S_low'][n]['Max']
        i += 1

    pol_high = np.zeros(4)
    i = 0
    for sr in ['CS', 'SWA', 'OA', 'NS']:
        pol_high[i] = (result[sr]['stats'][sens]['X_high'][n]['Mean']) / result['CS']['stats'][sens]['S_high'][n]['Max']
        i += 1

    chart = {'OUTFILE': home + out + 'x_share' + img_ext,
     'YLABEL': 'Mean externality over mean storage',
     'XLABEL': 'Policy scenario',
     'LABELS': ('', 'CS', '', 'SWA', '', 'OA', '', 'NS'),
     'LEGEND': ('Low reliability', 'High reliability'),
     'WIDTH': 0.3}
    data = [[np.arange(4), pol_low], [np.arange(4) + chart['WIDTH'], pol_high]]
    build_chart(chart, data, chart_type='bar')



def build_loss(lossresult, result, sens = 2):
    """
        Generate charts and tables for report

    """
    home = '/home/nealbob'
    out = '/Dropbox/Thesis/IMG/chapter5/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter5/'
    srlist = ['CS', 'SWA']
    
    """
    data0 = []
    n = result['CS']['VE'][sens].shape[0]
    for i in range(50, n):
        record = {}
        for sr in srlist:
            record[sr + '-LD'] = result[sr]['VE'][sens][i][0]
        for sr in srlist:
            record[sr + '-SL'] = lossresult[sr]['VE'][sens][i][0]
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_VE_low' + img_ext,
     'YLABEL': 'Value function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    data0 = []
    n = result['CS']['VE'][sens].shape[0]
    for i in range(50, n):
        record = {}
        for sr in srlist:
            record[sr + '-LD'] = result[sr]['VE'][sens][i][1]

        for sr in srlist:
            record[sr + '-SL'] = lossresult[sr]['VE'][sens][i][1]
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_VE_high' + img_ext,
     'YLABEL': 'Value function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')

    data0 = []
    n = result['CS']['PE'][sens].shape[0]
    for i in range(50, n):
        record = {}
        for sr in srlist:
            record[sr + '-LD'] = abs(result[sr]['PE'][sens][i][0])
        for sr in srlist:
            record[sr + '-SL'] = abs(lossresult[sr]['PE'][sens][i][0])
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_PE_low' + img_ext,
     'YLABEL': 'Policy function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')

    data0 = []
    n = result['CS']['PE'][sens].shape[0]
    for i in range(50, n):
        record = {}
        for sr in srlist:
            record[sr + '-LD'] = abs(result[sr]['PE'][sens][i][1])
        for sr in srlist:
            record[sr + '-SL'] = abs(lossresult[sr]['PE'][sens][i][1])
        data0.append(record)
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_PE_high' + img_ext,
     'YLABEL': 'Policy function error',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    """

    data0 = []
    n = result['CS']['stats'][sens]['SW'].shape[0]
    for i in range(n):
        record = {}
        for sr in srlist:
            record[sr + '-SL'] = lossresult[sr]['stats'][sens]['S'][i]['Mean'] / 1000

        for sr in srlist:
            record[sr + '-LD'] = result[sr]['stats'][sens]['S'][i]['Mean'] / 1000

        data0.append(record)

    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_Storage' + img_ext,
     'YLABEL': 'Mean storage $S_t$ (GL)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    data0 = []
    n = result['CS']['stats'][sens]['S'].shape[0]
    for i in range(n):
        record = {}
        for sr in srlist:
            record[sr + '-LD'] = result[sr]['stats'][sens]['S'][i]['Mean'] / 1000 - result[sr]['stats'][sens]['W'][i]['Mean'] / 1000

        for sr in srlist:
            record[sr + '-SL'] = lossresult[sr]['stats'][sens]['S'][i]['Mean'] / 1000 - lossresult[sr]['stats'][sens]['W'][i]['Mean'] / 1000

        data0.append(record)

    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_Reserve' + img_ext,
     'YLABEL': 'Mean storage reserve $S_t - W_t$ (GL)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    data0 = []
    for i in range(n):
        record = {}
        for sr in srlist:
            record[sr + '-LD'] = result[sr]['stats'][sens]['SW'][i]['Mean'] / 1000000

        for sr in srlist:
            record[sr + '-SL'] = lossresult[sr]['stats'][sens]['SW'][i]['Mean'] / 1000000

        data0.append(record)

    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + 'Loss_Welfare' + img_ext,
     'YLABEL': 'Mean social welfare $\\sum_{i=1}^n u_{it}$ (\\$M)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')


def tables(result = 0, sens = 0, scen = ['CS', 'CS-SL', 'SWA', 'SWA-SL', 'OA', 'NS']):
    
    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter5/'
    table_out = '/Dropbox/Thesis/STATS/chapter5/'
    
    if result == 0:
        with open(home + folder + '0_0_result.pkl', 'rb') as f:
            result = pickle.load(f)
            f.close()
    
    series = ['S', 'SW', 'W', 'Z', 'U_low', 'U_high', 'X_low', 'X_high']
    stats = ['Mean', 'SD', '25th', '75th', '2.5th','97.5th']
    n = result['CS']['stats'][sens]['S'].shape[0] - 1
    print result['CS']['stats'][0]['S'][(n - 1)]['Mean']
    
    adj = 0
    for x in series:
        if x == 'SW' or x == 'U_low' or x == 'U_high':
            scale = 1000000
            adj = 0
        elif x == 'Z':
            scale = 1000
            adj = 0
        elif x == 'X_low' or x == 'X_high':
            scale = 0.01
            adj = 0
        else:
            scale = 1000
            adj = 0
        data0 = []
        for sr in scen:
            record = {}
            for stat in stats:
                if x == 'X_low':
                    record[stat] = result[sr]['stats'][sens][x][(n - 1)][stat] / result[sr]['stats'][sens]['S_low'][(n - 1)][stat] / scale
                elif x == 'X_high':
                    record[stat] = result[sr]['stats'][sens][x][(n - 1)][stat] / result[sr]['stats'][sens]['S_high'][(n - 1)][stat] / scale
                else:
                    record[stat] = result[sr]['stats'][sens][x][(n - 1)][stat] / scale + adj

            data0.append(record)

        record = {}
        for stat in stats:
            record[stat] = result['CS']['stats'][sens][x][0][stat] / scale

        data0.append(record)
        tab = pandas.DataFrame(data0)
        temp = [ sr for sr in scen ]
        temp.append('Planner')
        tab.index = temp
        with open(home + table_out + x + '_table.txt', 'w') as f:
            f.write(tab.to_latex(float_format='{:,.1f}'.format, columns=['Mean',
             'SD', '2.5th', '25th', '75th', '97.5th'], escape=False))
            f.close()

def notrade_tables(result = 0, sens = 0, scen = ['CS', 'SWA',  'OA', 'NS', 'CS-SL', 'SWA-SL', 'CS-SWA']):
    
    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter5/'
    table_out = '/Dropbox/Thesis/STATS/chapter5/'
    out = '/Dropbox/Thesis/IMG/chapter5/'
    
    if result == 0:
        with open(home + folder + '0_result_notrade.pkl', 'rb') as f:
            result = pickle.load(f)
            f.close()
    
    series = ['S', 'SW', 'W', 'Z', 'U_low', 'U_high', 'X_low', 'X_high']
    stats = ['Mean', 'SD', '25th', '75th', '2.5th','97.5th']
    n = result['CS']['stats'][sens]['S'].shape[0] - 1
    print result['CS']['stats'][0]['S'][(n - 1)]['Mean']
    
    adj = 0
    for x in series:
        if x == 'SW' or x == 'U_low' or x == 'U_high':
            scale = 1000000
            adj = 0
        elif x == 'Z':
            scale = 1000
            adj = 0
        elif x == 'X_low' or x == 'X_high':
            scale = 0.01
            adj = 0
        else:
            scale = 1000
            adj = 0
        data0 = []
        for sr in scen:
            record = {}
            for stat in stats:
                if x == 'X_low':
                    record[stat] = result[sr]['stats'][sens][x][(n - 1)][stat] / result[sr]['stats'][sens]['S_low'][(n - 1)][stat] / scale
                elif x == 'X_high':
                    record[stat] = result[sr]['stats'][sens][x][(n - 1)][stat] / result[sr]['stats'][sens]['S_high'][(n - 1)][stat] / scale
                else:
                    record[stat] = result[sr]['stats'][sens][x][(n - 1)][stat] / scale + adj

            data0.append(record)

        record = {}
        for stat in stats:
            record[stat] = result['CS']['stats'][sens][x][0][stat] / scale

        data0.append(record)
        tab = pandas.DataFrame(data0)
        temp = [ sr for sr in scen ]
        temp.append('Planner')
        tab.index = temp
        with open(home + table_out + x + '_notrade_table.txt', 'w') as f:
            f.write(tab.to_latex(float_format='{:,.1f}'.format, columns=['Mean',
             'SD', '2.5th', '25th', '75th', '97.5th'], escape=False))
            f.close()

    notrade = np.array([182.1, 182.6, 180.8, 173.7, 182.7, 183.2, 182.5])  
    trade = np.array([185.3, 185.3, 182.7, 182.0, 185.5, 185.2, 185.4])
    gain = trade - notrade
    labels = scen
    chart_params()
    
    width = 0.5
    pylab.bar(np.arange(7), gain, width)
    pylab.xticks(np.arange(7) + width, scen)
    pylab.xlabel('Scenario')
    pylab.ylabel('Gain from trade, (\$M)')
    pylab.savefig(home + out + 'tradegain.pdf', bbox_inches='tight')
    pylab.show()

def policy_chart(policies):
    home = '/home/nealbob'
    out = '/Dropbox/Thesis/IMG/chapter5/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter5/'
    X = np.arange(0, 1025000.0, 25000).reshape(41, 1)
    data0 = []
    for i in range(41):
        record = {}
        for sr in ['CS', 'SWA', 'OA', 'NS']:
            record[sr] = policies[sr][0][1].predict(X)[i] / 1000

        record['Planner'] = policies[sr][0][0].predict(X)[i] / 1000
        data0.append(record)

    data = pandas.DataFrame(data0)
    data.index = X.ravel() / 1000
    chart = {'OUTFILE': home + out + 'Policy' + img_ext,
     'YLABEL': 'Mean withdrawal $W_t$ (GL)',
     'XLABEL': 'Mean storage $S_t$ (GL)'}
    build_chart(chart, data, chart_type='date')

"""
def inflow_share(n = 10):
    home = '/home/nealbob'
    out = '/Dropbox/Thesis/IMG/chapter5/sens/'
    img_ext = '.pdf'
    srlist = ['CS', 'SWA', 'OA', 'NS']
    n = n
    results = []
    for j in range(n):
        f = open(str(j) + '_result_sens.pkl', 'rb')
        results.append(pickle.load(f))
        f.close()

    data0 = []
    n2 = results[0]['CS']['stats'][2]['SW'].shape[0] - 1
    tablist = []
    for i in range(n):
        data0 = []
        for k in range(5):
            record = {}
            for sr in srlist:
                record[sr] = results[i][sr]['stats'][k]['SW'][n2]['Mean'] / 1000000

            data0.append(record)

        data = pandas.DataFrame(data0)
        tablist.append(data0)

    maxk_list = []
    for i in range(n):
        for k in range(5):
            maxk = -1
            sw_max = -1000000000
            for sr in ['CS', 'SWA', 'OA', 'NS']:
                if tablist[i][k][sr] > sw_max:
                    sw_max = tablist[i][k][sr]
                    maxk = sr

            maxk_list.append(maxk)


    data1 = []
    for i in range(n):
        record = []
        for sr in ['SWA', 'OA', 'NS']:
            array = np.zeros(5)
            for k in range(5):
                array[k] = tablist[i][k][sr] / tablist[i][k]['CS']

            data1.append(array)


    fig_width_pt = 600
    inches_per_pt = 1.0 / 72.27
    golden_mean = 1.2360679774997898 / 2.0
    fig_width = fig_width_pt * inches_per_pt
    fig_height = fig_width * golden_mean * 2
    fig_size = [fig_width, fig_height]
    params = {'backend': 'ps',
     'axes.labelsize': 10,
     'text.fontsize': 10,
     'legend.fontsize': 10,
     'xtick.labelsize': 8,
     'ytick.labelsize': 8,
     'text.usetex': True,
     'figure.figsize': fig_size}
    pylab.rcParams.update(params)
    fig = pylab.figure()
    for i in range(n):
        n2 = results[i]['CS']['stats'][0]['SW'].shape[0]
        data0 = []
        for k in range(5):
            record = {}
            for sr in ['CS', 'SWA', 'OA', 'NS']:
                record[sr] = results[i][sr]['stats'][k]['SW'][(n2 - 1)]['Mean'] / 1000000

            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = np.array([0.3, 0.35, 0.4, 0.45, 0.5])
        chart = {'OUTFILE': home + out + 'Lambda' + img_ext,
         'XLABEL': 'Inflow share $\\Lambda_{high}$',
         'YLABEL': 'Mean social welfare $\\sum_{i=1}^n u_{it}$ (\\$M)'}
        fig = pylab.subplot(n / 2, 2, i + 1)
        for sr in srlist:
            pylab.plot(data.index, data[sr], label=sr)

        setFigLinesBW(fig)

    pylab.legend()
    pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)
    pylab.legend(loc='upper center', bbox_to_anchor=(-0.2, 3.55), ncol=4, fancybox=True)
    pylab.show()
    return [maxk_list, data1]
"""


def sens(n = 20, m=10):
    
    home = '/home/nealbob'
    infolder = '/Dropbox/Model/results/chapter5/sens/chapter5/'
    out = '/Dropbox/Thesis/IMG/chapter5/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter5/'
    srlist = ['CS', 'SWA', 'OA', 'NS']

    results = []
    for j in range(1, n):
        for k in range(m):
            try:
                f = open(home + infolder + str(j) + '_' + str(k) + '_result.pkl', 'rb')
                results.append(pickle.load(f))
                f.close()
            except:
                print 'FAIL! job number: ' + str(j) + ' , run number: ' + str(k)
                pass
   
    

    nfull = len(results)
    delidx = []
    for i in range(nfull):
        n2 = results[i]['CS']['stats'][0]['SW'].shape[0] - 2
        if (results[i]['OA']['stats'][0]['W']['Mean'][n2] / results[i]['CS']['stats'][0]['W']['Mean'][n2]) < 0.5 and results[i]['OA']['paras'][0]['LL'] < 3500:
            delidx.append(i)
        if (results[i]['OA']['stats'][0]['SW']['Mean'][n2] / results[i]['CS']['stats'][0]['SW']['Mean'][n2]) < 0.5 and results[i]['OA']['paras'][0]['LL'] < 4000:
            delidx.append(i)
        if results[i]['CS']['stats'][0]['SW']['Mean'][n2] == float('Inf') or results[i]['SWA']['stats'][0]['SW']['Mean'][n2] == float('Inf') or results[i]['OA']['stats'][0]['SW']['Mean'][n2] == float('Inf') or results[i]['NS']['stats'][0]['SW']['Mean'][n2] == float('Inf'):
            delidx.append(i)
        if results[i]['CS']['stats'][0]['SW']['Mean'][0] == float('Inf') or results[i]['SWA']['stats'][0]['SW']['Mean'][0] == float('Inf') or results[i]['OA']['stats'][0]['SW']['Mean'][0] == float('Inf') or results[i]['NS']['stats'][0]['SW']['Mean'][0] == float('Inf'):
            delidx.append(i)

    results = [i for j, i in enumerate(results) if j not in delidx]
    n = len(results)
    print str(n) + ' good results of ' + str(nfull) + ' total runs.'
     
    data0 = []
    SW = {}
    for sr in srlist:
        array = np.zeros(n)
        for i in range(n):
            n2 = results[0]['CS']['stats'][0]['SW'].shape[0] - 2
            #if n2 == 21:
            array[i] = results[i][sr]['stats'][0]['SW'][n2]['Mean'] / 1000000

        SW[sr] = np.round(array, 2)

    SWmax = []
    for i in range(n):
        SWm = -1
        SWi = -1
        for sr in srlist:
            if SW[sr][i] > SWm:
                SWm = SW[sr][i]
                SWi = sr
            elif SW[sr][i] == SWm:
                SWm = SWm
                SWi = SWi + sr

        SWmax.append(SWi)

    Y = np.zeros(n)
    srnum = {'CS': 0, 'SWA': 1, 'OA': 2, 'NS': 3}
    for sr in srlist:
        count = 0
        for z in range(n):
            if SWmax[z] == sr:
                count += 1
                Y[z] = srnum[sr]

        print sr
        print count
    """
    paralist = results[0]['CS']['paras'][0]  
    paralist = removekeys(paralist,  ['L', 'Lambda_high_RS', 'risk', 'SA_K', 'Prop_high'])
    
    #m = len(results[0]['CS']['paras'][0]) - 6
    #Xx = np.zeros([n, m])
    #for i in range(n):
    #    temp = results[i]['CS']['paras'][0] 
    #    temp = removekeys(temp, ['sig_eta', 'rho_eps', 'delta0', 'LL', 'Lambda_high', 'Lambda_high_RS'])
    #    Xx[i,:] = np.array([temp[p] for p in temp])
    
    home = '/home/nealbob'
    fold = '/Dropbox/Model/results/chapter5/'
    #with open(home + fold + 'xX.pkl', 'wb') as f:
    #   pickle.dump(Xx, f)
    #   f.close()
     
    with open(home + fold + 'Yy.pkl', 'rb') as f:
       Yy = pickle.load(f)
       f.close()

    for i in range(n):
        results[i]['CS']['paras'][0]['Lambda_high'] = results[i]['CS']['paras'][0]['Lambda_high'] - Yy[i, 1] #/ results[i]['CS']['paras'][0]['Prop_high']

    pnum = len(paralist)
    paras = [i for i in paralist]
    print paras

    para_names = ['$\delta0$', '$E[I]/K$', '$\rho_e$',  '$\alpha$',  '$\sigma_{\eta}$', '$n_{high}$',
     '$\Lambda_{high} - \hat \Lambda_{high}$', '$\rho_I$', '$\delta_{1b}$', '$\tau$', '$\delta_{1a}$', '$c_v$', '${\aA_{low} \over E[I]/K}$']
    print len(para_names)
    
    Xpara = np.zeros([n, pnum])
    for i in range(n):
        pn = 0
        for p in paras:
            Xpara[i, pn] = results[i]['CS']['paras'][0][p]
            if p == 'LL':
                Xpara[i, pn] = results[i]['CS']['paras'][0]['LL'] / results[i]['CS']['paras'][0]['I_K']

            pn = pn + 1

    treec = Tree_classifier(n_estimators=500, n_jobs=4) #min_samples_split=3, min_samples_leaf=2)
    treec.fit(Xpara, Y)
    rank = treec.feature_importances_ * 100
    print rank
    
    data0 = []
    inn = 0
    for p in para_names:
        record = {}
        record['Importance'] = rank[inn]
        record['CS'] = np.mean(Xpara[np.where(Y == 0), inn])
        record['SWA'] = np.mean(Xpara[np.where(Y == 1), inn])
        record['OA'] = np.mean(Xpara[np.where(Y == 2), inn])
        record['NS'] = np.mean(Xpara[np.where(Y == 3), inn])
        data0.append(record)
        inn = inn + 1

    tab = pandas.DataFrame(data0)
    tab.index = para_names
    tab = tab.sort(columns=['Importance'], ascending=False)
    tab_text = tab.to_latex(float_format='{:,.2f}'.format, escape=False)
    
    with open(home + table_out + 'classifier_table.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format, escape=False, columns=['Importance', 'CS', 'SWA', 'OA', 'NS']))
        f.close()

    pylab.ioff()
    fig_width_pt = 350
    inches_per_pt = 1.0 / 72.27
    golden_mean = 1.2360679774997898 / 2.0
    fig_width = fig_width_pt * inches_per_pt
    fig_height = fig_width * golden_mean
    fig_size = [fig_width, fig_height]
    params = {'backend': 'ps',
     'axes.labelsize': 10,
     'text.fontsize': 10,
     'legend.fontsize': 10,
     'xtick.labelsize': 8,
     'ytick.labelsize': 8,
     'text.usetex': True,
     'figure.figsize': fig_size}
    pylab.rcParams.update(params)
    plot_colors = 'rybg'
    cmap = pylab.cm.RdYlBu
    
    (xx, yy,) = np.meshgrid(np.arange(min(Xpara[:, 1]), max(Xpara[:, 1]), 0.02), np.arange(min(Xpara[:, 11]), max(Xpara[:, 11]), 0.02))

    nnn = xx.ravel().shape[0]
    Xlist = [np.mean(Xpara[:,i])*np.ones(nnn) for i in range(pnum)]

    Xlist[1] = xx.ravel()
    Xlist[11] = yy.ravel()
    X = np.array(Xlist).T

    ############## Check if Z only 1s and zeros
    Z = treec.predict(X).reshape(xx.shape)
    fig = pylab.contourf(xx, yy, Z, [0, 0.9999, 1.9999, 2.9999, 3.9999], colors=('red', 'yellow', 'blue', 'green'), alpha=0.5, antialiased=False, extend='both')
    for (i, c,) in zip(xrange(4), plot_colors):
        idx = np.where(Y == i)
        pylab.scatter(Xpara[idx, 1], Xpara[idx, 11], c=c, cmap=cmap, label=srlist[i], s = 12, lw=0.5)
        pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)

    pylab.xlabel('Mean inflow over capacity')
    pylab.ylabel('Inflow coefficient of variation')
    OUT = home + out + 'class_fig.pdf'
    pylab.savefig(OUT, bbox_inches='tight')
    pylab.show()
    
    for (i, c,) in zip(xrange(4), plot_colors):
        idx = np.where(Y == i)
        pylab.scatter(Xpara[idx, 1], Xpara[idx, 11], c=c, cmap=cmap, label=srlist[i], s=10, lw=0)
        pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)
    
    pylab.xlim(0.2, 1.2)
    pylab.ylim(0.4, 1.0)
    pylab.xlabel('Mean inflow over capacity')
    pylab.ylabel('Inflow coefficient of variation')
    OUT = home + out + 'class_fig0.pdf'
    pylab.savefig(OUT, bbox_inches='tight')
    pylab.show()
    
    (xx, yy,) = np.meshgrid(np.arange(min(Xpara[:, 1]), max(Xpara[:, 1]), 0.02), np.arange(min(Xpara[:, 11]), max(Xpara[:, 11]), 0.02))

    nnn = xx.ravel().shape[0]
    Xlist = [np.mean(Xpara[:,i])*np.ones(nnn) for i in range(pnum)]
    Xlist[5] = np.percentile(Xpara[:,5], 90)*np.ones(nnn)
    Xlist[1] = xx.ravel()
    Xlist[11] = yy.ravel()
    X = np.array(Xlist).T

    ############## Check if Z only 1s and zeros
    Z = treec.predict(X).reshape(xx.shape)
    fig = pylab.contourf(xx, yy, Z, [0, 0.9999, 1.9999, 2.9999, 3.9999], colors=('red', 'yellow', 'blue', 'green'), alpha=0.5, antialiased=False, extend='both')
    #for (i, c,) in zip(xrange(4), plot_colors):
    #    idx = np.where(Y == i)
    #    pylab.scatter(Xpara[idx, 1], Xpara[idx, 11], c=c, cmap=cmap, label=srlist[i])
    #    pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)

    pylab.xlabel('Mean inflow over capacity')
    pylab.ylabel('Inflow coefficient of variation')
    OUT = home + out + 'class_fig2.pdf'
    pylab.savefig(OUT, bbox_inches='tight')
    pylab.show()

    (xx, yy,) = np.meshgrid(np.arange(min(Xpara[:, 1]), max(Xpara[:, 1]), 0.02), np.arange(min(Xpara[:, 11]), max(Xpara[:, 11]), 0.02))

    nnn = xx.ravel().shape[0]
    Xlist = [np.mean(Xpara[:,i])*np.ones(nnn) for i in range(pnum)]
    Xlist[5] = np.percentile(Xpara[:,5], 10)*np.ones(nnn)
    Xlist[1] = xx.ravel()
    Xlist[11] = yy.ravel()
    X = np.array(Xlist).T

    ############## Check if Z only 1s and zeros
    Z = treec.predict(X).reshape(xx.shape)
    fig = pylab.contourf(xx, yy, Z, [0, 0.9999, 1.9999, 2.9999, 3.9999], colors=('red', 'yellow', 'blue', 'green'), alpha=0.5, antialiased=False, extend='both')
    #for (i, c,) in zip(xrange(4), plot_colors):
    #    idx = np.where(Y == i)
    #    pylab.scatter(Xpara[idx, 1], Xpara[idx, 11], c=c, cmap=cmap, label=srlist[i])
    #    pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)

    pylab.xlabel('Mean inflow over capacity')
    pylab.ylabel('Inflow coefficient of variation')
    OUT = home + out + 'class_fig3.pdf'
    pylab.savefig(OUT, bbox_inches='tight')
    pylab.show()

    (xx, yy,) = np.meshgrid(np.arange(min(Xpara[:, 1]), max(Xpara[:, 1]), 0.02), np.arange(min(Xpara[:, 11]), max(Xpara[:, 11]), 0.02))

    nnn = xx.ravel().shape[0]
    Xlist = [np.mean(Xpara[:,i])*np.ones(nnn) for i in range(pnum)]
    Xlist[9] = np.percentile(Xpara[:,9], 10)*np.ones(nnn)
    Xlist[1] = xx.ravel()
    Xlist[11] = yy.ravel()
    X = np.array(Xlist).T

    ############## Check if Z only 1s and zeros
    Z = treec.predict(X).reshape(xx.shape)
    fig = pylab.contourf(xx, yy, Z, [0, 0.9999, 1.9999, 2.9999, 3.9999], colors=('red', 'yellow', 'blue', 'green'), alpha=0.5, antialiased=False, extend='both')
    #for (i, c,) in zip(xrange(4), plot_colors):
    #    idx = np.where(Y == i)
    #    pylab.scatter(Xpara[idx, 1], Xpara[idx, 11], c=c, cmap=cmap, label=srlist[i])
    #    pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)

    pylab.xlabel('Mean inflow over capacity')
    pylab.ylabel('Inflow coefficient of variation')
    OUT = home + out + 'class_fig4.pdf'
    pylab.savefig(OUT, bbox_inches='tight')
    pylab.show()

    nnn = xx.ravel().shape[0]
    Xlist = [np.mean(Xpara[:,i])*np.ones(nnn) for i in range(pnum)]
    Xlist[9] = np.percentile(Xpara[:,9], 90)*np.ones(nnn)
    Xlist[1] = xx.ravel()
    Xlist[11] = yy.ravel()
    X = np.array(Xlist).T

    ############## Check if Z only 1s and zeros
    Z = treec.predict(X).reshape(xx.shape)
    fig = pylab.contourf(xx, yy, Z, [0, 0.9999, 1.9999, 2.9999, 3.9999], colors=('red', 'yellow', 'blue', 'green'), alpha=0.5, antialiased=False, extend='both')
    #for (i, c,) in zip(xrange(4), plot_colors):
    #    idx = np.where(Y == i)
    #    pylab.scatter(Xpara[idx, 1], Xpara[idx, 11], c=c, cmap=cmap, label=srlist[i])
    #    pylab.legend(bbox_to_anchor=(0.0, 1.02, 1.0, 0.102), loc=3, ncol=4, mode='expand', borderaxespad=0.0)

    pylab.xlabel('Mean inflow over capacity')
    pylab.ylabel('Inflow coefficient of variation')
    OUT = home + out + 'class_fig5.pdf'
    pylab.savefig(OUT, bbox_inches='tight')
    pylab.show()
#def sens_results(n = 110):
#    home = '/home/nealbob'
#    folder = '/Dropbox/Model/Results/chapter5/'
#    out = '/Dropbox/Thesis/IMG/chapter5/'
#    img_ext = '.pdf'
#    table_out = '/Dropbox/Thesis/STATS/chapter5/'
#    results = []
#    for i in range(n):
#        with open(home + folder + str(i) + '_result.pkl', 'rb') as f:
#            res = pickle.load(f)
#            results.append(res)
#            f.close()

    data0 = []
    n2 = results[0]['CS']['stats'][0]['SW'].shape[0] - 2
    miny = 10
    maxy = -10
    srlist = ['CS', 'SWA', 'OA', 'NS']
    SW = {}
    SWI = {}
    for sr in srlist:
        array = np.zeros(n)
        arrayI = np.zeros(n)
        for i in range(n):
            n2 = results[i][sr]['stats'][0]['SW'].shape[0] - 2
            #if n2 == 21:
            #print results[i][sr]['stats'][0]['SW'][n2]['Mean'] / 1000000
            array[i] = results[i][sr]['stats'][0]['SW'][n2]['Mean'] / 1000000
            arrayI[i] = results[i][sr]['stats'][0]['SW'][n2]['Mean'] / 1000000 / (results[i]['CS']['stats'][0]['SW'][n2]['Mean'] / 1000000)

        SW[sr] = array
        SWI[sr] = arrayI
        mn = np.min(arrayI)
        mx = np.max(arrayI)
        if mn < miny:
            miny = mn
        if mx > maxy:
            maxy = mx

    SW_p = np.zeros(n)
    for i in range(n):
        SW_p[i] = results[i][sr]['stats'][0]['SW'][0]['Mean'] / 1000000

    chart(SWI, 0.85, 1.01 * maxy, 'Social welfare relative to CS', out, 'Welfare_sens')

    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(SW[x])
        record['Min'] = np.min(SW[x])
        record['Q1'] = np.percentile(SW[x], 25)
        record['Q3'] = np.percentile(SW[x], 75)
        record['Max'] = np.max(SW[x])
        data0.append(record)

    record = {}
    record['Mean'] = np.mean(SW_p)
    record['Min'] = np.min(SW_p)
    record['Q1'] = np.percentile(SW_p, 25)
    record['Q3'] = np.percentile(SW_p, 75)
    record['Max'] = np.max(SW_p)
    data0.append(record)
    tab = pandas.DataFrame(data0)
    tab.index = ['CS', 'SWA', 'OA', 'NS', 'Planner']
    
    with open(home + table_out + 'welfare_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(SWI[x])
        record['Median'] = np.median(SWI[x])
        record['Min'] = np.min(SWI[x])
        record['Q1'] = np.percentile(SWI[x], 25)
        record['Q3'] = np.percentile(SWI[x], 75)
        record['Max'] = np.max(SWI[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = series
    with open(home + table_out + 'welfareI_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.4f}'.format, columns=['Mean', 'Median', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()

    
    idx = np.array([SWI['SWA'], SWI['OA'], SWI['NS']]).T
    
    
    tree = Tree(n_estimators=500, n_jobs=4)
    tree.fit(Xpara, idx)
    rank = tree.feature_importances_ * 100
    
    data0 = []
    inn = 0
    for p in para_names:
        record = {}
        record['Importance'] = rank[inn]
        data0.append(record)
        inn = inn + 1

    tab = pandas.DataFrame(data0)
    tab.index = para_names
    tab = tab.sort(columns=['Importance'], ascending=False)
    tab_text = tab.to_latex(float_format='{:,.2f}'.format, escape=False)
    print tab_text 
    with open(home + table_out + 'importance.txt', 'w') as f:
        f.write(tab_text)
        f.close()

    for i in range(pnum):
        X = np.zeros([200, pnum])
        for j in range(pnum):
            X[:, j] = np.ones(200) * np.mean(Xpara[:, j])

        X[:, i] = np.linspace(np.min(Xpara[:, i]), np.max(Xpara[:, i]), 200)
        Y = tree.predict(X)
        data = [[X[:, i], Y]]
        data0 = []
        for k in range(200):
            record = {}
            record['SWA'] = Y[k, 0]
            record['OA'] = Y[k, 1]
            record['NS'] = Y[k, 2]
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = X[:, i]
        chart_data = {'OUTFILE': home + out + 'SW_' + paras[i] + img_ext,
         'XLABEL': '',
         'YLABEL': '',
         'YMIN': 0.94,
         'YMAX': 1.01}
        build_chart(chart_data, data, chart_type='date', ylim=True)

    SWmax = []
    for i in range(n):
        SWm = -1
        SWi = -1
        for sr in srlist:
            if SW[sr][i] > SWm:
                SWm = SW[sr][i]
                SWi = sr
            elif SW[sr][i] == SWm:
                SWm = SWm
                SWi = SWi + sr

        SWmax.append(SWi)

    miny = 10
    maxy = -10
    S = {}
    SI = {}
    for sr in srlist:
        array = np.zeros(n)
        arrayI = np.zeros(n)
        for i in range(n):
            n2 = results[i][sr]['stats'][0]['S'].shape[0] - 2
            arrayI[i] = results[i][sr]['stats'][0]['S'][n2]['Mean'] / 1000 / (results[i]['CS']['stats'][0]['S'][n2]['Mean'] / 1000)
            array[i] = results[i][sr]['stats'][0]['S'][n2]['Mean'] / 1000

        S[sr] = array
        SI[sr] = arrayI
        mn = np.min(arrayI)
        mx = np.max(arrayI)
        if mn < miny:
            miny = mn
        if mx > maxy:
            maxy = mx

    S_p = np.zeros(n)
    for i in range(n):
        S_p[i] = results[i][sr]['stats'][0]['S'][0]['Mean'] / 1000

    chart(SI, 0.99 * miny, 1.6, 'Storage relative to CS', out, 'Storage_sens')

    series = ['CS', 'SWA', 'OA','NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(S[x])
        record['Min'] = np.min(S[x])
        record['Q1'] = np.percentile(S[x], 25)
        record['Q3'] = np.percentile(S[x], 75)
        record['Max'] = np.max(S[x])
        data0.append(record)

    record = {}
    record['Mean'] = np.mean(S_p)
    record['Min'] = np.min(S_p)
    record['Q1'] = np.percentile(S_p, 25)
    record['Q3'] = np.percentile(S_p, 75)
    record['Max'] = np.max(S_p)
    data0.append(record)
    tab = pandas.DataFrame(data0)
    tab.index = ['CS', 'SWA', 'OA', 'NS', 'Planner']
    with open(home + table_out + 'storage_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(SI[x])
        record['Min'] = np.min(SI[x])
        record['Q1'] = np.percentile(SI[x], 25)
        record['Q3'] = np.percentile(SI[x], 75)
        record['Max'] = np.max(SI[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = series
    with open(home + table_out + 'storageI_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.3f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    
    miny = 10
    maxy = -10
    Z = {}
    ZI = {}
    for sr in srlist:
        array = np.zeros(n)
        arrayI = np.zeros(n)
        for i in range(n):
            n2 = results[i][sr]['stats'][0]['Z'].shape[0] - 2
            array[i] = results[i][sr]['stats'][0]['Z'][n2]['Mean'] / 1000
            arrayI[i] = results[i][sr]['stats'][0]['Z'][n2]['Mean'] / 1000 / (results[i]['CS']['stats'][0]['Z'][n2]['Mean'] / 1000)

        Z[sr] = array
        ZI[sr] = arrayI
        mn = np.min(arrayI)
        mx = np.max(arrayI)
        if mn < miny:
            miny = mn
        if mx > maxy:
            maxy = mx

    Z_p = np.zeros(n)
    for i in range(n):
        Z_p[i] = results[i][sr]['stats'][0]['Z'][0]['Mean'] / 1000

    chart(ZI, 0, 3, 'Spills relative to CS', out, 'Spills_sens')
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(Z[x])
        record['Min'] = np.min(Z[x])
        record['Q1'] = np.percentile(Z[x], 25)
        record['Q3'] = np.percentile(Z[x], 75)
        record['Max'] = np.max(Z[x])
        data0.append(record)

    record = {}
    record['Mean'] = np.mean(Z_p)
    record['Min'] = np.min(Z_p)
    record['Q1'] = np.percentile(Z_p, 25)
    record['Q3'] = np.percentile(Z_p, 75)
    record['Max'] = np.max(Z_p)
    data0.append(record)
    tab = pandas.DataFrame(data0)
    tab.index = ['CS', 'SWA', 'OA', 'NS', 'Planner']
    with open(home + table_out + 'spill_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(ZI[x])
        record['Min'] = np.min(ZI[x])
        record['Q1'] = np.percentile(ZI[x], 25)
        record['Q3'] = np.percentile(ZI[x], 75)
        record['Max'] = np.max(ZI[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = series
    with open(home + table_out + 'spillI_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.3f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    
    
    
    miny = 10
    maxy = -10
    U = {}
    UI = {}
    for sr in srlist:
        array = np.zeros(n)
        arrayI = np.zeros(n)
        for i in range(n):
            n2 = results[i][sr]['stats'][0]['U_high'].shape[0] - 2
            array[i] = results[i][sr]['stats'][0]['U_high'][n2]['Mean'] / 1000000
            arrayI[i] = results[i][sr]['stats'][0]['U_high'][n2]['Mean'] / 1000000 / (results[i]['CS']['stats'][0]['U_high'][n2]['Mean'] / 1000000)

        U[sr] = array
        UI[sr] = arrayI
        mn = np.min(arrayI)
        mx = np.max(arrayI)
        if mn < miny:
            miny = mn
        if mx > maxy:
            maxy = mx

    chart(UI, 0.8, 1.01 * maxy, 'High user welfare relative to CS', out, 'highUI_sens')
    
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(U[x])
        record['Min'] = np.min(U[x])
        record['Q1'] = np.percentile(U[x], 25)
        record['Q3'] = np.percentile(U[x], 75)
        record['Max'] = np.max(U[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = ['CS', 'SWA', 'OA', 'NS']
    with open(home + table_out + 'highU_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(UI[x])
        record['Min'] = np.min(UI[x])
        record['Q1'] = np.percentile(UI[x], 25)
        record['Q3'] = np.percentile(UI[x], 75)
        record['Max'] = np.max(UI[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = series
    with open(home + table_out + 'highUI_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.3f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()

    miny = 10
    maxy = -10
    U = {}
    UI = {}
    for sr in srlist:
        array = np.zeros(n)
        arrayI = np.zeros(n)
        for i in range(n):
            n2 = results[i][sr]['stats'][0]['U_low'].shape[0] - 2
            array[i] = results[i][sr]['stats'][0]['U_low'][n2]['Mean'] / 1000000
            arrayI[i] = results[i][sr]['stats'][0]['U_low'][n2]['Mean'] / 1000000 / (results[i]['CS']['stats'][0]['U_low'][n2]['Mean'] / 1000000)

        U[sr] = array
        UI[sr] = arrayI
        mn = np.min(arrayI)
        mx = np.max(arrayI)
        if mn < miny:
            miny = mn
        if mx > maxy:
            maxy = mx

    chart(UI, 0.8, 1.15, 'Low user welfare relative to CS', out, 'lowUI_sens')
    
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(U[x])
        record['Min'] = np.min(U[x])
        record['Q1'] = np.percentile(U[x], 25)
        record['Q3'] = np.percentile(U[x], 75)
        record['Max'] = np.max(U[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = ['CS', 'SWA', 'OA', 'NS']
    with open(home + table_out + 'lowU_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    
    series = ['CS', 'SWA', 'OA', 'NS']
    data0 = []
    for x in series:
        record = {}
        record['Mean'] = np.mean(UI[x])
        record['Min'] = np.min(UI[x])
        record['Q1'] = np.percentile(UI[x], 25)
        record['Q3'] = np.percentile(UI[x], 75)
        record['Max'] = np.max(UI[x])
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = series
    with open(home + table_out + 'lowUI_sens.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.3f}'.format, columns=['Mean', 'Min', 'Q1', 'Q3', 'Max'], escape=False))
        f.close()
    """
