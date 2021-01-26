import pandas as pd

f1 = pd.read_csv("1_result.txt", delimiter = '\t')
f2 = pd.read_csv("2_result.txt", delimiter = '\t')
f3 = pd.read_csv("3_result.txt", delimiter = '\t')
f4 = pd.read_csv("4_result.txt", delimiter = '\t')
f5 = pd.read_csv("5_result.txt", delimiter = '\t')
f6 = pd.read_csv("6_result.txt", delimiter = '\t')
f7 = pd.read_csv("7_result.txt", delimiter = '\t')
f8 = pd.read_csv("8_result.txt", delimiter = '\t')
f9 = pd.read_csv("9_result.txt", delimiter = '\t')
f10 = pd.read_csv("10_result.txt", delimiter = '\t')
f11 = pd.read_csv("11_result.txt", delimiter = '\t')
f12 = pd.read_csv("12_result.txt", delimiter = '\t')
f13 = pd.read_csv("13_result.txt", delimiter = '\t')
f14 = pd.read_csv("14_result.txt", delimiter = '\t')
f15 = pd.read_csv("15_result.txt", delimiter = '\t')
f16 = pd.read_csv("16_result.txt", delimiter = '\t')
f17 = pd.read_csv("17_result.txt", delimiter = '\t')
f18 = pd.read_csv("18_result.txt", delimiter = '\t')
f19 = pd.read_csv("19_result.txt", delimiter = '\t')
f20 = pd.read_csv("20_result.txt", delimiter = '\t')
f21 = pd.read_csv("21_result.txt", delimiter = '\t')
f22 = pd.read_csv("22_result.txt", delimiter = '\t')

df1 = f1[f1['epigenomes_with_experimental_evidence'].isnull()==False]
df2 = f2[f2['epigenomes_with_experimental_evidence'].isnull()==False]
df3 = f3[f3['epigenomes_with_experimental_evidence'].isnull()==False]
df4 = f4[f4['epigenomes_with_experimental_evidence'].isnull()==False]
df5 = f5[f5['epigenomes_with_experimental_evidence'].isnull()==False]
df6 = f6[f6['epigenomes_with_experimental_evidence'].isnull()==False]
df7 = f7[f7['epigenomes_with_experimental_evidence'].isnull()==False]
df8 = f8[f8['epigenomes_with_experimental_evidence'].isnull()==False]
df9 = f9[f9['epigenomes_with_experimental_evidence'].isnull()==False]
df10 = f10[f10['epigenomes_with_experimental_evidence'].isnull()==False]
df11 = f11[f11['epigenomes_with_experimental_evidence'].isnull()==False]
df12 = f12[f12['epigenomes_with_experimental_evidence'].isnull()==False]
df13 = f13[f13['epigenomes_with_experimental_evidence'].isnull()==False]
df14 = f14[f14['epigenomes_with_experimental_evidence'].isnull()==False]
df15 = f15[f15['epigenomes_with_experimental_evidence'].isnull()==False]
df16 = f16[f16['epigenomes_with_experimental_evidence'].isnull()==False]
df17 = f17[f17['epigenomes_with_experimental_evidence'].isnull()==False]
df18 = f18[f18['epigenomes_with_experimental_evidence'].isnull()==False]
df19 = f19[f19['epigenomes_with_experimental_evidence'].isnull()==False]
df20 = f20[f20['epigenomes_with_experimental_evidence'].isnull()==False]
df21 = f21[f21['epigenomes_with_experimental_evidence'].isnull()==False]
df22 = f22[f22['epigenomes_with_experimental_evidence'].isnull()==False]

print("df1\n")
print(df1)
print("df2\n")
print(df2)
print("df3\n")
print(df3)
print("df4\n")
print(df4)
print("df5\n")
print(df5)
print("df6\n")
print(df6)
print("df7\n")
print(df7)
print("df8\n")
print(df8)
print("df9\n")
print(df9)
print("df10\n")
print(df10)
print("df11\n")
print(df11)
print("df12\n")
print(df12)
print("df13\n")
print(df13)
print("df14\n")
print(df14)
print("df15\n")
print(df15)
print("df16\n")
print(df16)
print("df17\n")
print(df17)
print("df18\n")
print(df18)
print("df19\n")
print(df19)
print("df20\n")
print(df20)
print("df21\n")
print(df21)
print("df22\n")
print(df22)


evidence_all = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22])
evidence_all.to_csv("evidence_all.txt", sep = '\t', index = False)