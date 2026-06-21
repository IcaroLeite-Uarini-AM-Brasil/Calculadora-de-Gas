#!/usr/bin/env python3
"""
calculadora_gas.py - Calculadora de Gasto de Combustível Profissional

Módulo principal com funcionalidades avançadas:
- Cálculo de combustível com validação robusta
- Suporte a múltiplos combustíveis e conversão
- Histórico de cálculos persistente (JSON)
- CLI com argparse
- Modo interativo inteligente
"""

from __future__ import annotations
import argparse
import sys
import json
from pathlib import Path
from typing import Tuple, Dict, List, Optional
from datetime import datetime


class CalculadoraGas:
    """Classe principal para cálculos de combustível."""
    
    # Preços médios de combustíveis (atualizável)
    COMBUSTIVEIS = {
        "gasolina": 6.50,
        "etanol": 4.50,
        "diesel": 6.20,
        "gnv": 4.00,
    }
    
    HISTORICO_FILE = Path.home() / ".calculadora_gas_historico.json"
    
    def __init__(self):
        """Inicializa a calculadora e carrega histórico."""
        self.historico: List[Dict] = self._carregar_historico()
    
    @staticmethod
    def calcular_gasto_combustivel(
        distancia: float,
        consumo_medio: float,
        preco_litro: float
    ) -> Tuple[float, float]:
        """
        Calcula o custo total e litros necessários.
        
        Args:
            distancia: Distância em km (>= 0)
            consumo_medio: Consumo em km/l (> 0)
            preco_litro: Preço em R$ (>= 0)
        
        Returns:
            Tupla (custo_total, litros_necessarios)
        
        Raises:
            ValueError: Se valores forem inválidos
        """
        if consumo_medio <= 0:
            raise ValueError("❌ Consumo médio deve ser maior que zero.")
        if distancia < 0:
            raise ValueError("❌ Distância não pode ser negativa.")
        if preco_litro < 0:
            raise ValueError("❌ Preço por litro não pode ser negativo.")
        
        litros_necessarios = distancia / consumo_medio
        custo_total = litros_necessarios * preco_litro
        return custo_total, litros_necessarios
    
    def calcular_multiplos_trajetos(self, trajetos: List[Dict]) -> Dict:
        """
        Calcula custo total para múltiplos trajetos.
        
        Args:
            trajetos: Lista de dicts com 'distancia', 'consumo', 'preco'
        
        Returns:
            Dict com totais e detalhes
        """
        total_custo = 0.0
        total_litros = 0.0
        detalhes = []
        
        for i, trajeto in enumerate(trajetos, 1):
            custo, litros = self.calcular_gasto_combustivel(
                trajeto.get("distancia", 0),
                trajeto.get("consumo", 1),
                trajeto.get("preco", 0)
            )
            total_custo += custo
            total_litros += litros
            detalhes.append({
                "trajeto": i,
                "custo": custo,
                "litros": litros
            })
        
        return {
            "total_custo": total_custo,
            "total_litros": total_litros,
            "detalhes": detalhes
        }
    
    def comparar_combustiveis(
        self,
        distancia: float,
        consumo_medio: float
    ) -> Dict[str, Tuple[float, float]]:
        """
        Compara custos entre diferentes combustíveis.
        
        Args:
            distancia: Distância em km
            consumo_medio: Consumo em km/l
        
        Returns:
            Dict com comparação de custos
        """
        resultado = {}
        for combustivel, preco in self.COMBUSTIVEIS.items():
            custo, litros = self.calcular_gasto_combustivel(
                distancia, consumo_medio, preco
            )
            resultado[combustivel] = {
                "custo": custo,
                "litros": litros,
                "preco_litro": preco
            }
        return resultado
    
    def economizar(
        self,
        custo_gasolina: float,
        combustivel_alternativo: str
    ) -> Dict:
        """
        Calcula economia usando combustível alternativo.
        
        Args:
            custo_gasolina: Custo com gasolina
            combustivel_alternativo: Tipo de combustível alternativo
        
        Returns:
            Dict com economias
        """
        if combustivel_alternativo not in self.COMBUSTIVEIS:
            raise ValueError(f"❌ Combustível '{combustivel_alternativo}' não suportado.")
        
        economia = custo_gasolina - (custo_gasolina * 0.8)  # Estimativa
        return {
            "economia": economia,
            "percentual": (economia / custo_gasolina) * 100
        }
    
    def _carregar_historico(self) -> List[Dict]:
        """Carrega histórico de cálculos do arquivo JSON."""
        if self.HISTORICO_FILE.exists():
            try:
                with open(self.HISTORICO_FILE, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️  Erro ao carregar histórico: {e}")
                return []
        return []
    
    def salvar_calculo(self, dados: Dict) -> None:
        """Salva um cálculo no histórico."""
        dados["timestamp"] = datetime.now().isoformat()
        self.historico.append(dados)
        self._salvar_historico()
    
    def _salvar_historico(self) -> None:
        """Salva histórico em arquivo JSON."""
        try:
            with open(self.HISTORICO_FILE, "w") as f:
                json.dump(self.historico, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Erro ao salvar histórico: {e}")
    
    def listar_historico(self, limite: int = 10) -> List[Dict]:
        """Retorna últimos N cálculos do histórico."""
        return self.historico[-limite:]
    
    def limpar_historico(self) -> None:
        """Limpa todo o histórico."""
        self.historico = []
        self._salvar_historico()
        print("✅ Histórico limpo!")


def parse_args() -> argparse.Namespace:
    """Parser de argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="🚗 Calculadora de Gasto de Combustível Profissional",
        epilog="Exemplos:\n"
               "  python calculadora_gas.py -d 100 -c 12 -p 6.50\n"
               "  python calculadora_gas.py --historico\n"
               "  python calculadora_gas.py --comparar -d 100 -c 12",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--distancia", "-d", type=float, help="Distância em km")
    parser.add_argument("--consumo", "-c", type=float, help="Consumo em km/l")
    parser.add_argument("--preco", "-p", type=float, help="Preço por litro em R$")
    parser.add_argument("--combustivel", "-f", default="gasolina", help="Tipo de combustível")
    parser.add_argument("--comparar", action="store_true", help="Comparar combustíveis")
    parser.add_argument("--historico", action="store_true", help="Ver histórico")
    parser.add_argument("--limpar-historico", action="store_true", help="Limpar histórico")
    
    return parser.parse_args()


def solicitar_float(prompt: str, minimo: Optional[float] = None) -> float:
    """Solicita e valida entrada de float."""
    while True:
        try:
            valor = float(input(prompt).strip())
            if minimo is not None and valor < minimo:
                print(f"⚠️  Valor deve ser >= {minimo}")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")


def exibir_resultado(custo: float, litros: float, combustivel: str = "gasolina") -> None:
    """Exibe resultado formatado."""
    print("\n" + "="*50)
    print(f"💰 Custo total estimado: R$ {custo:.2f}")
    print(f"⛽ Litros necessários: {litros:.2f} L")
    print(f"🔋 Combustível: {combustivel.upper()}")
    print("="*50 + "\n")


def modo_interativo(calc: CalculadoraGas) -> int:
    """Modo interativo da calculadora."""
    print("\n🚗 " + "="*48)
    print("  Mini Calculadora de Gasto de Combustível")
    print("="*50)
    
    try:
        distancia = solicitar_float("📏 Distância total (km): ", minimo=0)
        consumo_medio = solicitar_float("⛽ Consumo médio (km/l): ", minimo=0.1)
        preco_litro = solicitar_float("💵 Preço do combustível (R$/l): ", minimo=0)
        
        custo_total, litros = calc.calcular_gasto_combustivel(
            distancia, consumo_meio, preco_litro
        )
        
        exibir_resultado(custo_total, litros)
        
        # Salvar no histórico
        calc.salvar_calculo({
            "distancia": distancia,
            "consumo": consumo_medio,
            "preco": preco_litro,
            "custo_total": custo_total,
            "litros": litros
        })
        
        return 0
    
    except ValueError as ve:
        print(f"❌ Erro: {ve}")
        return 2
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return 1


def main() -> int:
    """Função principal."""
    args = parse_args()
    calc = CalculadoraGas()
    
    try:
        # Limpar histórico
        if args.limpar_historico:
            calc.limpar_historico()
            return 0
        
        # Ver histórico
        if args.historico:
            historico = calc.listar_historico()
            if historico:
                print("\n📋 Últimos Cálculos:")
                print("="*50)
                for i, calc_data in enumerate(historico, 1):
                    print(f"{i}. {calc_data.get('timestamp', 'N/A')}")
                    print(f"   Custo: R$ {calc_data.get('custo_total', 0):.2f}")
                    print(f"   Litros: {calc_data.get('litros', 0):.2f}")
                print("="*50 + "\n")
            else:
                print("📭 Histórico vazio.\n")
            return 0
        
        # Comparar combustíveis
        if args.comparar and args.distancia and args.consumo:
            resultado = calc.comparar_combustiveis(args.distancia, args.consumo)
            print("\n🔥 Comparação de Combustíveis:")
            print("="*50)
            for combustivel, dados in resultado.items():
                print(f"{combustivel.upper()}: R$ {dados['custo']:.2f} ({dados['litros']:.2f}L)")
            print("="*50 + "\n")
            return 0
        
        # Modo CLI
        if args.distancia is not None and args.consumo is not None and args.preco is not None:
            custo_total, litros = calc.calcular_gasto_combustivel(
                args.distancia, args.consumo, args.preco
            )
            exibir_resultado(custo_total, litros, args.combustivel)
            
            calc.salvar_calculo({
                "distancia": args.distancia,
                "consumo": args.consumo,
                "preco": args.preco,
                "custo_total": custo_total,
                "litros": litros,
                "combustivel": args.combustivel
            })
            return 0
        
        # Modo interativo
        return modo_interativo(calc)
    
    except ValueError as ve:
        print(f"❌ Erro: {ve}")
        return 2
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
