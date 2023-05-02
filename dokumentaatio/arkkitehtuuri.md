# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on seuraava: 

```mermaid
graph LR
A[history]
B[tests]
C[tietotila]
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

C --> A
B --> A
```
## Käyttöliittymä

Käyttöliittymä sisältää x näkymää:


## Sovelluslogiikka


## Tietojen pysyväistallennus


### Tiedostot

## Päätoiminnallisuudet

### Käyttäjän kirjaantuminen

### Uuden käyttäjän luominen

### Tietotilan(mindmapin) luominen

### Muut toiminnallisuudet

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä
