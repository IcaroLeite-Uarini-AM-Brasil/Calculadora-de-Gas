# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [2.0.0] - 2026-06-21

### ✨ Adicionado
- Interface gráfica completa com Tkinter
  - Abas para Cálculo, Comparação, Histórico e Múltiplos Trajetos
  - Tema escuro moderno
  - Exibição formatada de resultados

- Aplicação Web com Flask
  - Dashboard interativo
  - API REST completa
  - Responsivo para mobile

- Testes unitários com pytest
  - Cobertura completa de funcionalidades
  - Testes de validação
  - Casos extremos

- Novo módulo `CalculadoraGas` com:
  - Comparação de múltiplos combustíveis
  - Cálculo de múltiplos trajetos
  - Histórico persistente em JSON
  - Validação robusta

- Documentação completa
  - README detalhado
  - Exemplos de uso
  - Guia de instalação
  - Docstrings em todo código

### 🔧 Modificado
- Refatoração completa do código original
- Melhor tratamento de erros
- Type hints em todas as funções
- Mensagens de erro mais descritivas

### 🐛 Corrigido
- Validação de entrada mais rigorosa
- Tratamento de exceções melhorado
- Histórico não salva se houver erro

### 📦 Dependências
- Flask 2.3.3 para web
- pytest 7.4.2 para testes
- black 23.9.1 para formatting

## [1.0.0] - 2026-01-10

### ✨ Adicionado
- Versão inicial do projeto
- Cálculo básico de combustível
- CLI com argparse
- Modo interativo

---

**Formato baseado em [Keep a Changelog](https://keepachangelog.com/)**
