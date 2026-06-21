#!/usr/bin/env python3
"""
test_calculadora_gas.py - Testes Unitários Completos

Testes com pytest cobrindo:
- Cálculos básicos
- Validações
- Casos extremos
- Múltiplos trajetos
- Comparação de combustíveis
"""

import pytest
import json
from pathlib import Path
from calculadora_gas import CalculadoraGas


class TestCalculadoraGasBasico:
    """Testes básicos de cálculo."""
    
    def test_calculo_simples(self):
        """Testa cálculo simples."""
        custo, litros = CalculadoraGas.calcular_gasto_combustivel(
            distancia=100,
            consumo_medio=10,
            preco_litro=6.50
        )
        assert litros == 10.0
        assert custo == 65.0
    
    def test_calculo_com_decimais(self):
        """Testa cálculo com números decimais."""
        custo, litros = CalculadoraGas.calcular_gasto_combustivel(
            distancia=150.5,
            consumo_medio=12.5,
            preco_litro=6.25
        )
        assert abs(litros - 12.04) < 0.01
        assert abs(custo - 75.25) < 0.01
    
    def test_distancia_zero(self):
        """Testa com distância zero."""
        custo, litros = CalculadoraGas.calcular_gasto_combustivel(0, 10, 6.50)
        assert litros == 0.0
        assert custo == 0.0
    
    def test_preco_zero(self):
        """Testa com preço zero."""
        custo, litros = CalculadoraGas.calcular_gasto_combustivel(100, 10, 0)
        assert litros == 10.0
        assert custo == 0.0


class TestValidacoes:
    """Testes de validação de entrada."""
    
    def test_consumo_zero(self):
        """Consumo zero deve gerar erro."""
        with pytest.raises(ValueError):
            CalculadoraGas.calcular_gasto_combustivel(100, 0, 6.50)
    
    def test_consumo_negativo(self):
        """Consumo negativo deve gerar erro."""
        with pytest.raises(ValueError):
            CalculadoraGas.calcular_gasto_combustivel(100, -5, 6.50)
    
    def test_distancia_negativa(self):
        """Distância negativa deve gerar erro."""
        with pytest.raises(ValueError):
            CalculadoraGas.calcular_gasto_combustivel(-50, 10, 6.50)
    
    def test_preco_negativo(self):
        """Preço negativo deve gerar erro."""
        with pytest.raises(ValueError):
            CalculadoraGas.calcular_gasto_combustivel(100, 10, -6.50)


class TestMultiplosTrajetos:
    """Testes para múltiplos trajetos."""
    
    def test_multiplos_trajetos_simples(self):
        """Testa cálculo de múltiplos trajetos."""
        calc = CalculadoraGas()
        trajetos = [
            {"distancia": 100, "consumo": 10, "preco": 6.50},
            {"distancia": 50, "consumo": 10, "preco": 6.50},
        ]
        resultado = calc.calcular_multiplos_trajetos(trajetos)
        
        assert resultado["total_litros"] == 15.0
        assert resultado["total_custo"] == 97.50
        assert len(resultado["detalhes"]) == 2
    
    def test_multiplos_trajetos_vazio(self):
        """Testa com lista vazia."""
        calc = CalculadoraGas()
        resultado = calc.calcular_multiplos_trajetos([])
        
        assert resultado["total_litros"] == 0.0
        assert resultado["total_custo"] == 0.0
        assert resultado["detalhes"] == []


class TestComparacao:
    """Testes para comparação de combustíveis."""
    
    def test_comparar_combustiveis(self):
        """Testa comparação de combustíveis."""
        calc = CalculadoraGas()
        resultado = calc.comparar_combustiveis(distancia=100, consumo_medio=10)
        
        assert "gasolina" in resultado
        assert "etanol" in resultado
        assert "diesel" in resultado
        assert "gnv" in resultado
        
        # Gasolina deve ser mais cara que etanol
        assert resultado["gasolina"]["custo"] > resultado["etanol"]["custo"]


class TestHistorico:
    """Testes para gerenciamento de histórico."""
    
    def setup_method(self):
        """Setup antes de cada teste."""
        self.calc = CalculadoraGas()
        self.calc.limpar_historico()
    
    def teardown_method(self):
        """Cleanup após cada teste."""
        self.calc.limpar_historico()
    
    def test_salvar_calculo(self):
        """Testa salvar cálculo no histórico."""
        self.calc.salvar_calculo({
            "distancia": 100,
            "consumo": 10,
            "preco": 6.50,
            "custo_total": 65.0,
            "litros": 10.0
        })
        
        assert len(self.calc.historico) == 1
        assert self.calc.historico[0]["distancia"] == 100
    
    def test_listar_historico(self):
        """Testa listagem do histórico."""
        for i in range(15):
            self.calc.salvar_calculo({
                "distancia": 100 + i,
                "consumo": 10,
                "preco": 6.50,
                "custo_total": 65.0 + i,
                "litros": 10.0
            })
        
        historico = self.calc.listar_historico(limite=10)
        assert len(historico) == 10
    
    def test_limpar_historico(self):
        """Testa limpeza do histórico."""
        self.calc.salvar_calculo({"distancia": 100})
        assert len(self.calc.historico) > 0
        
        self.calc.limpar_historico()
        assert len(self.calc.historico) == 0


class TestCasosExtremos:
    """Testes para casos extremos."""
    
    def test_numero_muito_grande(self):
        """Testa com números muito grandes."""
        custo, litros = CalculadoraGas.calcular_gasto_combustivel(
            1_000_000, 10, 100
        )
        assert litros == 100_000
        assert custo == 10_000_000
    
    def test_numero_muito_pequeno(self):
        """Testa com números muito pequenos."""
        custo, litros = CalculadoraGas.calcular_gasto_combustivel(
            0.001, 100, 0.001
        )
        assert abs(litros - 0.00001) < 1e-10
        assert abs(custo - 1e-8) < 1e-10


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
