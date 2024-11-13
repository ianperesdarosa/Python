import pandas as pd # type: ignore
import yfinance as yf # type: ignore
import matplotlib.pyplot as plt # type: ignore
from powerbi import PowerBI # type: ignore

class StatusInvestImporter:
    def __init__(self, link):
        self.link = link
        self.dados = None

    def importar_dados(self):
        # Importar dados do Status Invest
        self.dados = pd.read_csv(self.link)

    def gerar_graficos(self):
        # Gerar gráficos das ações
        for acao in self.dados['Ação'].unique():
            dados_acao = self.dados[self.dados['Ação'] == acao]
            plt.figure(figsize=(10, 6))
            plt.plot(dados_acao['Data'], dados_acao['Preço'])
            plt.title(f'Gráfico de {acao}')
            plt.xlabel('Data')
            plt.ylabel('Preço')
            plt.savefig(f'{acao}.png')

    def exportar_para_power_bi(self):
        # Exportar gráficos para o Power BI
        power_bi = PowerBI()
        for acao in self.dados['Ação'].unique():
            power_bi.import_image(f'{acao}.png', f'Gráfico de {acao}')

# Exemplo de uso:
link = 'https://statusinvest.com.br/acoes/acoes.csv'
importer = StatusInvestImporter(link)
importer.importar_dados()
importer.gerar_graficos()
importer.exportar_para_power_bi()