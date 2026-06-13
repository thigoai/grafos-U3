from collections import deque

def pref_to_rank(pref):
    return {
        a: {b: rank for rank, b in enumerate(a_pref)}
        for a, a_pref in pref.items()
    }

def gale_shapley(A, B, A_pref, B_pref):
    """
    pref é um dicionário com cada elemento de A e sua respectiva
    lista de preferências.
    """
    B_rank = pref_to_rank(B_pref) # Em alguns momentos é mais fácil usar o ranking
    a_list = {a: deque(pref_list) for a, pref_list in A_pref.items()}

    pair = {}
    remaining_A = set(A)
    while len(remaining_A) > 0: # São feitas propostas até todo mundo estar casado
        a = remaining_A.popleft()
        b = a_list[a].popleft() # a primeiro propõem para a sua primeira opção b,
        # que não será mais considerada (para a)

        if b not in pair:
            pair[b] = a # se b está livre, casamos os dois por enquanto
        
        else: # se b já está casado
            a_current = pair[b]
            b_prefer_current = B_rank[b][a_current] < B_rank[b][a]
            if b_prefer_current:
                remaining_A.add(a) # a pior que o marido atual, não trocamos
            else: # a melhor que o marido atual
                pair[b] = a # trocamos
                remaining_A.add(a_current) # o antigo marido de b volta para a lista de solteiros.
    
    return [(a, b) for b, a in pair.items()]
