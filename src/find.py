# merge local time and energy
import pandas as pd
import csv

signals = pd.read_csv('../data/raw_signals.csv')
backgrounds = pd.read_csv('../data/raw_backgrounds.csv')

W = signals['wire']
T = signals['mdetmt0']
E = signals['me']
time = list(T)
energy = list(E)
wire = list(W)
tmp = list(set(wire))
total = []

for i in tmp:
	time_i = []
	energy_i = []
	position = [t for t, v in enumerate(wire) if v == i]
	for j in position:
		time_i.append(time[j])
	for j in position:
		energy_i.append(energy[j])
	min_i = min(time_i)
	sum_e = sum(energy_i)
	row_i = signals.loc[wire.index(i)]
	row_i[12] = min_i
	row_i[15] = sum_e
	total.append(row_i)
with open('test.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(total)
