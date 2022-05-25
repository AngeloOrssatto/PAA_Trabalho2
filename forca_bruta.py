def forca_bruta(args, repeat, pesos, beneficios, capacidade):
    
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    # print(pools)
    # pesos = [i for i in range (0,20)]
    # beneficio = [i for i in range (0,20)]
    # capacidade = 10
    combinacao = []
    peso = 0
    lucro = 0
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
        # print('result', result)
    for prod in result:
        # yield tuple(prod)
        l = 0
        p = 0
        # print(prod)
        
        for i in range (0, repeat):
          p = p + (prod[i]*pesos[i])
        # print('peso: ', p)
        if p <= capacidade:
          # print('é viavel')  
          for j in range (0, repeat):
            l = l + (prod[j]*beneficios[j])
          # print('lucro: ', l)
          if l > lucro:
            combinacao = prod
            lucro = l
            peso = p
            #   print('combinacao: ', prod, 'peso: ', p, 'lucro: ', l)
            
          
    return lucro, combinacao
