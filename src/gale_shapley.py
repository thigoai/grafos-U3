from gerador import *

def rank_to_pref(pref):
    return [
        [k for k, v in sorted(d.items(), key=lambda item: item[1])]
        for d in pref
    ]

def gale_shapley(H, M, H_rank, M_rank):
    rejeitados = set(H)
    proxima_opcao = {h : 0 for h in H}
    em_consideracao = {m : None for m in M}
    H_pref = rank_to_pref(H_rank)

    while rejeitados:
        h = rejeitados.pop()
        m = H_pref[h][proxima_opcao[h]]
        proxima_opcao[h] = proxima_opcao[h] + 1

        h2 = em_consideracao[m]

        if (h2 == None):
            em_consideracao[m] = h

        elif M_rank[m][em_consideracao[m]] < M_rank[m][h]:
            rejeitados.add(em_consideracao[m])
            em_consideracao[m] = h

        else:
            rejeitados.add(h)

    return [(h, m) for m, h in em_consideracao.items()]

        
