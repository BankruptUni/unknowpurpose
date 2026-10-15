import pandas as skadush
class ODSRepository :
    def __init__(self):
        pass
    def GetRankingPaises(nomeArquivo : str, abaPlanilha : str ) -> skadush.DataFrame:
        planilha = skadush.read_excel(nomeArquivo, sheet_name = abaPlanilha)
        return planilha