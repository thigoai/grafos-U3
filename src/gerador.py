import random
import os


def gerar_caso_teste(n, m, p1, p2):
    """
    n: número de funcionários oferecendo carona
    m: número de funcionários recebendo carona 
    p1: probabilidade de remover um parceiro da lista 
    p2: probabilidade de gerar um empate
    """
    # Algoritmo de Gent e Prosser (adaptado)
    while True:
        
        # Preferências aleatórias
        l1 = {i: random.sample(range(1, m + 1), m) for i in range(1, n + 1)}
        l2 = {j: random.sample(range(1, n + 1), n) for j in range(1, m + 1)}

        recomece = False

        for i in range(1, n + 1):
            for j in list(l1[i]):
                p = random.random()
                if p <= p1:
                    l1[i].remove(j)
                    l2[j].remove(i)

            if not l1[i]: 
                recomece = True
                break

        if recomece:
            continue
            
        ranks1 = {}
        for i in range(1, n + 1):
            ranks1[i] = {}
            if l1[i]:
                ranks1[i][l1[i][0]] = 1
                rank_atual = 1
                for k in range(1, len(l1[i])):
                    if random.random() > p2:
                        rank_atual += 1
                    
                    ranks1[i][l1[i][k]] = rank_atual

        ranks2 = {}
        for j in range(1, m + 1):
            ranks2[j] = {}
            if l2[j]:
                ranks2[j][l2[j][0]] = 1
                rank_atual = 1
                for k in range(1, len(l2[j])):
                    if random.random() > p2:
                        rank_atual += 1

                    ranks2[j][l2[j][k]] = rank_atual

        return ranks1, ranks2

def salvar_caso_teste(nome_arquivo, n, m, p1, p2):
    ranks1, ranks2 = gerar_caso_teste(n, m, p1, p2)
    
    os.makedirs("../casos_teste", exist_ok=True)
    caminho_completo = os.path.join("../casos_teste", nome_arquivo)
    
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        f.write(f"{n} {m}\n") 
        
        f.write("Oferecem Carona:\n")
        for i, prefs in ranks1.items():
            f.write(f"{i}: {prefs}\n")
            
        f.write("Recebem Carona:\n")
        for j, prefs in ranks2.items():
            f.write(f"{j}: {prefs}\n")
            


if __name__ == "__main__":
    
    salvar_caso_teste("caso_1.txt", n=5, m=5, p1=0, p2=0)