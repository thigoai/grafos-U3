import gale_shapley
import gerador
import random

def local_search(H, M, H_rank, M_rank, n_passos):

    def pares_bloqueadores(C):
        pb = []
        conjuge = {}
    
        for h, m in C:
           conjuge[h] = m 
           conjuge[m] = h
    
        for h in H:
            for m in M:
                if conjuge.get(h) == m:
                    continue
                h_conj = conjuge.get(h)
                m_conj = conjuge.get(m)
    
                if H_rank[h].get(m, 1000000) < H_rank[h].get(h_conj, 1000000) and M_rank[m].get(h, 1000000) < M_rank[m].get(m_conj, 1000000):
                    pb.append((h, m))
    
    
        pb_reduzido = {}
        for h, m in pb:
            if h not in pb_reduzido or H_rank[h].get(m, 1000000) < H_rank[h].get(pb_reduzido[h], 1000000):
                pb_reduzido[h] = m
    
        return list(pb_reduzido.items())

    def casamento_aleatorio():
        random.shuffle(list(H))
        random.shuffle(list(M))
    
        n = random.randint(0, min(len(H), len(M)))
    
        return [(H[i], M[i]) for i in range(n)]

    def vizinhos(C):
        viz = []
        pb = pares_bloqueadores(C)
    
        for h, m in pb:
            novo_C = []
            for h2, m2 in C:
                if h != h2 and m != m2:
                    novo_C.append((h2, m2))
    
            novo_C.append((h, m))
            viz.append(novo_C)
    
        return viz

    def pontos(C):
        casados = set()
    
        for h, m in C:
            casados.add(h)
            casados.add(m)
    
        solteiros = (set(H) | set(M)) - casados
    
        pb = pares_bloqueadores(C)
    
        return len(solteiros) + len(pb)

    atual = casamento_aleatorio()
    atual_pontos = pontos(atual)

    for i in range(n_passos):
        print("step: " + str(i))
        melhor_viz = atual
        melhor_pontos = atual_pontos

        for viz in vizinhos(atual):
            viz_pontos = pontos(viz)

            if  viz_pontos < melhor_pontos:
                melhor_viz = viz
                melhor_pontos = viz_pontos

        if melhor_viz == atual:
            break

        atual = melhor_viz
        atual_pontos = melhor_pontos

    return atual

if __name__ == "__main__":
    rh, rm = gerador.gerar_caso_teste(100,100,0.3,0.3)  

    H = range(100)
    M = range(100)

    ls = local_search(H, M, rh, rm, 100)
    print(ls)
    print(len(ls))
