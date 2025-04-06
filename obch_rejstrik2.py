# Zadání
# Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.


# Část 2
# Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat. Následně vypiš všechny nalezené subjekty, které ti API vrátí.

import json
import requests
import os

print("OBCHODNÍ REJSTŘÍK - podle názvu")
print("Aplikace pro vyhledávání v obchodním rejstříku")
nazev = input("Zadejte název nebo část názvu subjektu, který chcete vyhledat: ")
print(f"Vyhledávám {nazev}...")

# V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat. Request typu POST pošleme tak, že namísto funkce requests.get() použijeme funkci requests.post(). K requestu musíme přidat hlavičku (parametr headers), který určí formát výstupních dat. Použij slovník níže.

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
payload = {"obchodniJmeno": f"{nazev}"}

response = requests.post(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=payload)

data = response.json()
print(data)

# Tentokrát API vrátí počet nalezených subjektů (pocetCelkem) a seznam nalezených subjektů ekonomickeSubjekty. Tvůj program by měl vypsat obchodní jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou. 

print("")
print("Výsledek vyhledávání:")

pocet = data.get("pocetCelkem", 0)

if pocet == 0:
  print("Nebyl nalezen žádný subjekt.")
else:
  print(f"Nalezeno subjektů: {pocet}")


subjekty = data.get("ekonomickeSubjekty", [])

vystup = [f"{subjekt['obchodniJmeno']} ({subjekt['ico']})" for subjekt in subjekty]


vypis = ", ".join(vystup)

print(f"Subjekty obsahující  {nazev} : " + vypis)


