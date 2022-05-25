def gulosa(capacidade, pesos, beneficios, n):
    # n = len(pesos)
    lucro = 0
    custo_beneficio = []
    itens_mochila = [0 for i in range (0, n)]
    # print(n)
    for i in range (0,n):
        # print(i, pesos[i])
        cb = beneficios[i]/pesos[i]
        custo_beneficio.append(cb)

    # print('ORIGINAL', custo_beneficio)

    search_cb = custo_beneficio.copy()

    ocupacao = 0
    while (ocupacao < capacidade):
        cb_item = max(custo_beneficio)
        n_item = custo_beneficio.index(cb_item)
        
        a = min(pesos[n_item], capacidade-ocupacao)
        if a == pesos[n_item]:
            ocupacao = ocupacao + a
            index = search_cb.index(cb_item)
            itens_mochila[index] = 1
            lucro = lucro + beneficios[index]
            custo_beneficio.pop(n_item)
            pesos.pop(n_item)
        else: 
            break
        
    return lucro, itens_mochila
    
