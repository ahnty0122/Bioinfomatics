import pandas as pd
import multiprocessing
from functools import partial
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

f2 = pd.read_csv('../data/Regulatory_Build_A549.csv')
f2 = f2[f2['chromosome'] == '1']
def compare(a_s, a_e, b_s, b_e):
	start = f2['start']
	end = f2['end']
	description = f2['description']
	for start, end, description in zip(start, end, description):
		if ((start <= b_s) & (b_e <= end)):
			return description
		else:
			return None

if __name__ == '__main__':
	f1 = pd.read_csv('../data/chr1.csv')
	a_s = f1['StartA']
	a_e = f1['EndA']
	b_s = f1['StartB']
	b_e = f1['EndB']

	with poolcontext(processes = 16) as pool:
		f1['description'] = pool.starmap(compare, zip(a_s, a_e, b_s, b_e))

	print(f1)
	f1.to_csv('test.csv', index = False)