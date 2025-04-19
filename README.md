# 📊 Análise de Correlações com Teoria dos Grafos

Este projeto aplica conceitos de teoria dos grafos para analisar a correlação entre canais de sensores com base em dados experimentais. A análise é feita utilizando grafos ponderados, árvores geradoras mínimas e visualizações gráficas.

---

## 📁 Arquivo de Entrada

- `LM_data.txt`: arquivo contendo os dados de sensores.
  - A primeira coluna representa o tempo (removida durante o pré-processamento).
  - As colunas de 27 a 30 são descartadas por não serem relevantes à análise.
  - Restam 26 canais analisados.

---

## 📚 Bibliotecas Utilizadas

- `pandas`
- `numpy`
- `networkx`
- `matplotlib`
- `scipy.stats`

---

## 📌 Etapas do Código

1. **Leitura dos Dados:**  
   O arquivo é lido e tratado para remover colunas desnecessárias.

2. **Matriz de Correlação (Pearson):**  
   Calcula-se a correlação entre todos os pares de canais (exceto correlações com eles mesmos).

3. **Criação do Grafo Geral:**  
   Um grafo é construído com os canais como nós e correlações positivas como arestas ponderadas.

4. **Grafos por Faixa de Correlação:**
   - Correlações entre `0.0 e 0.5` → grafo com arestas laranjas.
   - Correlações entre `0.51 e 1.0` → grafo com arestas verdes.

5. **Árvores Geradoras Mínimas:**
   - **Prim:** Gera a árvore de forma incremental.
   - **Kruskal:** Ordena as arestas por peso e conecta os componentes.

6. **Comparação Visual (Prim vs Kruskal):**  
   Mostra lado a lado as árvores geradas por ambos os algoritmos.

---

## 🧠 Conclusão

> O algoritmo de **Prim** constrói a árvore de forma incremental, sempre conectando o vértice mais próximo ainda não visitado.  
> O algoritmo de **Kruskal**, por outro lado, ordena todas as arestas e vai conectando os vértices de maneira a evitar ciclos.  
> **Ambos produzem a mesma árvore geradora mínima**, mas usam estratégias diferentes para alcançá-la.

---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 e as bibliotecas necessárias instaladas.
2. Coloque o arquivo `LM_data.txt` no caminho correto (ou ajuste o caminho no código).
3. Execute o script Python.

```bash
python nome_do_script.py
```

---

## 📌 Observação

As visualizações gráficas dos grafos são fundamentais para a análise, e são exibidas automaticamente durante a execução do código.

---
