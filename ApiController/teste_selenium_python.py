from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import traceback
import re
acronyns = ["BR","DK"];
score = [];
try:
    #instanciando uma captura no Edge
    driver = webdriver.Edge();
    driver.get("https://transparenciainternacional.org.br/ipc");
    for acronym in acronyns:
        divElementoPai = driver.find_element(By.ID, f"mapsvg-directory-item-{acronym}");
        text: str = re.sub("\D",divElementoPai.find_element(By.CLASS_NAME, "cpi-score").text);
        score.append((acronym, text));

    print("—".join([f"{sigla} | {resultado}" for sigla, resultado in zip(*score)]));
except Exception as e: 
    print(f"{e}\n{traceback.print_exc()}")
    
