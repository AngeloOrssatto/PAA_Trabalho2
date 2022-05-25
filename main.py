import glob, time
import pandas as pd
from forca_bruta import forca_bruta
from gulosa import gulosa

results_fb = pd.DataFrame(columns=['N','Tempo','Lucro','Configuracao'])
results_eg = pd.DataFrame(columns=['N','Tempo','Lucro','Configuracao'])

files_fb = glob.glob('fb/*.txt')
files_eg = glob.glob('eg/*.txt')

i = 0
for file in files_fb:
   f = open(file, 'r')
   print(file)
   lines = f.readlines()
   capacidade = lines[0].split()
   capacidade = int(capacidade[0])
   beneficios = lines[1].split()
   beneficios = [int(i) for i in beneficios]
   pesos = lines[2].split()
   pesos = [int(i) for i in pesos]
   n = len(pesos)

   begin = time.perf_counter_ns()
   el = [(0, 1)]
   r = forca_bruta(el, n, pesos, beneficios, capacidade)
   end = time.perf_counter_ns()
   print("FB | Resultado: ", r)
   print("FB | Tempo Execução: ", end-begin)
   results_fb.loc[i] = [n, end-begin, r[0], r[1]]
   i = i + 1

results_fb.to_excel('results_fb.xlsx')

i = 0
for file in files_eg:
    f = open(file, 'r')
    print(file)
    lines = f.readlines()
    capacidade = lines[0].split()
    capacidade = int(capacidade[0])
    beneficios = lines[1].split()
    beneficios = [float(i) for i in beneficios]
    pesos = lines[2].split()
    pesos = [float(i) for i in pesos]
    n = len(pesos)

    # print(capacidade, beneficios, pesos)
    begin = time.perf_counter_ns()
    r = gulosa(capacidade, pesos, beneficios, n)
    end = time.perf_counter_ns()
    print("EG | Resultado: ", r)
    print("EG | Tempo execução: ", end-begin)

    results_eg.loc[i] = [n, end-begin, r[0], r[1]]
    i = i + 1
results_eg = results_eg.sort_values(by='N')
results_eg = results_eg.reset_index(drop=True)
print(results_eg)
results_eg.to_excel('results_eg.xlsx')
