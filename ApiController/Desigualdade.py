import traceback
from Repository.DesigualdadeRepository import DesigualdadeRepository
class DesigualdadeBusiness:
    def __init__(self, repository:DesigualdadeRepository):
        self.__repository = repository                
    def GetDesigualdadeCountry(self, ano: int = 2020) -> list[tuple]:
        """     //  Captação da desigualdade de cada país //    """
        try:
            return self.__repository.GetDesigualdade(ano)
        except Exception: traceback.print_exc()
