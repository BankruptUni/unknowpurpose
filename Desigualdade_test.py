import unittest
from ApiController.Desigualdade import DesigualdadeBusiness as ineq
from Repository.DesigualdadeRepository import DesigualdadeRepository as repository

class TestInequalityUtils(unittest.TestCase):    
    def testeSamplePaises(self, valor: str = "") -> None:
        business = ineq(repository())
        retorno_metodo_principal = business.GetDesigualdadeCountry(2024)
        paises = []
        paises.extend([
    ("Switzerland", 0.0372, 0.6279),
    ("Brazil", 0.0203, 0.7190000000000001), # O "vilão" da estabilidade
    ("Slovakia", 0.0744, 0.4940000000000001)
])
        for pais in paises:
            self.assertIn(pais, retorno_metodo_principal, "Não capturou esses países no mesmo período que tirei de amostra")
    

