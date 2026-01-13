# meuPiá IA – Módulo de Inteligência Artificial

![meuPia](assets/meuPia-ia.png)

## 📖 Overview

> **Nota:** Este é um **plugin oficial** para o compilador [meuPiá](https://www.google.com/search?q=https://github.com/henryhamon/meuPia-core).

**meuPiá IA** é o "cérebro" do ecossistema. Ele traz o poder do *Machine Learning* profissional (via Scikit-Learn) para dentro da sintaxe amigável do Portugol.

O objetivo é permitir que estudantes aprendam conceitos de **Ciência de Dados** — como regressão, classificação, overfit e datasets — sem precisarem lidar com a complexidade de tensores, dataframes ou álgebra linear avançada no início do aprendizado.

**meuPiá IA** fornece:

* **Abstração de Dados:** Converta listas simples do Portugol (`[[1,2], [3,4]]`) automaticamente em matrizes NumPy.
* **Modelos Prontos:** Acesso imediato a algoritmos clássicos como Regressão Linear, KNN, Random Forest e SVR.
* **Persistência:** Salve (`.pkl`) e carregue seus modelos treinados para usar em outros algoritmos ou robôs.

---

## 🚀 Installation

Utilize o gerenciador de pacotes do meuPiá (**mpgp**) para instalar a extensão e suas dependências (`pandas`, `scikit-learn`, `joblib`).

```bash
# No terminal
mpgp instale ia

```

---

## 🛠️ Usage Examples

### 1. Previsão Simples (Regressão Linear)

Ensinando o computador a entender uma sequência numérica simples (x * 10).

```portugol
algoritmo "AprendendoTabuada"
usar "ia"

var previsao: real
inicio
    escreva("Treinando a IA...")

    // Dados de Treino: [Entrada], [Saída Esperada]
    ia_definir_dados(
        [[1], [2], [3], [4], [5]], 
        [10, 20, 30, 40, 50]
    )

    // Cria e treina um modelo linear
    ia_criar_modelo("regressao_linear")
    ia_treinar(0.2) // Usa 20% dos dados para teste

    // Fazendo uma previsão
    // Quanto é 8 * 10?
    previsao <- ia_prever([8])
    
    escreva("A IA acha que 8 * 10 é: ", previsao)
fimalgoritmo

```

### 2. Classificação (Gato ou Cachorro?)

Usando KNN para classificar com base em características (ex: Tamanho e Peso).

```portugol
algoritmo "ClassificadorPet"
usar "ia"

var classe: real
inicio
    // Features: [Tamanho (cm), Peso (kg)]
    // Labels: 0 = Gato, 1 = Cachorro
    ia_definir_dados(
        [[25, 4], [20, 3], [50, 15], [60, 20]], 
        [0, 0, 1, 1]
    )

    ia_criar_modelo("knn_classificador")
    ia_treinar(0.0) // Treina com tudo (exemplo didático)

    // Animal novo: 55cm, 18kg -> O que é?
    classe <- ia_prever([55, 18])

    se classe = 1 entao
        escreva("É um Cachorro!")
    senao
        escreva("É um Gato!")
    fim_se
fimalgoritmo

```

---

## 📚 API Reference

Abaixo estão as funções disponíveis na versão v0.1.0:

### Gestão de Dados

* `ia_definir_dados(matriz_x, vetor_y)`: Carrega os dados na memória.
* `ia_coletar_amostra(lista_features)`: Adiciona uma linha a um buffer temporário (útil para loops de coleta de dados em tempo real).
* `ia_exportar_csv(nome_arquivo)`: Salva o buffer coletado em um arquivo CSV.

### Modelagem

* `ia_criar_modelo(tipo)`: Inicializa um algoritmo de IA.
* `"regressao_linear"`: Para tendências simples.
* `"arvore"`: Árvore de Decisão (Decision Tree).
* `"floresta"`: Random Forest (Robusto para dados ruidosos).
* `"svr"`: Support Vector Regression (Complexo/Não-linear).
* `"gradient_boosting"`: Alta precisão.
* `"knn_classificador"`: Classificação baseada em vizinhos.



### Execução

* `ia_treinar(tamanho_teste)`: Executa o treinamento (`fit`) e exibe a acurácia (`score`). O parâmetro `tamanho_teste` (0.0 a 1.0) define quanto dos dados será separado para validação.
* `ia_prever(lista_entrada)`: Retorna o valor predito pelo modelo para uma nova entrada.

### Persistência

* `ia_salvar(arquivo.pkl)`: Salva o "cérebro" treinado no disco.
* `ia_carregar(arquivo.pkl)`: Carrega um modelo pré-existente.

---

## 🙌 Credits

Desenvolvido como parte do ecossistema educacional **meuPiá** que é desenvolvido com ❤️ por **[@henryhamon](https://github.com/henryhamon)**.

* **Core Compiler:** [meuPia-core](https://www.google.com/search?q=https://github.com/henryhamon/meuPia-core)
* **Engine:** [scikit-learn](https://scikit-learn.org/)