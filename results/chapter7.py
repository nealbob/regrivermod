from __future__ import division
from chartbuilder import *
import numpy as np
import pandas
import pylab
import pickle
from sklearn.ensemble import ExtraTreesClassifier as Tree_classifier
from sklearn.ensemble import ExtraTreesRegressor as Tree

def planner(results):

    """
        Generate charts and tables for central case scenarios
    """
    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter7/'
    out = '/Dropbox/Thesis/IMG/chapter7/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter7/'
     
    #with open(home + folder + 'central_result.pkl', 'rb') as f:
    #    results = pickle.load(f)
    #    f.close()

    stats_envoff, timeseries_envoff, stats, timeseries = results


    ###### Summary results #####
    
    cols = ['Mean', 'SD', '2.5th', '25th', '75th', '97.5th']
    rows = ['Consumptive', 'Optimal']
    series = ['SW', 'Profit', 'B', 'S', 'W', 'E']
    scale = {'SW' : 1000000, 'Profit' : 1000000, 'S' : 1000, 'W' : 1000, 'E' : 1000, 'B' : 1000000}

    m = 1

    for x in series:
        data0 = []

        record = {}
        for col in cols:
            record[col] = stats_envoff[x]['Annual'][col][m] / scale[x]
        data0.append(record)

        record = {}
        for col in cols:
            record[col] = stats[x]['Annual'][col][m] / scale[x]
        data0.append(record)
        
        data = pandas.DataFrame(data0)
        data.index = rows

        with open(home + table_out + ' ' + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()
    
    ###### Environmental flows #####
    
    cols = ['Mean', 'SD', '2.5th', '25th', '75th', '97.5th']
    rows = ['Summer', 'Winter', 'Annual']
    series = ['Q_env', 'Q']
    scale = {'Q_env' : 1000, 'Q' : 1000}

    m = 1

    for x in series:
        data0 = []
        for row in rows:
            record = {}
            for col in cols:
                record[col] = stats[x][row][col][m] / scale[x]
            data0.append(record)
        
        data = pandas.DataFrame(data0)
        data.index = rows

        with open(home + table_out + ' ' + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()


    ###### River flows #########

    cols = ['Mean', 'SD', '2.5th', '25th', '75th', '97.5th']
    rows = ['Summer', 'Winter', 'Annual']
    series = ['F1', 'F1_tilde', 'F3', 'F3_tilde']
    scale = 1000

    m = 1

    for x in series:
        data0 = []

        for row in rows:
            record = {}
            for col in cols:
                record[col] = stats[x][row][col][m] / scale
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = rows

        with open(home + table_out + ' ' + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()
    
    for x in series:
        data0 = []

        for row in rows:
            record = {}
            for col in cols:
                record[col] = stats_envoff[x][row][col][m] / scale
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = rows

        with open(home + table_out + ' ' + x + '_envoff.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()

    # Flow duration curves
    data = {'Natural' : timeseries['F1_tilde'][:, 0],
            'Consumptive' : timeseries_envoff['F1'][:, 0],
            'Optimal' :  timeseries['F1'][:, 0] } 
    duration_curve(data, OUTFILE=home + out + 'up_sum' + img_ext)

    data = {'Natural' : timeseries['F1_tilde'][:, 1],
            'Consumptive' : timeseries_envoff['F1'][:, 1],
            'Optimal' :  timeseries['F1'][:, 1] } 
    duration_curve(data, OUTFILE=home + out + 'up_win' + img_ext)
    
    data = {'Natural' : timeseries['F3_tilde'][:, 0],
            'Consumptive' : timeseries_envoff['F3'][:, 0],
            'Optimal' :  timeseries['F3'][:, 0] } 
    duration_curve(data, OUTFILE=home + out + 'down_sum' + img_ext)
    
    data = {'Natural' : timeseries['F3_tilde'][:, 1],
            'Consumptive' : timeseries_envoff['F3'][:, 1],
            'Optimal' :  timeseries['F3'][:, 1] } 
    duration_curve(data, OUTFILE=home + out + 'down_win' + img_ext)


def duration_curve(data, bins=100, XMAX=0, OUTFILE=''):

    chart_params()
    
    xmax = 0
    pylab.figure()
    for x in data:
        values, base = np.histogram(data[x], bins=bins)
        cum = np.cumsum(values) / float(len(data[x]))

        fig = pylab.plot(base[:-1], 1 - cum, label=x)
        
        xmax = max(xmax, np.max(data[x]))
    
    if XMAX == 0:
        XMAX = xmax

    setFigLinesBW(fig[0])
    #pylab.legend()
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.) 
    pylab.xlim(0, XMAX)
    pylab.savefig(OUTFILE, bbox_inches='tight')
    pylab.show()


def simple_share_model(n=10):

    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter6/lambda/'
    model = '/Dropbox/Model/'
    out = '/Dropbox/Thesis/IMG/chapter7/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter7/'
   
    results = []
    paras = []

    for i in range(n):
        if i != 9:
            with open(home + folder + 'lambda_result_' + str(i) +'.pkl', 'rb') as f:
                results.extend(pickle.load(f))
                f.close()

            with open(home + folder + 'lambda_para_' + str(i) + '.pkl', 'rb') as f:
                paras.extend(pickle.load(f))
                f.close()
    
    nn = (n - 1) * 10

    Y = np.zeros([nn, 4])
    X = np.zeros([nn, 12])

    for i in range(nn):
       
        Y[i, 0] = results[i][0][1][0]
        Y[i, 1] = results[i][0][1][1]
        Y[i, 2] = results[i][1][1][0]
        Y[i, 3] = results[i][1][1][1]
        
        X[i, :] = np.array([paras[i][p] for p in paras[i]])

    """    
    tree = Tree(min_samples_split=3, min_samples_leaf=2, n_estimators = 300)
    tree.fit(X, Y)
    
    with open(home + model + 'sharemodel.pkl', 'wb') as f:
       pickle.dump(tree, f)
       f.close()
    
    scen = ['RS-O', 'CS-O', 'RS-HL-O', 'CS-HL-O']

    for i in range(4):
    
        chart = {'OUTFILE' : (home + out + 'lambda_' + scen[i] + img_ext),
                 'XLABEL' : 'Optimal flow share',
                 'XMIN' : min(Y[:,i]),
                 'XMAX' : max(Y[:,i]),
                 'BINS' : 10}
        data = [Y[:,i]]
        build_chart(chart, data, chart_type='hist')

        chart = {'OUTFILE' : (home + out + 'lambda_scat_' + scen[i] + img_ext),
                 'XLABEL' : 'Number of high reliability users',
                 'YLABEL' : 'Optimal flow share'}
        data = [[X[:, 2], Y[:,i]]]
        build_chart(chart, data, chart_type='scatter')
    
    
    rank = tree.feature_importances_ * 100
    
    data0 = []
    for i in range(len(paras[0])):
        record = {}
        record['Importance'] = rank[i]
        data0.append(record)

    tab = pandas.DataFrame(data0)
    tab.index = [p for p in paras[i]]
    tab = tab.sort(columns=['Importance'], ascending=False)
    
    with open(home + table_out + 'lambda' + '.txt', 'w') as f:
        f.write(tab.to_latex(float_format='{:,.2f}'.format))
        f.close()
    """  

    from sklearn.linear_model import LinearRegression as OLS
    ols = OLS()
    
    ols.fit(X[:,2].reshape([190, 1]), Y[:,1])
    CS_c = ols.intercept_
    CS_b = ols.coef_[0]
    xp = np.linspace(30, 70, 300)
    yp = CS_c + CS_b * xp
    
    chart_params()
    pylab.figure()
    pylab.plot(X[:,2], Y[:, 1], 'o') 
    pylab.plot(xp, yp)
    pylab.xlabel('Number of high reliability users')
    pylab.ylabel('Optimal flow share')
    pylab.ylim(0, 0.8)
    pylab.savefig(home + out + 'sharemodel1.pdf')
    pylab.show()
    
    ols.fit(X[:,2].reshape([190, 1]), Y[:,3])
    CSHL_c = ols.intercept_
    CSHL_b = ols.coef_[0]
    xp = np.linspace(30, 70, 300)
    yp = CSHL_c + CSHL_b * xp
    
    chart_params() 
    pylab.figure()
    pylab.plot(X[:,2], Y[:, 3], 'o') 
    pylab.plot(xp, yp)
    pylab.xlabel('Number of high reliability users')
    pylab.ylabel('Optimal flow share')
    pylab.ylim(0, 0.8)
    pylab.savefig(home + out + 'sharemodel2.pdf')
    pylab.show()

    return [CS_c, CS_b, CSHL_c, CSHL_b]

def central_case(notrade=False):

    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter7/chapter7/'
    out = '/Dropbox/Thesis/IMG/chapter7/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter7/'
    
    rows = ['CS', 'SWA', 'OA', 'NS', 'CS-HL', 'SWA-HL']
    results = {row : 0 for row in rows}
    
    if notrade:
        filename = 'notrade'
    else:
        filename = '0'
    
    for row in rows:
        with open(home + folder + '0' + row + '_' + filename + '_result.pkl', 'rb') as f:
            results[row] = pickle.load(f)[0:2]
            f.close()
    
    ###### Summary results #####
    
    cols = ['Mean', 'SD', '2.5th', '25th', '75th', '97.5th']
    series = ['SW', 'Profit', 'B', 'S', 'W', 'E', 'Z', 'Q_low', 'Q_high', 'Q_env', 'A_low', 'A_high', 'A_env', 'S_low', 'S_high', 'S_env', 'U_low', 'U_high', 'Budget']
    scale = {'SW' : 1000000, 'Profit' : 1000000, 'S' : 1000, 'W' : 1000, 'E' : 1000, 'B' : 1000000, 'Z' : 1000, 'Q_low' : 1000, 'Q_high' : 1000, 'Q_env' : 1000, 'A_low' : 1000, 'A_high' : 1000, 'A_env' : 1000, 'S_low' : 1000, 'S_high' : 1000, 'S_env' : 1000, 'U_low' : 1000000, 'U_high' : 1000000, 'Budget' : 1000000}

    m = len(results['CS'][0]['S']['Annual']['Mean']) - 1

    if not(notrade):
        filename = 'central_'
    else:
        filename = 'notrade_'

    for x in series:
        data0 = []
        
        record = {}
        for col in cols:
            record[col] = results[row][0][x]['Annual'][col][2] / scale[x]
        data0.append(record)
        
        for row in rows:
            record = {}
            for col in cols:
                record[col] = results[row][0][x]['Annual'][col][m] / scale[x]
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = ['Planner'] + rows

        with open(home + table_out + filename + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()


    for x in series:
        data0 = []
        
        record = {}
        for col in cols:
            record[col] = results[row][0][x]['Summer'][col][2] / scale[x]
        data0.append(record)
        
        for row in rows:
            record = {}
            for col in cols:
                record[col] = results[row][0][x]['Summer'][col][m] / scale[x]
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = ['Planner'] + rows

        with open(home + table_out + filename + 'sum_' + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()
    
    for x in series:
        data0 = []
        
        record = {}
        for col in cols:
            record[col] = results[row][0][x]['Winter'][col][2] / scale[x]
        data0.append(record)
        
        for row in rows:
            record = {}
            for col in cols:
                record[col] = results[row][0][x]['Winter'][col][m] / scale[x]
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = ['Planner'] + rows

        with open(home + table_out + filename + 'win_' + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=cols))
            f.close()

    if not(notrade):
        filename = ''
    else:
        filename = 'notrade_'
    
    # central case trade-off chart
    X = np.zeros(7)
    X[0] = results['CS'][0]['B']['Annual']['Mean'][2] / scale['B']
    for i in range(1, 7):
        X[i] = results[rows[i-1]][0]['B']['Annual']['Mean'][m] / scale['B']
    
    Y = np.zeros(7)
    Y[0] = results['CS'][0]['Profit']['Annual']['Mean'][2] / scale['Profit']
    for i in range(1, 7):
        Y[i] = results[rows[i-1]][0]['Profit']['Annual']['Mean'][m] / scale['Profit']

    chart_params()
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    ax.plot(Y, X, 'o') 
    
    ax.annotate('Planner', xy=(Y[0], X[0]), xytext=(-43, 2) , textcoords='offset points', xycoords=('data'),)
    ax.annotate(rows[0], xy=(Y[1], X[1]), xytext=(2, 6) , textcoords='offset points', xycoords=('data'),)
    ax.annotate(rows[1], xy=(Y[2], X[2]), xytext=(10, -4) , textcoords='offset points', xycoords=('data'),)
    ax.annotate(rows[2], xy=(Y[3], X[3]), xytext=(-22, -5) , textcoords='offset points', xycoords=('data'),)
    ax.annotate(rows[3], xy=(Y[4], X[4]), xytext=(10, -4) , textcoords='offset points', xycoords=('data'),)
    ax.annotate(rows[4], xy=(Y[5], X[5]), xytext=(-40, 5) , textcoords='offset points', xycoords=('data'),)
    ax.annotate(rows[5], xy=(Y[6], X[6]), xytext=(-38, -14) , textcoords='offset points', xycoords=('data'),)
    
    pylab.xlabel('Mean irrigation profit (\$m)')
    pylab.ylabel('Mean environmental benefit (\$m)')
    pylab.ylim(26, 40)
    pylab.savefig(home + out + filename + 'tradeoff.pdf', bbox_inches='tight')
    pylab.show()
    
    # Storage chart
    n = len(results['CS'][0]['S']['Annual']['Mean'])
    data0 = []
    for i in range(2, n-1):
        record = {}
        for sr in ['CS', 'SWA', 'OA', 'NS']:
            record[sr] = results[sr][0]['S']['Annual']['Mean'][i] / 1000
        data0.append(record)
    
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + filename + 'Storage' + img_ext,
     'YLABEL': 'Mean storage $S_t$ (GL)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    # Budget
    n = len(results['CS'][0]['S']['Annual']['Mean'])
    data0 = []
    for i in range(2, n-1):
        record = {}
        for sr in ['CS', 'SWA', 'OA', 'NS']:
            record[sr] = results[sr][0]['Budget']['Annual']['Mean'][i] / 1000000
        data0.append(record)
    
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + filename + 'Budget' + img_ext,
     'YLABEL': 'Environmental trade $P_t(a_{0t} - q_{0t})$',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
            
    # Extraction
    n = len(results['CS'][0]['S']['Annual']['Mean'])
    data0 = []
    for i in range(2, n-1):
        record = {}
        for sr in ['CS', 'SWA', 'OA', 'NS']:
            record[sr] = results[sr][0]['E']['Annual']['Mean'][i] / 1000
        data0.append(record)
    
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + filename + 'Extraction' + img_ext,
     'YLABEL': 'Extraction, $E_t$ (GL)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')
    
    # Price
    n = len(results['CS'][0]['S']['Annual']['Mean'])
    data0 = []
    for i in range(2, n-1):
        record = {}
        for sr in ['CS', 'SWA', 'OA', 'NS']:
            record[sr] = results[sr][0]['P']['Annual']['Mean'][i]
        data0.append(record)
    
    data = pandas.DataFrame(data0)
    chart = {'OUTFILE': home + out + filename + 'Price' + img_ext,
     'YLABEL': 'Price, $P_t$ (\$/ML)',
     'XLABEL': 'Iteration'}
    build_chart(chart, data, chart_type='date')

    return results

def env_demand():

    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter7/chapter7/'
    out = '/Dropbox/Thesis/IMG/chapter7/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter7/'
    
    rows = ['CS', 'CS-HL', 'SWA', 'OA']
    
    data = {}

    for row in rows:
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            data[row] = pickle.load(f)[2]['F3'][:, 1]

    duration_curve(data, OUTFILE=home + out + 'down_win_dec' + img_ext)
    
    for row in rows:
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            data[row] = pickle.load(f)[2]['F3'][:, 0]
            f.close()

    duration_curve(data, OUTFILE=home + out + 'down_sum_dec' + img_ext)
    
    from econlearn import TilecodeRegressor as TR
    
    tr = TR(1, [11], 20)
    fig = pylab.figure()

    for row in rows:
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            Q = np.sum(pickle.load(f)[2]['Q_env'], axis = 1)
            f.close()
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            S = np.sum(pickle.load(f)[2]['S'], axis = 1) / 2.0
            f.close()
        #with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
        #    I = np.sum(pickle.load(f)[2]['I'], axis = 1)
        #    f.close()

        tr.fit(S, Q)
        tr.tile.plot(['x'], showdata=False, label=row)
    
    pylab.xlabel('Storage volume, $S_t$ (GL)')
    pylab.ylabel('Mean environmental flow, $q_{0t}$ (GL)')
    setFigLinesBW_list(fig)
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.) 
    pylab.savefig(home + out + 'env_demand_S.pdf', bbox_inches='tight')
    pylab.show()
    
    
    tr = TR(1, [11], 20)
    fig = pylab.figure()

    for row in rows:
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            Q = np.sum(pickle.load(f)[2]['Q_env'], axis = 1)
            f.close()
        #with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
        #    S = np.sum(pickle.load(f)[2]['S'], axis = 1) / 2.0
        #    f.close()
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            I = np.sum(pickle.load(f)[2]['I'], axis = 1)
            f.close()

        tr.fit(I, Q)
        tr.tile.plot(['x'], showdata=False, label=row)
    
    pylab.xlabel('Inflow, $I_t$ (GL)')
    pylab.ylabel('Mean environmental flow, $q_{0t}$ (GL)')
    setFigLinesBW_list(fig)
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.) 
    pylab.savefig(home + out + 'env_demand_I.pdf', bbox_inches='tight')
    pylab.show()

    tr = TR(1, [11], 20)
    fig = pylab.figure()

    for row in rows:
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            B = np.sum(pickle.load(f)[2]['Budget'], axis = 1)
            f.close()
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            S = np.sum(pickle.load(f)[2]['S'], axis = 1) / 2.0
            f.close()
        #with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
        #    I = np.sum(pickle.load(f)[2]['I'], axis = 1)
        #    f.close()

        tr.fit(S, B)
        tr.tile.plot(['x'], showdata=False, label=row)
    
    pylab.xlabel('Storage volume, $S_t$ (GL)')
    pylab.ylabel('Mean environmental trade, $P_t(a_{0t} - q_{0t})$ (GL)')
    setFigLinesBW_list(fig)
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.) 
    pylab.savefig(home + out + 'env_trade_S.pdf', bbox_inches='tight')
    pylab.show()
    
    tr = TR(1, [11], 20)
    fig = pylab.figure()

    for row in rows:
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            B = np.sum(pickle.load(f)[2]['Budget'], axis = 1)
            f.close()
        with open(home + folder + '0' + row + '_' + '0' + '_result.pkl', 'rb') as f:
            I = np.sum(pickle.load(f)[2]['I'], axis = 1)
            f.close()

        tr.fit(I, B)
        tr.tile.plot(['x'], showdata=False, label=row)
    
    pylab.xlabel('Inflow, $I_t$ (GL)')
    pylab.ylabel('Mean environmental trade, $P_t(a_{0t} - q_{0t})$ (GL)')
    setFigLinesBW_list(fig)
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.) 
    pylab.savefig(home + out + 'env_trade_I.pdf', bbox_inches='tight')
    pylab.show()

def tradeoff():

    home = '/home/nealbob'
    folder = '/Dropbox/Model/results/chapter7/chapter7/'
    out = '/Dropbox/Thesis/IMG/chapter7/'
    img_ext = '.pdf'
    table_out = '/Dropbox/Thesis/STATS/chapter7/'
    
    rows = ['CS', 'SWA', 'OA', 'NS', 'CS-HL', 'SWA-HL']
    rows2 = ['CS', 'SWA', 'OA', 'CS-HL']
    shares = ['10', '20', '26.3', '30', '40', '50']
    results = {share: {row : 0 for row in rows} for share in shares} 

    for share in shares: 
        for row in rows:
            if share == '26.3':
                share_ext = ''
            else:
                share_ext = share
            with open(home + folder + '0' + row + '_0_result' + share_ext + '.pkl', 'rb') as f:
                results[share][row] = pickle.load(f)[0:2]
                f.close()
    
    ###### Summary results #####
    
    series = ['SW', 'Profit', 'B', 'Budget', 'S']
    scale = {'SW' : 1000000, 'Profit' : 1000000, 'S' : 1000, 'W' : 1000, 'E' : 1000, 'B' : 1000000, 'Z' : 1000, 'Q_low' : 1000, 'Q_high' : 1000, 'Q_env' : 1000, 'A_low' : 1000, 'A_high' : 1000, 'A_env' : 1000, 'S_low' : 1000, 'S_high' : 1000, 'S_env' : 1000, 'U_low' : 1000000, 'U_high' : 1000000, 'Budget' : 1000000}

    m = len(results['20']['CS'][0]['S']['Annual']['Mean']) - 1

    for x in series:
        data0 = []
        
        for row in rows:
            record = {}
            for share in shares:
                record[share] = results[share][row][0][x]['Annual']['Mean'][m] / scale[x]
            data0.append(record)

        data = pandas.DataFrame(data0)
        data.index = rows

        with open(home + table_out + 'tradeoff_' + x + '.txt', 'w') as f:
            f.write(data.to_latex(float_format='{:,.2f}'.format, columns=shares))
            f.close()

    chart_params()
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    
    # central case trade-off chart
    rows = ['CS',  'CS-HL', 'SWA', 'OA']
    for row in rows:
        X = np.zeros(6)
        Y = np.zeros(6)
        i = 0 
        for share in shares:  
            X[i] = results[share][row][0]['Profit']['Annual']['Mean'][m] / scale['Profit']
            Y[i] = results[share][row][0]['B']['Annual']['Mean'][m] / scale['B']
            i += 1

        ax.plot(X, Y, label=row) 
    X = np.array(results['26.3']['CS'][0]['Profit']['Annual']['Mean'][2] / scale['Profit'])
    Y = np.array(results['26.3']['CS'][0]['B']['Annual']['Mean'][2] / scale['B'])

    setAxLinesBW(ax)
    ax.plot(X, Y, 'o') 
    ax.annotate('Planner', xy=(X, Y), xytext=(-5, 10) , textcoords='offset points', xycoords=('data'),)
    
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.) 
    
    pylab.xlabel('Mean irrigation profit (\$m)')
    pylab.ylabel('Mean environmental benefit (\$m)')
    pylab.xlim(140, 190)
    pylab.ylim(20, 50)
    pylab.savefig(home + out + 'tradeoff_multi.pdf', bbox_inches='tight')
    
    pylab.show()
    
    chart_params()
    fig, ax = pylab.subplots()   
    
    # central case trade-off chart
    rows = ['CS',  'CS-HL', 'SWA', 'SWA-HL', 'OA', 'NS']
    
    pos = np.arange(6)
    width = 0.1
    for share in shares:  
        i = 0
        X = np.zeros(6)
        for row in rows:
            X[i] = results[share][row][0]['SW']['Annual']['Mean'][m] / scale['SW']
            i += 1
        ax.bar(pos, X, width=width)
        pos = pos + width
        
    
    #two = ax.bar(data_set[1][0], data_set[1][1], chart['WIDTH'], color='w')
    #ax.set_ylabel(chart['YLABEL'])
    #ax.set_xticklabels(chart['LABELS'])
    #ax.legend((one[0], two[0]), chart['LEGEND'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=4, mode="expand", borderaxespad=0.)

    pylab.ylim(190, 215)
    pylab.savefig(home + out + 'tradeoff_multi2.pdf', bbox_inches='tight')
    
    pylab.show()

    return results
