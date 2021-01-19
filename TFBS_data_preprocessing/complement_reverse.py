import multiprocessing
from functools import partial
from contextlib import contextmanager
from Bio.Seq import Seq
import pandas as pd

# 병렬
@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()
    
# 역상보서열로 변경    
def seq(seq):
    my_seq = Seq(seq).reverse_complement()
    my_seq = str(my_seq)
    return my_seq

# strand 가 '-'면 역상보서열로 변경
if __name__ == '__main__':

    df = pd.read_csv('test.txt', delimiter = '\t')
    f = df[df['7'] == '-']
    sequence = f['sequence']
    
    with poolcontext(processes = 16) as pool:
        result = pool.map(seq, sequence)

    f['sequence'] = result
    df[df['7'] == '-'] = f
    print(df)
    df.to_csv("test_result.txt", sep = '\t', index=False)