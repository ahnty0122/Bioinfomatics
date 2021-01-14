import requests, sys
import pandas as pd
import timeit

import multiprocessing
from functools import partial
from contextlib import contextmanager

start_time = timeit.default_timer()

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()


def restapi(start, end):
	server = "https://rest.ensembl.org"
	ext = "/sequence/region/human/21:{0}..{1}?".format(start, end)

	r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
    
	if not r.ok:
		r.raise_for_status()
		sys.exit()
        
	print(r.text)
	sequence = r.text
    
	return sequence

if __name__ == '__main__':
	f = pd.read_csv('21test.csv')

	start = f['4']
	end = f['5']

	with poolcontext(processes = 16) as pool:
		f['sequence'] = pool.starmap(restapi, zip(start, end))

	terminate_time = timeit.default_timer() # 종료 시간 체크  
	print("%f초 걸렸습니다." % (terminate_time - start_time)) 
	f.to_csv('21test_result.txt', sep = '\t', index = False)
	print(f)