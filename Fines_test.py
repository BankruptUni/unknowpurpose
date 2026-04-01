import unittest
from ApiController import HonestidadeEmpresarial as hon

class TestResourceUtils(unittest.TestCase):    
    def testeValorValido(self, valor: str = "") -> None:
        assert valor and valor.strip(), "Valor Nulo ou vazio inválido para o método"
    def testeExemplo(self):        
        testado = hon.GetAllFineCompany("03.362.908/0001-33")
        self.assertEqual(testado, "251.293,61", "É exatamente o mesmo parametro usado para teste, deveria ter encontrado")
    

