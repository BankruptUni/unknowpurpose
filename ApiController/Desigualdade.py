
from pathlib import Path
import traceback
import csv
class DesigualdadeBusiness:
    def __init__(self, diretorio:str = Path(__file__).resolve().parents[1]):
        self._diretorio = diretorio

    def GetDesigualdadeCountry(self, ano: int = 2020) -> list[tuple]:
        """     //  Captação da desigualdade de cada país //    """
        desigualdadePaises:list[tuple] = []
        dictPaises = {}
        try:
            
            with open(f"{self._diretorio}/PercentilDesigualdade.csv", "r", encoding = "utf-8") as percentis:
                next(percentis)
                reader = csv.DictReader(percentis, delimiter = ";")
                paises = {pais.strip().split('\n')[-1].strip(): pais for pais in reader.fieldnames if pais not in ["Percentile ", "Year "]}
                #next(percentis)                    
                for registro in reader:            
                    if int(registro["Year "]) == ano:
                        percentil = registro["Percentile "]
                        for pais, nomeComplexo in paises.items():
                            valor = float(registro[nomeComplexo]) if registro[nomeComplexo].strip() else 0.0
                            dictPaises.setdefault(pais, {})[percentil] = valor
                for nomePais, valores in dictPaises.items():        
                    tupla = (nomePais, valores['p0p50'], valores['p90p100'])
                    desigualdadePaises.append(tupla)            
                percentis.seek(0)

                return sorted(desigualdadePaises, key = lambda pais: pais[0])
        except Exception: traceback.print_exc()
