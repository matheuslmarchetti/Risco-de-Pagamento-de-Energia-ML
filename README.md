# Risco-de-Pagamento-de-Energia-ML

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
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

## 📊 Dataset Sintético para Previsão de Inadimplência

### Visão Geral dos Dados

Este projeto utiliza um **dataset sintético** gerado artificialmente, contendo **mais de 65.000 registros** com informações simuladas de consumo e pagamento de energia elétrica. Os dados foram criados para desenvolver um modelo preditivo de inadimplência **100% conformes com a LGPD e GDPR**, garantindo a privacidade e segurança das informações.

#### 🗂️ Estrutura Principal

| Coluna | Descrição | Tipo |
|--------|-----------|------|
| `NUMCDC_VINCULADO` | Identificador único da unidade consumidora | Texto |
| `SITUACAO_UC` | Situação da unidade (Ligada/Desligada) | Categórico |
| `DATA_VENCIMENTO` | Data de vencimento da fatura | Data |
| `DATA_PAGAMENTO` | Data efetiva de pagamento | Data |
| `DIAS_VENCIDOS` | Dias em atraso (se aplicável) | Numérico |
| `VALOR_EMISSAO` | Valor original da fatura | Numérico |
| `TIPO_UC` | Classificação do tipo de consumidor | Categórico |
| `STATUS_HOSPITAL` | Indica se é unidade hospitalar | Booleano |

#### 🎯 Dados Incluídos

- **Perfil do consumidor**: Tipo de unidade consumidora, classe (Residencial, Comercial, Industrial, etc.)
- **Histórico financeiro**: Valores de fatura, datas de vencimento, pagamento e dias de atraso
- **Informações contratuais**: Situação do contrato, tipo de tarifa, forma de envio da conta
- **Dados temporais**: Meses/anos de referência das faturas

#### ✅ Principais Cuidados na Geração

- **Privacidade garantida**: Dados 100% sintéticos, sem qualquer informação real de clientes
- **Realismo estatístico**: Valores e distribuições condizentes com o mercado energético
- **Relações consistentes**: Vínculos preservados entre unidades consumidoras e clientes
- **Variabilidade controlada**: Dados faltantes simulados para representar cenários reais
- **Lógica temporal**: Datas e prazos de pagamento gerados com base em regras realistas

#### 🚀 Objetivo

Este dataset serve como base para o desenvolvimento de um modelo de machine learning capaz de identificar padrões de inadimplência, permitindo ações preventivas e redução de perdas financeiras no setor energético.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **Pandas** - Manipulação de dados
- **Scikit-learn** - Modelos de machine learning
- **XGBoost/LightGBM** - Algoritmos de boosting
- **Matplotlib/Seaborn** - Visualização de dados
- **Jupyter Notebook** - Análise exploratória

## 📁 Estrutura do Projeto

```
Risco-de-Pagamento-de-Energia-ML/
│
├── 📊 data/
│   ├── 📂 raw/                 # Dados brutos (arquivo synthetic_data.parquet)
│   └── 📂 processed/           # Dados processados e preparados para o modelo
│
├── 🐍 src/
│   ├── generate_synthetic_data.py  # Script para gerar o dataset sintético
│   ├── data_processing.py         # Funções para limpeza e transformação
│   └── feature_engineering.py     # Criação de novas variáveis preditivas
│
├── 📓 notebooks/
│   ├── 01_eda.ipynb              # Análise exploratória e visualizações
│   ├── 02_preprocessing.ipynb    # Pré-processamento dos dados
│   └── 03_modeling.ipynb         # Desenvolvimento do modelo preditivo
│
├── 🤖 models/                    # Modelos treinados salvos (.pkl)
├── 📈 results/                   # Resultados, métricas e gráficos
├── 📋 reports/                   # Relatórios e documentação
├── ✅ tests/                     # Scripts de teste para o código (Pytest)
└── 📄 README.md                  # Instruções do projeto
```
<!--
## 🚀 Como Executar (Em Desenvolvimento)

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

## 📈 Métricas de Performance (Em Desenvolvimento)

O modelo será avaliado com base nas seguintes métricas:

- **AUC-ROC** - Curva ROC e área sob a curva
- **Precision/Recall** - Balanceamento entre falsos positivos/negativos
- **F1-Score** - Média harmônica entre precisão e recall
- **Matriz de Confusão** - Visualização dos acertos e erros

## 🤝 Contribuição (Em Desenvolvimento)

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

-->

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **Matheus L. Marchetti** - *Desenvolvimento inicial* - [GitHub](https://github.com/matheuslmarchetti)

## 🎯 Próximos Passos

**🟢 CONCLUÍDO**
- [x] Geração do dataset sintético com mais de 65.000 registros

**🔵 PRÓXIMAS ETAPAS (EM ANDAMENTO)**
- [ ] Análise exploratória de dados (EDA) e feature engineering
- [ ] Desenvolvimento e validação do modelo preditivo
- [ ] Otimização de hiperparâmetros e validação cruzada

**⚪ FUTURAS ETAPAS**
- [ ] Desenvolvimento de API para deployment
- [ ] Dashboard interativo para visualização
- [ ] Modelo de explicação de previsões (SHAP/LIME)
- [ ] Integração com sistemas existentes

Esta versão deixa claro que:
1. ✅ A geração do dataset já foi concluída
2. 🔵 As próximas etapas imediatas são relacionadas à análise e modelagem
3. ⚪ As etapas de deployment e visualização são futuras

## 📞 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato através das issues do repositório ou pelo [LinkedIn](https://www.linkedin.com/in/matheuslunguinhomarchetti/)

---

**Nota**: Este projeto utiliza dados sintéticos para desenvolvimento e teste de modelos. Em produção, devem ser utilizados dados reais seguindo as regulamentações de proteção de dados.
