import pandas as pd

import multiprocessing
from functools import partial
from contextlib import contextmanager

# multiprocessing 패키지 이용한 병렬처리로 연산 속도 개선
@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()


# dna sequence 파일(.fa) 불러오기
filename = '21.fa'
with open(filename) as file_object:
    seq = file_object.read()
seq = seq.split('REF\n')[1]
re_seq = seq.replace("\n","") # sequence 저장


# sequence 문자열에서 슬라이싱으로 TFBS(Transcription Factor Binding Site)에 해당하는 sequence 만 추출하는 함수
def seq(start, end):
	result = re_seq[start:end]
	return result


if __name__ == '__main__':
	f = pd.read_csv('test.txt', delimiter = '\t', names = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
	print(f)

	# 데이터프레임 열 추가 후 sequence를 그 열에 모두 복사
	start = f['4'] - 1
	end = f['5']
	f['seq'] = re_seq


	# 함수에 데이터프레임 단위의 병렬 연산 처리, multiple arguments 가능한 pool.starmap 사용 --> 속도 개선
	with poolcontext(processes = 16) as pool:
		f['sequence'] = pool.starmap(seq, zip(start, end))
	del f['seq']
	print(f)

	f.to_csv("test_result.txt", sep = '\t', index=False)
