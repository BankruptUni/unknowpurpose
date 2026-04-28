"""Certo, fundar um sistema de honestidade empresarial nacional parece um bom plano, mas preciso de mais dados.
    CNEP / CEIS
"""
import traceback
from Repository.HonestidadeEmpresarialRepository import HonestidadeEmpresarialRepository as repository
class HonestidadeEmpresarialBusiness:
    def __init__(self, repository:repository):
        self.__repository = repository        
    def GetAllFineCompany(self) -> str:
        """Formulando um método de captação de multas de uma empresa específica caso ela esteja no arquivo da CNEP CEIS """
        try:        
           return self.__repository.GetAllFineCompany()
        except Exception:
            traceback.print_exc()
               