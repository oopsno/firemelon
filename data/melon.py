# encoding: UTF-8

import csv
import os

melon_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'melon.csv')

with open(melon_csv, encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file)
    watermelon_v2 = []
    watermelon_v3 = []
    next(reader)  # skip header
    for i, row in enumerate(reader):
        _, *attr, density, saccharinity, label = row
        density, saccharinity = map(float, [density, saccharinity])
        label = label == '是'
        watermelon_v2.append([attr, label])
        watermelon_v3.append([attr + [density, saccharinity], label])

watermelon_v2_alpha = list(watermelon_v2)
for s, f in [(0, 0), (1, 5), (2, 2), (4, 0), (5, 4), (7, 3),
             (8, 1), (9, 3), (10, 5), (11, 2), (12, 0), (14, 4), (16, 1)]:
    watermelon_v2_alpha[s][0][f] = None

watermelon_v3_alpha = [[melon[6:8], int(label)] for melon, label in watermelon_v3]


def str_to_index(dataset, dtype=int):
    label = [l for _, l in dataset]
    converted = [[] for _ in range(len(dataset))]
    m = []
    n = []
    if len(dataset) > 0:
        features = len(dataset[0][0])
        for i in range(features):
            if isinstance(dataset[0][0][i], str):
                ks = list(set(s[0][i] for s in dataset))
                xs = {k: dtype(v) for k, v in zip(ks, range(features))}
                m.append(xs)
                n.append(ks)
                for r, d in enumerate(dataset):
                    converted[r].append(xs[d[0][i]])
            else:
                m.append(None)
                n.append(None)
                for r, d in enumerate(dataset):
                    converted[r].append(d[0][i])
    return [[d, l] for d, l in zip(converted, label)], m, n
