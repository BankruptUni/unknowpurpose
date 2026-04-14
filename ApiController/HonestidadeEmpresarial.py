"""Certo, fundar um sistema de honestidade empresarial nacional parece um bom plano, mas preciso de mais dados.
    CNEP / CEIS
"""
from pathlib import Path
import csv
import traceback
companies = []
def GetCurrency(valor:str)-> bool:    
    retorno = False
    teste = valor.replace(".","").replace(",",".")
    try:
        float(teste)
        retorno = True
    except ValueError:
        pass
    return retorno

def GetAllFineCompany(cnpj: str = "") -> str:
    """Formulando um método de captação de multas de uma empresa específica caso ela esteja no arquivo da CNEP CEIS """
    try:        
        if len(cnpj) == 0: 
            raise ValueError("Cnpj precisa ter um valor válido.");
        formattedDoc = cnpj if any(formatacao in cnpj for formatacao in [".", "/", "-"]) else f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
        directory = Path(__file__).resolve().parents[1]        
        with open(f"{directory}/sancoes.csv", "r", encoding = "utf-8-sig") as sancoes:
            reader = csv.DictReader(sancoes, delimiter = ";",skipinitialspace=True)
            documento = reader.fieldnames
            
            sancoes.seek(0)
            next(sancoes)

            valores = [
                (valor["Nome da Pessoa ou Empresa Sancionada"], valor["Valor multa"])
                for valor in reader  
                if valor.get("CNPJ/CPF da Pessoa ou Empresa Sancionada", "").strip() == formattedDoc]
            print(documento)
            
            print("\n".join([f"—{empresa} : R$ {valor}"if GetCurrency(valor) else f"—{empresa} : {valor}"  for empresa, valor in valores]))
    except Exception:
        traceback.print_exc()
    return valores[-1][1]