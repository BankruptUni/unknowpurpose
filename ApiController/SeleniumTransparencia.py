from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import re
acronyns: list[str] = ["BR","DK"];

def GetPaisesSelecionados (acronyns: list[str]) -> list[tuple[str,str]]:
    """Função que captura a posição dos países mencionados nas siglas dentro do portal da 
   Transparência Internacional para verificar seu índice de corrupção"""
    score:list[tuple[str, str]] = [];
    try:
        #instanciando uma captura no Edge
        driver = webdriver.Edge();
        driver.get("https://transparenciainternacional.org.br/ipc");
        #nuisance
        advertising = WebDriverWait(driver, 40).until( EC.element_to_be_clickable((By.ID, "adopt-reject-all-button")))
        advertising.click()
        try:
            joinUs = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@style, 'z-index:2')]//button")))
            joinUs.click()
        except:
            print("É uma porcaria achar isso viu?")

        for acronym in acronyns:
            divElementoPai = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, f"mapsvg-directory-item-{acronym}")));
            text: str = re.sub("\D",divElementoPai.find_element(By.CLASS_NAME, "cpi-score").text);
            score.append((acronym, text));

        print("—".join([f"{sigla} | {resultado}" for sigla, resultado in zip(*score)]));
    except Exception as e: 
        print(f"{e}\n{traceback.print_exc()}")
    return score
    
