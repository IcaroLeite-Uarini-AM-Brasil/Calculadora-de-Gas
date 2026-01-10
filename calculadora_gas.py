#!/usr/bin/env python3
"""
calculadora_gas.py

Calculadora de gasto de combustível:
- Função reutilizável calcular_gasto_combustivel
- CLI com argparse + modo interativo quando argumentos não são fornecidos
"""

from __future__ import annotations
import argparse
import sys
from typing import Tuple


def calcular_gasto_combustivel(distancia: float, consumo_medio: float, preco_litro: float) -> Tuple[float, float]:
    """
    Calcula o custo total de combustível e litros necessários para uma viagem.

    Args:
        distancia (float): Distância total a ser percorrida em km. Deve ser >= 0.
        consumo_medio (float): Consumo médio do veículo em km/l. Deve ser > 0.
        preco_litro (float): Preço do combustível por litro em R$. Deve ser >= 0.

    Returns:
        Tuple[float, float]: (custo_total_em_reais, litros_necessarios)

    Raises:
        ValueError: Se entradas forem inválidas (consumo_medio <= 0 ou valores negativos).
    """
    if consumo_medio <= 0:
        raise ValueError("Consumo médio deve ser maior que zero.")
    if distancia < 0:
        raise ValueError("Distância não pode ser negativa.")
    if preco_litro < 0:
        raise ValueError("Preço por litro não pode ser negativo.")

    litros_necessarios = distancia / consumo_medio
    custo_total = litros_necessarios * preco_litro
    return custo_total, litros_necessarios


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculadora de gasto de combustível")
    parser.add_argument("--distancia", "-d", type=float, help="Distância total em km")
    parser.add_argument("--consumo", "-c", type=float, help="Consumo médio em km/l")
    parser.add_argument("--preco", "-p", type=float, help="Preço do combustível por litro em R$")
    return parser.parse_args()


def solicitar_float(prompt: str) -> float:
    while True:
        try:
            valor = float(input(prompt).strip())
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


def main() -> int:
    args = parse_args()

    try:
        if args.distancia is None or args.consumo is None or args.preco is None:
            # Modo interativo (se qualquer argumento estiver faltando)
            print("--- Mini Calculadora de Gasto de Combustível ---")
            distancia = solicitar_float("Digite a distância total percorrida em km: ")
            consumo_medio = solicitar_float("Digite o consumo médio do veículo em km/litro: ")
            preco_litro = solicitar_float("Digite o preço do combustível por litro em R$: ")
        else:
            distancia = args.distancia
            consumo_medio = args.consumo
            preco_litro = args.preco

        custo_total, litros_necessarios = calcular_gasto_combustivel(distancia, consumo_medio, preco_litro)

        print(f"\nCusto total estimado da viagem: R$ {custo_total:.2f}")
        print(f"Litros de combustível necessários: {litros_necessarios:.2f} L")
        return 0

    except ValueError as ve:
        print(f"Erro: {ve}")
        return 2
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
