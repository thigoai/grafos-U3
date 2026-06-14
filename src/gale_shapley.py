from collections import deque

def pref_to_rank(pref):
    return {
        a: {b: rank for rank, b in enumerate(a_pref)}
        for a, a_pref in pref.items()
    }

def gale_shapley(H, M, H_pref, M_pref):
    rejeitados = set(H)
    proxima_opcao = {h : 0 for h in H}
    em_consideracao = {m : None for m in M}
    M_rank = pref_to_rank(M_pref)

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


