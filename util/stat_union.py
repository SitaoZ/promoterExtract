#!/home/zhusitao/anaconda3/bin/python
# -*- coding:utf-8 -*-
'''
filename: stat_union.py.py
date: 2021/3/24 下午2:44
author: Sitao Zhu
mail: zhusitao1990@163.com
'''

import os



def get_interaction(filepath):
    '''
    generate interaction list
    :param filepath: string filepath
    :return: interaction list
    '''
    os.path.exists(filepath)

    RBP_database = []
    with open(filepath,'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            array = line.split('\t')
            it = [array[0],array[1]]
            RBP_database.append(it)
    return RBP_database


def union(list1,list2):
    '''
    return union interaction
    :param list1: interaction list1
    :param list2: interaction list2
    :return: union interaction list
    '''
    union_list = []
    for it in list1:
        A,B = it
        it1 = [A,B]
        it2 = [B,A]
        if it1 not in list2 and it2 not in list2:
            union_list.append(it)
    union_list.extend(list2)
    return union_list

def intersection(list1,list2):
    '''
    generate intersection interaction
    :param list1: intersection list1
    :param list2: intersection list2
    :return: intersection
    '''
    intersect = []
    for it in list1:
        A,B = it
        it1 = [A,B]
        it2 = [B,A]
        if it1 in list2 or it2 in list2:
            intersect.append(it)
    return intersect


def main():
    # in database
    ath_path = '/Users/zhusitao/Desktop/RBP/tobacco/result_reproduce/00.arabidposis_all_interaction/arabidposis_interaction_map_within_RBPs.csv'
    ath_interaction = get_interaction(ath_path)
    #uni
    uni_path = '/Users/zhusitao/Desktop/RBP/tobacco/result_reproduce/01.unidirect_network/with_geneid/RBP_interaction_with_geneid.csv'
    uniInteraction = get_interaction(uni_path)
    #bi
    bi_path = '/Users/zhusitao/Desktop/RBP/tobacco/result_reproduce/03.bidirect_network/with_geneid/edge_bidirect_uniq_r_geneid.txt'
    biInteraction = get_interaction(bi_path)
    # test function is true
    union_list = union(biInteraction,uniInteraction)
    if union_list == uniInteraction:
        print('ok')
    all_union = union(ath_interaction,union_list)
    print(len(all_union))
    # print(len(union_list))

    intersect1 = intersection(ath_interaction,biInteraction)
    print('双向互作,公共数据库互作的交集',len(intersect1))

    intersect2 = intersection(ath_interaction,uniInteraction)
    print('单向互作,公共数据库互作的交集', len(intersect2))


if __name__=='__main__':
    main()



