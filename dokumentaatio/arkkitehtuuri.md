# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on seuraava: 

```mermaid
graph LR
A[tietotila]
B[history]
C[tests]

A -->|sisältää| A1[__init__.py]
A -->|sisältää| A2[__pycache__]
A -->|sisältää| A3[foldermanagement.py]
A -->|sisältää| A4[main.py]
A -->|sisältää| A5[mindmapscreen.py]
A -->|sisältää| A6[usermanagement.py]
A -->|sisältää| A7[folderselectionscreen.py]
A -->|sisältää| A8[loadingscreen.py]
A -->|sisältää| A9[mindmapmanagement.py]
A -->|sisältää| A10[testi.py]
A -->|sisältää| A11[mindmapapp.py]
A -->|sisältää| A12[resized_image.jpg]
A -->|sisältää| A13[userselectionscreen.py]

```
## Käyttöliittymä

Käyttöliittymä sisältää kuusi erillistä näkymää:

-latausnäyttö

-käyttäjän valinta ja luominen

-kansion valinta ja luominen

-miellekartta näkymä

-muistikorttien luomiseen tarkoitettu näkymä

-muistikorttien harjoitteluun tarkoitettu näkymä

Jokainen näkymä käyttöliittymässä on toteutettu omana luokkanaan ja useat niistä sijaitsevat eri moduuleissa. 

## Sovelluslogiikka

Ohjelman osat jotka eivät käytä tkinter kirjastoa ovat eritelty loppupäätteellä ...management. 
Nämä moduulit vastaavat ohjelman logiikasta. 

Puolestaan screen päätteiset moduulit vastaavat ui puolesta. 

[sekvenssikaavio](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/sekvenssikaavio.md)


## Tietojen pysyväistallennus

Ohjelman juuressa oleva kansio src sisältää erillisen kansion nimeltä history jonka tarkoituksena on säilyttää .pickle tiedostoja. 

Näihin tiedostoihin kirjoitetaan miellekarttojen sisältö, käyttäjät sekä tiedosojen nimet. 

```mermaid
graph LR
A[src]
A1[history]
A2[tests]
A3[tietotila]
A -->|sisältää| A1
A -->|sisältää| A2
A -->|sisältää| A3

B[new_user_folder]
C[pickle_file]
A1 -->|luodaan uusi kansio| B
B -->|luodaan .pickle tiedosto| C

```

## Päätoiminnallisuudet

Ohjelman päätoiminnallisuudet ovat seuraavat: 

-Käyttäjien luominen ja valinta
-Uusien miellekartta tiedostojen luominen ja vanhojen valinta
-Miellekarttanäkymässä miellekarttojen muodostaminen
-Miellekartan avulla quizlet ja anki tyylisten muistikortti kokonaisuuksien luominen ja hallinta

## Ohjelman rakenteeseen jääneet heikkoudet

Ohjelmani rakenteeseen on jääynyt ainakin seuraavat heikkoudet:

- Ohjelman ui ja logic eivät ole tarpeeksi hyvin eritelty

-Ohjelmani kansiorakenne ja moduulien nimeäminen on sekavaa

