# Risco-de-Pagamento-de-Energia-ML

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-brightgreen)

Modelo de machine learning para previsão de inadimplência no pagamento de contas de energia elétrica.

## 📋 Sobre o Projeto

Este projeto desenvolve um modelo preditivo para identificar clientes com potencial risco de inadimplência no pagamento de contas de energia elétrica. A solução utiliza técnicas de machine learning para analisar padrões históricos de pagamento e características dos consumidores.

## 🎯 Objetivos

- Prever a probabilidade de inadimplência de clientes
- Identificar fatores que influenciam o não pagamento de contas
- Fornecer insights para ações preventivas
- Reduzir perdas financeiras por inadimplência

## 📊 Dataset

O projeto utiliza um dataset sintético com mais de 65.000 registros contendo:

- **Dados do cliente**: Perfil consumidor, tipo de unidade consumidora
- **Histórico financeiro**: Valores, datas de vencimento e pagamento
- **Informações contratuais**: Situação do contrato, tipo de tarifa
- **Dados temporais**: Meses/anos de referência das faturas

### Estrutura Principal do Dataset:

| Coluna | Descrição | Tipo |
|--------|-----------|------|
| `NUMCDC_VINCULADO` | Identificador da unidade consumidora | Texto |
| `SITUACAO_UC` | Situação da unidade (Ligada/Desligada) | Categórico |
| `DATA_VENCIMENTO` | Data de vencimento da fatura | Data |
| `DATA_PAGAMENTO` | Data efetiva de pagamento | Data |
| `DIAS_VENCIDOS` | Dias em atraso (se aplicável) | Numérico |
| `VALOR_EMISSAO` | Valor original da fatura | Numérico |
| `TIPO_UC` | Classificação do tipo de consumidor | Categórico |
| `STATUS_HOSPITAL` | Indica se é unidade hospitalar | Booleano |

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Pandas** - Manipulação de dados
- **Scikit-learn** - Modelos de machine learning
- **XGBoost/LightGBM** - Algoritmos de boosting
- **Matplotlib/Seaborn** - Visualização de dados
- **Jupyter Notebook** - Análise exploratória

## 📁 Estrutura do Projeto

```
Risco-de-Pagamento-de-Energia-ML/
│
├── data/
│   ├── raw/                 # Dados brutos
│   ├── processed/           # Dados processados
│   └── synthetic/           # Dados sintéticos gerados
│
├── notebooks/
│   ├── 01_eda.ipynb        # Análise exploratória
│   ├── 02_preprocessing.ipynb  # Pré-processamento
│   └── 03_modeling.ipynb   # Modelagem
│
├── src/
│   ├── data_processing.py   # Funções de processamento
│   ├── feature_engineering.py # Engenharia de features
│   └── model_training.py    # Treinamento de modelos
│
├── models/                  # Modelos treinados
├── results/                 # Resultados e métricas
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/Risco-de-Pagamento-de-Energia-ML.git
cd Risco-de-Pagamento-de-Energia-ML

# Instalar dependências
pip install -r requirements.txt
```

### Execução Básica

```python
# Exemplo de uso do modelo
from src.model_training import EnergyPaymentModel

# Carregar e preparar dados
model = EnergyPaymentModel()
model.load_data('data/processed/dataset_final.csv')

# Treinar modelo
model.train()

# Fazer previsões
predictions = model.predict(new_data)
```

## 📈 Métricas de Performance

O modelo será avaliado com base nas seguintes métricas:

- **AUC-ROC** - Curva ROC e área sob a curva
- **Precision/Recall** - Balanceamento entre falsos positivos/negativos
- **F1-Score** - Média harmônica entre precisão e recall
- **Matriz de Confusão** - Visualização dos acertos e erros

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **Seu Nome** - *Desenvolvimento inicial* - [SeuGitHub](https://github.com/matheuslmarchetti)

## 🎯 Próximos Passos

- [ ] Desenvolvimento de API para deployment
- [ ] Dashboard interativo para visualização
- [ ] Integração com sistemas existentes
- [ ] Modelo de explicação de previsões (SHAP/LIME)

## 📞 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato através das issues do repositório ou pelo [LinkedIn](www.linkedin.com/in/matheuslunguinhomarchetti)

---

**Nota**: Este projeto utiliza dados sintéticos para desenvolvimento e teste de modelos. Em produção, devem ser utilizados dados reais seguindo as regulamentações de proteção de dados.
