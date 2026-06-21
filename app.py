#!/usr/bin/env python3
"""
app.py - Aplicação Web com Flask

Interface web com:
- Dashboard interativo
- API REST
- Comparação visual
- Histórico
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from calculadora_gas import CalculadoraGas
import json

app = Flask(__name__)
CORS(app)
calc = CalculadoraGas()


@app.route('/')
def index():
    """Página inicial."""
    return render_template('index.html')


@app.route('/api/calcular', methods=['POST'])
def api_calcular():
    """API: Calcula gasto de combustível."""
    try:
        data = request.json
        distancia = float(data.get('distancia', 0))
        consumo = float(data.get('consumo', 0))
        preco = float(data.get('preco', 0))
        
        custo, litros = calc.calcular_gasto_combustivel(
            distancia, consumo, preco
        )
        
        calc.salvar_calculo({
            'distancia': distancia,
            'consumo': consumo,
            'preco': preco,
            'custo_total': custo,
            'litros': litros
        })
        
        return jsonify({
            'sucesso': True,
            'custo': f"{custo:.2f}",
            'litros': f"{litros:.2f}"
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': str(e)}), 400


@app.route('/api/comparar', methods=['POST'])
def api_comparar():
    """API: Compara combustíveis."""
    try:
        data = request.json
        distancia = float(data.get('distancia', 0))
        consumo = float(data.get('consumo', 0))
        
        resultado = calc.comparar_combustiveis(distancia, consumo)
        
        return jsonify({
            'sucesso': True,
            'comparacao': {
                comb: {
                    'custo': f"{dados['custo']:.2f}",
                    'litros': f"{dados['litros']:.2f}",
                    'preco': f"{dados['preco_litro']:.2f}"
                }
                for comb, dados in resultado.items()
            }
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': str(e)}), 400


@app.route('/api/historico')
def api_historico():
    """API: Retorna histórico."""
    historico = calc.listar_historico(limite=20)
    return jsonify({
        'sucesso': True,
        'historico': historico
    })


@app.route('/api/limpar-historico', methods=['DELETE'])
def api_limpar():
    """API: Limpa histórico."""
    calc.limpar_historico()
    return jsonify({'sucesso': True, 'mensagem': 'Histórico limpo'})


@app.errorhandler(404)
def not_found(error):
    """Tratamento de página não encontrada."""
    return jsonify({'erro': 'Página não encontrada'}), 404


@app.errorhandler(500)
def server_error(error):
    """Tratamento de erro de servidor."""
    return jsonify({'erro': 'Erro interno do servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
