import pandas as pd
from skbio.alignment import StripedSmithWaterman
import multiprocessing
from functools import partial
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

'''# SW 결과 aligned query sequence 반환해주는 함수
def aligned_query_sequence(symbolA, symbolB):
	# striped SW symbol 생성 및 SW score 계산
	symbolA = StripedSmithWaterman(symbolA)
	result = symbolA(str(symbolB))
	return result['aligned_query_sequence']

# SW 결과 aligned query sequence length 반환해주는 함수
def length_TF(symbolA, symbolB):
	# striped SW symbol 생성 및 SW score 계산
	symbolA = StripedSmithWaterman(symbolA)
	result = symbolA(str(symbolB))
	return len(result['aligned_query_sequence'])

# SW 결과 aligned target sequence 반환해주는 함수
def aligned_target_sequence(symbolA, symbolB):
	# striped SW symbol 생성 및 SW score 계산
	symbolA = StripedSmithWaterman(symbolA)
	result = symbolA(str(symbolB))
	return result['aligned_target_sequence']

# SW 결과 alignment score 반환해주는 함수
def sw_score(symbolA, symbolB):
	# striped SW symbol 생성 및 SW score 계산
	symbolA = StripedSmithWaterman(symbolA)
	result = symbolA(str(symbolB))
	return result['optimal_alignment_score']'''

# mismatch 계산함수
def mismatch(p,q):
	p = str(p)
	q = str(q)
	dist = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			dist += 1
	return dist


def all_SW(symbolA, symbolB):
	symbolA = StripedSmithWaterman(symbolA)
	result = symbolA(str(symbolB))
	return pd.Series([result['aligned_query_sequence'],len(result['aligned_query_sequence']), result['aligned_target_sequence'],result['optimal_alignment_score']])

tsg = pd.read_csv('Tumor_suppressor_gene_list.csv')
ocg = pd.read_csv('oncogene_list.csv')

# tsg, ocg list
tsg_list = list(tsg['GeneName'])
ocg_list = list(ocg['OncogeneName'])

# oncogene list에 TF있는지 확인하는 함수
def check_ocg(TF):
	if str(TF) not in ocg_list:
		return False
	else:
		return True

# tumor suppressor gene list에 TF있는지 확인하는 함수
def check_tsg(TF):
    if str(TF) not in tsg_list:
        return False
    else:
        return True

if __name__ == '__main__':
	# 경고 제거
	pd.set_option('mode.chained_assignment',  None)
	# artificial promoter sequence
	a_p = 'TGCCGCTAGAGGACGCCGTGGCCGCGCTCAGCGGTGCCGCTAGAGGCGCGCGGCCGCGGTCACCCTACCTTCCTCCGGGCCTCTCAGAGGAAATTAAGCGCTGCTGTCCACTGGCCCCACGGCACCGGGACACTGGGTGGATGAGTCCAGTCCCGCGGCCTTTCTCTTCACCGGAGACACCGATTAGATTTCAAGCCCATTTTATGACCCTCCGGACTTCCGCAGCGCTTATTTCCCTCCTGAATGCGGAGCAAGATGACTCCCACCCACCCCCGGGGCTGGGGGCGAGGCAGAACTGCGA'

	# tfbs, tumor supressor gene, oncogene 파일 불러오기
	tfbs = pd.read_csv('tfbs_test.txt', delimiter = '\t', low_memory=False)
	# tsg = pd.read_csv('Tumor_suppressor_gene_list.csv')
	# ocg = pd.read_csv('oncogene_list.csv')

	# tsg, ocg 저장
	# tsg_list = tsg['GeneName']
	# ocg_list = ocg['OncogeneName']

	# 염색체 번호, TF 서열, TF만 불러오고 컬럼명 변경
	result = tfbs[['1', 'sequence', 'transcription_factor_complex']]
	result.columns = ['chromosome_number', 'TF_sequence', 'TF']

	# Artificial promoter 열 생성
	result['Artificial_promoter_sequence'] = a_p

	# 병렬처리 실행
	with poolcontext(processes = 16) as pool:
		symbolA = result['TF_sequence']
		symbolB = result['Artificial_promoter_sequence']
		
		# SymbolA, symbolB zip으로 묶어서 starmap으로 인자 전달 및 함수 실행
		result[['Artificial promoter sequence(query)','length(TF)','TF_sequence(target)','SW_score']] = pool.starmap(all_SW, zip(symbolA, symbolB))
		print(result)
		# mismatch 함수 실행
		p = result['TF_sequence(target)']
		q = result['Artificial promoter sequence(query)']
		result['mismatch'] = pool.starmap(mismatch, zip(p, q))
		print(result)

		# Oncogene 열 생성
		TF = result['TF']
		result['OCG'] = pool.map(check_ocg, TF)

		# Tumor suppressor gene 열 생성
		result['TSG'] = pool.map(check_tsg, TF) 

	# 컬럼병 변경
	result = result[['Artificial_promoter_sequence', 'TF', 'TF_sequence(target)', 'Artificial promoter sequence(query)', 'mismatch', 'length(TF)', 'chromosome_number', 'OCG', 'TSG']]
	print(result)
	result = result.drop_duplicates() # 중복 제거 후 저장
	result.to_csv('testresult.txt', sep = '\t', index = False)