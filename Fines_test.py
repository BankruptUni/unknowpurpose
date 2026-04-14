import unittest
from ApiController import HonestidadeEmpresarial as hon

class TestResourceUtils(unittest.TestCase):    
    def testeExemplo(self):        
        testado = hon.GetAllFineCompany("03.362.908/0001-33")
        self.assertEqual(testado, "251.293,61", "É exatamente o mesmo parametro usado para teste, deveria ter encontrado")
    

