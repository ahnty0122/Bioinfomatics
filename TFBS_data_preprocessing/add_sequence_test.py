import pandas as pd

import multiprocessing
from functools import partial
from contextlib import contextmanager


# TEST VERSION
@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

filename = 'human_chromosome_21.fa'
with open(filename) as file_object:
    seq = file_object.read()
seq = seq.split('REF\n')[1]
re_seq = seq.replace("\n","")

def seq(start, end):
	result = re_seq[start:end]
	return result


if __name__ == '__main__':
	f = pd.read_csv('test.txt', delimiter = '\t', names = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
	print(f)

	start = f['4'] - 1
	end = f['5']
	f['seq'] = re_seq

	with poolcontext(processes = 16) as pool:
		f['sequence'] = pool.starmap(seq, zip(start, end))
	
	del f['seq']
	print(f)

	f.to_csv("test_result.txt", sep = '\t', index=False)