import pandas as pd
import numpy as np
import time
import datetime

start = time.time()

# column 명 지정해서 불러오기
f1 = pd.read_csv('21.gff', delimiter = '\t', names = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
#f1 = pd.read_csv('Homo_sapiens.GRCh38.chromosome.21.motif_features.gff.csv', names = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

# len에 따라 분리
lst = f1['9'].str.split(';')
lst_len = lst.str.len()
f1['lst_len'] = lst_len

print(f1)

# df1: len = 3인 경우
# df1: len = 4인 경우
df1 = f1[f1['lst_len'] == 3]
df2 = f1[f1['lst_len'] == 4]

# df1 column 분리 후 split
lst = df1['9'].str.split(';').str[0]
lst2 = df1['9'].str.split(';').str[1]
lst3 = df1['9'].str.split(';').str[2]
del df1['9']
df1['binding_matrix_stable_id'] = lst
df1['stable_id'] = lst2
df1['transcription_factor_complex'] = lst3

lst = df1['binding_matrix_stable_id'].str.split('=').str[1]
lst2 = df1['stable_id'].str.split('=').str[1]
lst3 = df1['transcription_factor_complex'].str.split('=').str[1]
df1['binding_matrix_stable_id'] = lst
df1['stable_id'] = lst2
df1['transcription_factor_complex'] = lst3

print(df1)

# %, :: 분리
complex_new = df1['transcription_factor_complex'].str.split('%')
df1['transcription_factor_complex'] = complex_new

def unnest(df, tile, explode):
    vals = df[explode].sum(1)
    rs = [len(r) for r in vals]
    a = np.repeat(df[tile].values, rs, axis=0)
    b = np.concatenate(vals.values)
    d = np.column_stack((a, b))
    return pd.DataFrame(d, columns = tile +  ['_'.join(explode)])

df1 = unnest(df1, ['1','2','3','4','5','6','7','8','binding_matrix_stable_id','stable_id'], ['transcription_factor_complex']) # % 분리
complex_new2 = df1['transcription_factor_complex'].str.split('::')
df1['transcription_factor_complex'] = complex_new2

final_df1 = unnest(df1, ['1','2','3','4','5','6','7','8','binding_matrix_stable_id','stable_id'], ['transcription_factor_complex']) # :: 분리
print(final_df1)


# df2 column 분리 후 split
lst = df2['9'].str.split(';').str[0]
lst2 = df2['9'].str.split(';').str[1]
lst3 = df2['9'].str.split(';').str[2]
lst4 = df2['9'].str.split(';').str[3]
del df2['9']
df2['binding_matrix_stable_id'] = lst
df2['epigenomes_with_experimental_evidence'] = lst2
df2['stable_id'] = lst3
df2['transcription_factor_complex'] = lst4

lst = df2['binding_matrix_stable_id'].str.split('=').str[1]
lst2 = df2['epigenomes_with_experimental_evidence'].str.split('=').str[1]
lst3 = df2['stable_id'].str.split('=').str[1]
lst4 = df2['transcription_factor_complex'].str.split('=').str[1]
df2['binding_matrix_stable_id'] = lst
df2['epigenomes_with_experimental_evidence'] = lst2
df2['stable_id'] = lst3
df2['transcription_factor_complex'] = lst4


# % 분리
evidence_new = df2['epigenomes_with_experimental_evidence'].str.split('%')
complex_new = df2['transcription_factor_complex'].str.split('%')

df2['epigenomes_with_experimental_evidence'] = evidence_new
df2['transcription_factor_complex'] = complex_new

df2 = unnest(df2, ['1','2','3','4','5','6','7','8','binding_matrix_stable_id','stable_id','epigenomes_with_experimental_evidence',], ['transcription_factor_complex'])
df2 = unnest(df2, ['1','2','3','4','5','6','7','8','binding_matrix_stable_id','stable_id','transcription_factor_complex'], ['epigenomes_with_experimental_evidence'])

# :: 분리
evidence_new2 = df2['epigenomes_with_experimental_evidence'].str.split('::')
complex_new2 = df2['transcription_factor_complex'].str.split('::')

df2['epigenomes_with_experimental_evidence'] = evidence_new2
df2['transcription_factor_complex'] = complex_new2

df2 = unnest(df2, ['1','2','3','4','5','6','7','8','binding_matrix_stable_id','stable_id','epigenomes_with_experimental_evidence',], ['transcription_factor_complex'])
final_df2 = unnest(df2, ['1','2','3','4','5','6','7','8','binding_matrix_stable_id','stable_id','transcription_factor_complex'], ['epigenomes_with_experimental_evidence'])

result = pd.concat([final_df1, final_df2])

print("Write result data to {} ...".format('result.txt'))
result.to_csv("result.txt", sep = '\t', index = False)

sec = time.time() - start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print("Time: ", times)