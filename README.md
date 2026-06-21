# 🚗 Calculadora de Gasto de Combustível

> Uma aplicação Python profissional para calcular custos de combustível com interface gráfica, CLI, web e histórico persistente.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🎯 Funcionalidades

✅ **Cálculo Simples**
- Calcula custo e litros necessários
- Suporta múltiplos combustíveis
- Validação robusta de entrada

✅ **Interface Gráfica (GUI)**
- GUI moderna com Tkinter
- Múltiplas abas (Cálculo, Comparação, Histórico, Trajetos)
- Tema escuro profissional

✅ **Interface Web**
- API REST com Flask
- Dashboard interativo
- Comparação visual de combustíveis

✅ **CLI Poderosa**
- Modo interativo
- Modo argumentos
- Histórico persistente
- Comparação rápida

✅ **Comparação de Combustíveis**
- Gasolina, Etanol, Diesel, GNV
- Análise de economia
- Recomendações

✅ **Histórico Persistente**
- Salva em JSON
- Acesso rápido
- Limpeza manual

## 📦 Instalação

### 1. Clonar Repositório
```bash
git clone https://github.com/IcaroLeite-Uarini-AM-Brasil/Calculadora-de-Gas.git
cd Calculadora-de-Gas
```

### 2. Criar Ambiente Virtual
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### 1️⃣ Interface Gráfica (Recomendado)
```bash
python gui_calculadora.py
```
- Clique em abas para diferentes funcionalidades
- Preencha os campos
- Veja resultados em tempo real

### 2️⃣ Aplicação Web
```bash
python app.py
```
- Acesse: http://localhost:5000
- Dashboard interativo
- Responsivo para mobile

### 3️⃣ Linha de Comando (CLI)

**Modo Interativo:**
```bash
python calculadora_gas.py
```

**Modo Argumentos:**
```bash
python calculadora_gas.py -d 100 -c 12 -p 6.50
```

**Ver Histórico:**
```bash
python calculadora_gas.py --historico
```

**Comparar Combustíveis:**
```bash
python calculadora_gas.py --comparar -d 100 -c 12
```

**Limpar Histórico:**
```bash
python calculadora_gas.py --limpar-historico
```

### 4️⃣ Como Biblioteca
```python
from calculadora_gas import CalculadoraGas

calc = CalculadoraGas()

# Cálculo simples
custo, litros = calc.calcular_gasto_combustivel(
    distancia=100,
    consumo_medio=12,
    preco_litro=6.50
)
print(f"Custo: R$ {custo:.2f}")
print(f"Litros: {litros:.2f}")

# Comparar combustíveis
resultado = calc.comparar_combustiveis(100, 12)
for combustivel, dados in resultado.items():
    print(f"{combustivel}: R$ {dados['custo']:.2f}")

# Múltiplos trajetos
trajetos = [
    {"distancia": 100, "consumo": 10, "preco": 6.50},
    {"distancia": 50, "consumo": 10, "preco": 6.50}
]
resultado = calc.calcular_multiplos_trajetos(trajetos)
print(f"Total: R$ {resultado['total_custo']:.2f}")
```

## 🧪 Testes

### Executar Todos os Testes
```bash
pytest test_calculadora_gas.py -v
```

### Cobertura de Testes
```bash
pytest test_calculadora_gas.py --cov=calculadora_gas --cov-report=html
```

### Testes Disponíveis
- ✅ Cálculos básicos
- ✅ Validações de entrada
- ✅ Múltiplos trajetos
- ✅ Comparação de combustíveis
- ✅ Gerenciamento de histórico
- ✅ Casos extremos

## 📁 Estrutura do Projeto

```
Calculadora-de-Gas/
├── calculadora_gas.py       # Módulo principal
├── gui_calculadora.py       # Interface gráfica
├── app.py                   # Aplicação web (Flask)
├── test_calculadora_gas.py  # Testes unitários
├── requirements.txt         # Dependências
├── README.md               # Este arquivo
├── LICENSE                 # MIT License
└── templates/              # Templates web
    ├── index.html
    ├── calcular.html
    └── comparacao.html
```

## 💻 Requisitos do Sistema

- Python 3.8+
- pip ou conda
- 50 MB de espaço

## 📊 Exemplos de Saída

### Cálculo Simples
```
==================================================
💰 Custo total estimado: R$ 65.00
⛽ Litros necessários: 10.00 L
🔋 Combustível: GASOLINA
==================================================
```

### Comparação
```
🔥 Comparação de Combustíveis:
==================================================
GASOLINA: R$ 65.00 (10.00L)
ETANOL: R$ 45.00 (10.00L)
DIESEL: R$ 62.00 (10.00L)
GNV: R$ 40.00 (10.00L)
==================================================
```

## 🐛 Bugs Conhecidos

- Nenhum no momento. Reporte em: Issues

## 🚀 Roadmap

- [ ] Suporte a mais combustíveis
- [ ] Integração com APIs de preço
- [ ] Gráficos históricos
- [ ] Notificações de preço
- [ ] App móvel

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a Licença MIT - veja [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Ícaro Leite**
- GitHub: [@IcaroLeite-Uarini-AM-Brasil](https://github.com/IcaroLeite-Uarini-AM-Brasil)
- Projeto: DIO.me

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato.

---

**Feito com ❤️ em Python**
