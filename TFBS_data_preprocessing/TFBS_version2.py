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

# SW 결과 aligned query sequence 반환해주는 함수
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
	return result['optimal_alignment_score']

# mismatch 계산함수
def mismatch(p,q):
	p = str(p)
	q = str(q)
	dist = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			dist += 1
	return dist

# oncogene list에 TF있는지 확인하는 함수
def check_ocg(ocg_list, TF):
    if TF not in ocg_list:
        return False
    else:
        return True

# tumor suppressor gene list에 TF있는지 확인하는 함수
def check_tsg(tsg_list, TF):
    if TF not in tsg_list:
        return False
    else:
        return True

if __name__ == '__main__':
	
	# artificial promoter sequence
	a_p = 'TGCCGCTAGAGGACGCCGTGGCCGCGCTCAGCGGTGCCGCTAGAGGCGCGCGGCCGCGGTCACCCTACCTTCCTCCGGGCCTCTCAGAGGAAATTAAGCGCTGCTGTCCACTGGCCCCACGGCACCGGGACACTGGGTGGATGAGTCCAGTCCCGCGGCCTTTCTCTTCACCGGAGACACCGATTAGATTTCAAGCCCATTTTATGACCCTCCGGACTTCCGCAGCGCTTATTTCCCTCCTGAATGCGGAGCAAGATGACTCCCACCCACCCCCGGGGCTGGGGGCGAGGCAGAACTGCGA'

	# tfbs, tumor supressor gene, oncogene 파일 불러오기
	tfbs = pd.read_csv('21_result.txt', delimiter = '\t')
	tsg = pd.read_csv('Tumor_suppressor_gene_list.csv')
	ocg = pd.read_csv('oncogene_list.csv')

	# 염색체 번호, TF 서열, TF만 불러오고 컬럼명 변경
	result = tfbs[['1', 'sequence', 'transcription_factor_complex']]
	result.columns = ['chromosome_number', 'TF_sequence', 'TF']

	# tsg, ocg 저장
	tsg_list = tsg['GeneName']
	ocg_list = ocg['OncogeneName']
	result['ocg_list'] = str(ocg_list)
	result['tsg_list'] = str(tsg_list)

	# Artificial promoter 열 생성
	result['Artificial_promoter_sequence'] = a_p

	# 병렬처리 실행
	with poolcontext(processes = 16) as pool:
		symbolA = result['TF_sequence']
		symbolB = result['Artificial_promoter_sequence']
		
		# SymbolA, symbolB zip으로 묶어서 starmap으로 인자 전달 및 함수 실행
		result['TF_sequence(target)'] = pool.starmap(aligned_target_sequence, zip(symbolA, symbolB))
		result['Artificial promoter sequence(query)'] = pool.starmap(aligned_query_sequence, zip(symbolA, symbolB))
		result['length(TF)'] = pool.starmap(length_TF, zip(symbolA, symbolB))
		result['SW_score'] = pool.starmap(sw_score, zip(symbolA, symbolB))

		# mismatch 함수 실행
		p = result['TF_sequence(target)']
		q = result['Artificial promoter sequence(query)']
		result['mismatch'] = pool.starmap(mismatch, zip(p, q))

		# Oncogene 열 생성
		ocg_list = result['ocg_list']
		TF = result['TF']
		result['OCG'] = pool.starmap(check_ocg, zip(ocg_list, TF))

		# Tumor suppressor gene 열 생성
		tsg_list = result['tsg_list']
		result['TSG'] = pool.starmap(check_tsg, zip(tsg_list, TF)) 

	# 컬럼병 변경
	result = result[['Artificial_promoter_sequence', 'TF', 'TF_sequence(target)', 'Artificial promoter sequence(query)', 'mismatch', 'length(TF)', 'OCG', 'TSG', 'chromosome_number']]
	print(result)
	result.to_csv('artificial_TF_21.txt', sep = '\t', index = False)