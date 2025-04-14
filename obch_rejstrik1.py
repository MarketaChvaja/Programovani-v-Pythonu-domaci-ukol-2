# Zadání
# Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.


# Část 1
# V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektu. Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace. 

import json
import requests
import os 

print("OBCHODNÍ REJSTŘÍK - podle IČO")
print("Aplikace pro vyhledávání v obchodním rejstříku")
ico = input("Zadejte IČO subjektu, který chcete vyhledat: ")
print(f"Vyhledávám {ico}...")

# S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, kde ICO nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). 

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = response.json()
print(data)

json_text = json.dumps(data, indent=2, ensure_ascii=False)


# stažená data uloží do souboru a do složky, soubor pojmenuje podle vyhledaneho ICO, pokud uz stejny soubor existuje, prida k nazvu souboru cislo
# S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd. Text, který API vrátí, převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). Získané informace vypiš na obrazovku.

# verze 1 - puvodni
# nazev = data["obchodniJmeno"]
# adresa = data["sidlo"]["textovaAdresa"]

# verze 2 - podle AI
# nazev = data.get("obchodniJmeno", "Neznámý název")
# adresa = data.get("sidlo", {}).get("textovaAdresa", "Adresa není k dispozici")

# verze 3 - pomoci vyjimek
try:
  nazev = data["obchodniJmeno"]
except KeyError:
  nazev = "Název nenalazen"
  print("API nevrací název.")

try:
  adresa = data["sidlo"]["textovaAdresa"]
except KeyError:
  adresa = "Adresa nenalezena"
  print("API nevrací adresu.")




folder = "vystupy"
if not os.path.exists(folder):   #pridano, kdyby nekdo napr omylem smazal slozku
  os.makedirs(folder)            #pridano, kdyby nekdo napr omylem smazal slozku

filename = os.path.join(folder, f"{ico}-{nazev}.txt")   # nebo: filename =  f"vystupy\{ico}.txt"
counter = 1
while os.path.exists(filename):
  filename = os.path.join(folder, f"{ico}-{nazev}-{counter}.txt") # nebo: filename = f"vystupy\{ico}-{counter}.txt"
  counter += 1

with open(filename, "w", encoding="utf-8") as file:
  file.write(json_text)




print(" ")
print("Výsledek vyhledávání:")
print(f"Zadané IČO patří společnosti: {nazev} s adresou: {adresa}. Data byla uložena do souboru: {filename} ve složce: vystupy.")






