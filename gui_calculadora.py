#!/usr/bin/env python3
"""
gui_calculadora.py - Interface Gráfica com Tkinter

GUI profissional com:
- Abas para diferentes funcionalidades
- Comparação visual de combustíveis
- Histórico persistente
- Temas modernos
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
from pathlib import Path
from datetime import datetime
from calculadora_gas import CalculadoraGas


class CalculadoraGUI:
    """Interface gráfica da calculadora."""
    
    def __init__(self, root):
        """Inicializa a GUI."""
        self.root = root
        self.calc = CalculadoraGas()
        
        self.root.title("🚗 Calculadora de Gasto de Combustível")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Cores
        self.cor_bg = "#2c3e50"
        self.cor_fg = "#ecf0f1"
        self.cor_acento = "#3498db"
        
        self.root.configure(bg=self.cor_bg)
        
        self._criar_interface()
    
    def _criar_interface(self):
        """Cria a interface principal."""
        # Título
        titulo = tk.Label(
            self.root,
            text="🚗 Calculadora de Combustível",
            font=("Arial", 18, "bold"),
            bg=self.cor_bg,
            fg=self.cor_acento
        )
        titulo.pack(pady=10)
        
        # Abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Estilo das abas
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=self.cor_bg)
        style.configure('TNotebook.Tab', padding=[20, 10])
        
        # Criar abas
        self._aba_calculo()
        self._aba_comparacao()
        self._aba_historico()
        self._aba_multiplos()
    
    def _aba_calculo(self):
        """Aba de cálculo simples."""
        frame = tk.Frame(self.notebook, bg=self.cor_bg)
        self.notebook.add(frame, text="📊 Cálculo")
        
        # Campos de entrada
        tk.Label(frame, text="Distância (km):", bg=self.cor_bg, fg=self.cor_fg).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_dist = tk.Entry(frame, width=20)
        self.entry_dist.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame, text="Consumo (km/l):", bg=self.cor_bg, fg=self.cor_fg).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_cons = tk.Entry(frame, width=20)
        self.entry_cons.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame, text="Preço (R$/l):", bg=self.cor_bg, fg=self.cor_fg).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_preco = tk.Entry(frame, width=20)
        self.entry_preco.grid(row=2, column=1, padx=10, pady=5)
        
        # Botão calcular
        btn = tk.Button(
            frame,
            text="Calcular",
            command=self._calcular_simples,
            bg=self.cor_acento,
            fg=self.cor_fg,
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Resultado
        tk.Label(frame, text="Resultado:", bg=self.cor_bg, fg=self.cor_fg, font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, sticky="w", padx=10)
        
        self.text_resultado = scrolledtext.ScrolledText(
            frame,
            height=8,
            width=50,
            bg="#34495e",
            fg="#2ecc71",
            font=("Courier", 10)
        )
        self.text_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    def _aba_comparacao(self):
        """Aba de comparação de combustíveis."""
        frame = tk.Frame(self.notebook, bg=self.cor_bg)
        self.notebook.add(frame, text="🔥 Comparação")
        
        tk.Label(frame, text="Distância (km):", bg=self.cor_bg, fg=self.cor_fg).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_dist_comp = tk.Entry(frame, width=20)
        self.entry_dist_comp.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame, text="Consumo (km/l):", bg=self.cor_bg, fg=self.cor_fg).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_cons_comp = tk.Entry(frame, width=20)
        self.entry_cons_comp.grid(row=1, column=1, padx=10, pady=5)
        
        btn = tk.Button(
            frame,
            text="Comparar Combustíveis",
            command=self._comparar_combustiveis,
            bg=self.cor_acento,
            fg=self.cor_fg,
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.text_comparacao = scrolledtext.ScrolledText(
            frame,
            height=12,
            width=50,
            bg="#34495e",
            fg="#f39c12",
            font=("Courier", 10)
        )
        self.text_comparacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def _aba_historico(self):
        """Aba de histórico."""
        frame = tk.Frame(self.notebook, bg=self.cor_bg)
        self.notebook.add(frame, text="📋 Histórico")
        
        btn_frame = tk.Frame(frame, bg=self.cor_bg)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(
            btn_frame,
            text="Atualizar",
            command=self._atualizar_historico,
            bg=self.cor_acento,
            fg=self.cor_fg,
            padx=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Limpar Histórico",
            command=self._limpar_historico,
            bg="#e74c3c",
            fg=self.cor_fg,
            padx=10
        ).pack(side=tk.LEFT, padx=5)
        
        self.text_historico = scrolledtext.ScrolledText(
            frame,
            height=15,
            width=50,
            bg="#34495e",
            fg="#9b59b6",
            font=("Courier", 9)
        )
        self.text_historico.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self._atualizar_historico()
    
    def _aba_multiplos(self):
        """Aba para múltiplos trajetos."""
        frame = tk.Frame(self.notebook, bg=self.cor_bg)
        self.notebook.add(frame, text="🛣️ Múltiplos Trajetos")
        
        tk.Label(
            frame,
            text="Cole JSON com lista de trajetos:\n[{\"distancia\": 100, \"consumo\": 10, \"preco\": 6.50}, ...]",
            bg=self.cor_bg,
            fg=self.cor_fg,
            justify=tk.LEFT
        ).pack(padx=10, pady=5)
        
        self.text_multiplos_entrada = scrolledtext.ScrolledText(
            frame,
            height=6,
            width=50,
            bg="#34495e",
            fg="#ecf0f1",
            font=("Courier", 9)
        )
        self.text_multiplos_entrada.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        tk.Button(
            frame,
            text="Calcular Múltiplos Trajetos",
            command=self._calcular_multiplos,
            bg=self.cor_acento,
            fg=self.cor_fg,
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        ).pack(pady=10)
        
        self.text_multiplos_resultado = scrolledtext.ScrolledText(
            frame,
            height=6,
            width=50,
            bg="#34495e",
            fg="#1abc9c",
            font=("Courier", 10)
        )
        self.text_multiplos_resultado.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def _calcular_simples(self):
        """Calcula gasto simples."""
        try:
            distancia = float(self.entry_dist.get())
            consumo = float(self.entry_cons.get())
            preco = float(self.entry_preco.get())
            
            custo, litros = self.calc.calcular_gasto_combustivel(distancia, consumo, preco)
            
            resultado = f"""
╔════════════════════════════════════════╗
║         RESULTADO DO CÁLCULO           ║
╠════════════════════════════════════════╣
║ Distância: {distancia:>28.2f} km
║ Consumo: {consumo:>30.2f} km/l
║ Preço: {preco:>33.2f} R$/l
║ ────────────────────────────────────── ║
║ Litros necessários: {litros:>21.2f} L
║ Custo total: R$ {custo:>26.2f}
╚════════════════════════════════════════╝
            """
            
            self.text_resultado.config(state=tk.NORMAL)
            self.text_resultado.delete("1.0", tk.END)
            self.text_resultado.insert(tk.END, resultado)
            self.text_resultado.config(state=tk.DISABLED)
            
            # Salvar no histórico
            self.calc.salvar_calculo({
                "distancia": distancia,
                "consumo": consumo,
                "preco": preco,
                "custo_total": custo,
                "litros": litros
            })
            
            messagebox.showinfo("✅ Sucesso", "Cálculo realizado e salvo no histórico!")
        
        except ValueError:
            messagebox.showerror("❌ Erro", "Por favor, preencha todos os campos com números válidos!")
    
    def _comparar_combustiveis(self):
        """Compara combustíveis."""
        try:
            distancia = float(self.entry_dist_comp.get())
            consumo = float(self.entry_cons_comp.get())
            
            resultado = self.calc.comparar_combustiveis(distancia, consumo)
            
            texto = "\n╔════════════════════════════════════════╗\n"
            texto += "║    COMPARAÇÃO DE COMBUSTÍVEIS          ║\n"
            texto += "╠════════════════════════════════════════╣\n"
            
            for comb, dados in resultado.items():
                texto += f"║ {comb.upper():>8} - R$ {dados['custo']:>7.2f} | {dados['litros']:>6.2f}L ║\n"
            
            texto += "╚════════════════════════════════════════╝\n"
            
            self.text_comparacao.config(state=tk.NORMAL)
            self.text_comparacao.delete("1.0", tk.END)
            self.text_comparacao.insert(tk.END, texto)
            self.text_comparacao.config(state=tk.DISABLED)
        
        except ValueError:
            messagebox.showerror("❌ Erro", "Valores inválidos!")
    
    def _calcular_multiplos(self):
        """Calcula múltiplos trajetos."""
        try:
            dados_json = self.text_multiplos_entrada.get("1.0", tk.END).strip()
            trajetos = json.loads(dados_json)
            
            resultado = self.calc.calcular_multiplos_trajetos(trajetos)
            
            texto = f"""
╔════════════════════════════════════════╗
║      MÚLTIPLOS TRAJETOS - TOTAL        ║
╠════════════════════════════════════════╣
║ Total de trajetos: {len(trajetos):>24}
║ Total de litros: {resultado['total_litros']:>24.2f} L
║ Custo total: R$ {resultado['total_custo']:>26.2f}
╚════════════════════════════════════════╝
            """
            
            self.text_multiplos_resultado.config(state=tk.NORMAL)
            self.text_multiplos_resultado.delete("1.0", tk.END)
            self.text_multiplos_resultado.insert(tk.END, texto)
            self.text_multiplos_resultado.config(state=tk.DISABLED)
        
        except json.JSONDecodeError:
            messagebox.showerror("❌ Erro", "JSON inválido!")
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro: {str(e)}")
    
    def _atualizar_historico(self):
        """Atualiza listagem do histórico."""
        historico = self.calc.listar_historico(limite=20)
        
        texto = "╔════════════════════════════════════════╗\n"
        texto += "║    ÚLTIMOS CÁLCULOS (últimos 20)       ║\n"
        texto += "╠════════════════════════════════════════╣\n"
        
        if historico:
            for i, calc_data in enumerate(historico[::-1], 1):
                timestamp = calc_data.get('timestamp', 'N/A')[:19]
                custo = calc_data.get('custo_total', 0)
                litros = calc_data.get('litros', 0)
                texto += f"║ {i:>2}. {timestamp} - R$ {custo:>6.2f} ({litros:>5.2f}L) ║\n"
        else:
            texto += "║ Histórico vazio                        ║\n"
        
        texto += "╚════════════════════════════════════════╝\n"
        
        self.text_historico.config(state=tk.NORMAL)
        self.text_historico.delete("1.0", tk.END)
        self.text_historico.insert(tk.END, texto)
        self.text_historico.config(state=tk.DISABLED)
    
    def _limpar_historico(self):
        """Limpa histórico com confirmação."""
        if messagebox.askyesno("⚠️ Confirmação", "Tem certeza que deseja limpar todo o histórico?"):
            self.calc.limpar_historico()
            self._atualizar_historico()
            messagebox.showinfo("✅ Sucesso", "Histórico limpo!")


def main():
    """Função principal."""
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
