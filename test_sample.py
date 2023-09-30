# content of test_sample.py

from utils import hparams_combination
'''def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

def test_wrong_answar():
    assert not inc(3)== 5'''  

def test_hparam_combination_count():
    # test all possible param combinations 
    gama_list = [0.001,0.01,0.1,1]
    C_list = [1.0,10.0,20.0]
    k_list =['rbf','linear']
    h_param = {}

    h_param['gamma'] = gama_list
    h_param['cList'] = C_list
    h_param['kernels'] =k_list
    h_param_combination = hparams_combination (h_param)
    print(len(h_param_combination))
    assert  len(h_param_combination) == len(gama_list) * len(C_list)*len(k_list)


def test_hparam_combination_check():
    # test all possible param combinations 
    gama_list = [0.001,0.01,0.1,1]
    C_list = [1.0,10.0,20.0]
    k_list =['rbf','linear']

    h_param = {}

    h_param['gamma'] = gama_list
    h_param['cList'] = C_list
    h_param['kernels'] =k_list
    h_param_combination = hparams_combination (h_param)
    print(h_param_combination)
    h_param_comb1 = {'gamma':0.001,'cList': 20.0,'kernels':'linear'}
    h_param_comb2 = {'gamma':0.01,'cList': 1.0}
    assert (h_param_comb1 in h_param_combination  )