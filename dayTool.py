#ferramenta de execução para tarefas diárias 
#inicia o navegador e abre as guias recém fechadas



import pyautogui
import time 


time.sleep(2)
pyautogui.press("browserhome")
pyautogui.hotkey("ctrl", "shift", "t")
time.sleep(2)
pyautogui.alert()



#transformar em executável após conclusão 
