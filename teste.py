import glob, time

files_fb = glob.glob('fb/*.txt')

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
   print(n)