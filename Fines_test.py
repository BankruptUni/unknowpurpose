import unittest
from ApiController.HonestidadeEmpresarial import HonestidadeEmpresarialBusiness as honestidade

class TestResourceUtils(unittest.TestCase):    
    def testeExemplo(self):        
        valorcapturado = honestidade("03.362.908/0001-33").GetAllFineCompany()           
        self.assertEqual(valorcapturado, "251.293,61", "É exatamente o mesmo parametro usado para teste, deveria ter encontrado")
    

