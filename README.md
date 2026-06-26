# grafos-U3

Trabalho da terceira unidade da disciplina de Grafos. 

O projeto consiste em um Sistema de Caronas baseado no Problema dos Casamentos Estáveis (*Stable Marriage SMP*), adaptado para lidar com complicadores reais como listas de preferências incompletas e empates.

## Algoritmos Implementados

Os códigos com as regras de negócio e resoluções dos algoritmos estão localizados na pasta `src/algoritmos/`:

* **Gale-Shapley (`src/algoritmos/gale_shapley.py`):** Algoritmo clássico exato que encontra uma solução estável em tempo polinomial para cenários ideais.
* **Busca Local / Local Search (`src/algoritmos/local_search.py`):** Abordagem heurística desenvolvida para buscar casamentos máximos e minimizar a existência de pares bloqueadores em cenários complexos (com empates e listas incompletas, onde o problema se torna NP-difícil).

## Como Executar

Para rodar o menu interativo e testar os algoritmos ou gerar análises de complexidade, execute o seguinte comando a partir da raiz do projeto:

```bash
python3 src/main.py
```

## Casos Testes

### O Cenário Ideal
teste_01_base.txt 
Parâmetros: N=10, M=10, p1=0.0, p2=0.0

### Oferta x Demanda
teste_02_desproporcional.txt
Parâmetros: N=5, M=15, p1=0.0, p2=0.0


### Listas Incompletas
teste_03_exigentes.txt
Parâmetros: N=20, M=20, p1=0.4, p2=0.0

### Preferências Iguais
teste_04_empates.txt
Parâmetros: N=15, M=15, p1=0.0, p2=0.6

### Teste de Estresse
teste_05_caos.txt 
Parâmetros: N=60, M=60, p1=0.2, p2=0.3
