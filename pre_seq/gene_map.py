"""
.. module:: gene_map
    :synopsis: generate map for sequence labeling
 
.. moduleauthor:: Liyuan Liu
"""
import pickle
import argparse
import os
import random
import numpy as np
from tqdm import tqdm
import sys

import itertools
import functools

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_corpus', default='./data/ner/eng.train.iobes')
    parser.add_argument('--input_embedding', default=None)
    parser.add_argument('--output_map', default="./data/conll_map.pk")
    parser.add_argument('--threshold', type=int, default=5)
    parser.add_argument('--unk', default='unk')
    args = parser.parse_args()

    gw_map = dict()
    embedding_array = list()
    if args.input_embedding != None:
        headline = True
        for line in open(args.input_embedding, 'r', encoding="utf-8"):
            line = line.split()
            vector = list(map(lambda t: float(t), filter(lambda n: n and not n.isspace(), line[1:])))
            if line[0] == args.unk:
                gw_map['<unk>'] = len(gw_map)
            else:
                gw_map[line[0]] = len(gw_map)
            embedding_array.append(vector)

        bias = 2 * np.sqrt(3.0 / len(embedding_array[0]))

        gw_map['<\n>'] = len(gw_map)
        embedding_array.append([random.random() * bias - bias for tup in embedding_array[0]])
    else:
        gw_map['<unk>'] = len(gw_map)
        gw_map['<\n>'] = len(gw_map)

    w_count = dict()
    c_count = dict()
    y_map = dict()
    # y_map = {'B-LST':0, 'E-LST':1}

    with open(args.train_corpus, 'r') as fin:
        for line in fin:
            if line.isspace() or line.startswith('-DOCSTART-'):
                c_count['\n'] = c_count.get('\n', 0) + 1
            else:
                line = line.split()
                for tup in line[0]:
                    c_count[tup] = c_count.get(tup, 0) + 1
                c_count[' '] = c_count.get(' ', 0) + 1
                if line[-1] not in y_map:
                    y_map[line[-1]] = len(y_map)
                word = line[0].lower()
                if word not in gw_map:
                    w_count[word] = w_count.get(word, 0) + 1

    w_map = {v[0]:k for k, v in enumerate(w_count.items()) if v[1] > args.threshold}
    for k in w_map:
        gw_map[k] = len(gw_map)
        if args.input_embedding != None:
            embedding_array.append([random.random() * bias - bias for tup in embedding_array[0]])

    #c_map = {v[0]:k for k, v in enumerate(c_count.items()) if v[1] > args.threshold}
    c_map = {}
    for k, v in enumerate(c_count.items()):
        if v[1] > args.threshold:
            c_map[v[0]] = len(c_map)
    c_map['<unk>'] = len(c_map)

    y_map['<s>'] = len(y_map)
    y_map['<eof>'] = len(y_map)

    print({'gw_map': len(gw_map), 'c_map': len(c_map), 'y_map': len(y_map), 'emb_array' : len(embedding_array)})
    print(c_count.items())
    print(c_map)
    print(y_map)

    with open(args.output_map, 'wb') as f:
        pickle.dump({'gw_map': gw_map, 'c_map': c_map, 'y_map': y_map, 'emb_array': embedding_array}, f)
