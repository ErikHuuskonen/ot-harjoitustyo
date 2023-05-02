# Käyttöohje

Lataa projektin viimeisimmän releasen

## Ohjelman käynnistäminen

1. Lataa repositorio /tmp hakemistoon:

```bash
cd /tmp
mkdir tietotila
cd tietotila
git clone https://github.com/ErikHuuskonen/ot-harjoitustyo.git
```
2. Asenna riippuvuudet komennolla: 

```bash
poetry install
```

3. Sovelluksen käynnistäminen komennolla:

```bash
poetry run invoke start
```
## Uuden käyttäjän luominen

Käyttäjän valinta ja luomis näkymässä käyttäjä näkee yhden napin josta painamalla hän voi luoda käyttäjän valitsemallaan nimellä

Jos käyttäjän luominen onnistuu, siirrytään siirrytään käyttäjän omiin tiedostoihin

## Tiedostojen luominen

Käyttäjä voi luoda tiedostoja samalla tavalla kuin käyttäjiä, painamalla ainoasta napista joka on näkymässä painettavissa.
Kun käyttäjä valitsee luodun tiedoston hiirellään hän pääsee miellekartta näkymään

## Miellekartan käyttö

Käyttäjä voi luoda, siirtää, zoomata ja yhdistää miellekartan solmuja seuraavasti: 

luominen = klikkaa kahdesta tyhjää kanvasta

zoomaa = hiiren roll toiminnolla

kahden solmun yhdistäminen = valitse solmu jonka haluat liittää toiseen painamalla solmua kerran hiirelläsi, vedä viiva solmuun jonka halua yhdistää. 

korttien luominen = valitse jokin solmu ja paina sitä kahdesti hiirelläsi

kortteja voi luoda avautuneessa näkymässä painamalla lisää nappia vasemmassa yläkulmassa

kun painat takaisin näät kortin etupuolen "pakka" näkymässä, jos painat näytä vastaus niin kortin takapuoli paljastuu. 
Tämän jälkeet voit siirtyä seuraavaan korttiin painamalla jotain ilmeistyneistä napeista. 


