"""Certo, fundar um sistema de honestidade empresarial nacional parece um bom plano, mas preciso de mais dados.
    CNEP / CEIS
"""
from pathlib import Path
import csv
import os
import traceback
companies = [];

class Company:
    @property 
    def Name(self):
        return self.name

    def __init__():
        pass

def GetAllFineCompany(cnpj: str = "") -> None:
    """Formulando um método de captação de multas de uma empresa específica caso ela esteja no arquivo da """
    try:
        
        formattedDoc = cnpj if any(formatacao in cnpj for formatacao in [".", "/", "-"]) else f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}";
        if len(cnpj) == 0: 
            raise ValueError("Cnpj precisa ter um valor válido.");
        directory = Path(__file__).parent;        
        with open(f"{directory}/sancoes.csv", "r", encoding = "utf-8-sig") as sancoes:
            reader = csv.DictReader(sancoes, delimiter = ";",skipinitialspace=True);
            documento = reader.fieldnames;
            
            sancoes.seek(0)
            next(sancoes)

            valores = [
                valor["Valor multa"] 
                for valor in reader  
                if valor.get("CNPJ/CPF da Pessoa ou Empresa Sancionada", "").strip() == formattedDoc];
            print(documento)
            
            print(valores)
    except Exception as ex:
        traceback.print_exc()
    return None;
#Testes
GetAllFineCompany("03.362.908/0001-33")