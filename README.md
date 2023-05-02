
# Ohjelmistotekniikka, harjoitustyö Tietotila 

Tietotila on säännölliseen tiedon omaksumiseen tarkoitettu mindmapien ja muistikorttien hyvät puolet kokoava apuohjelma. Ohjelma vaattii python 3.8 (tai uudemman) 

## Dokumentaatio 

- [työaikakirjanpito](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [vaatimusmäärittely](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [chanelog](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [alustava rakenne luokkakaaviona](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/alustava_luokkakaavio.md)
- [sekvenssikaavio](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/sekvenssikaavio.md)
- [arkkitehtuurikuvaus](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [käyttöohje](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)
## Asennus ja käyttö

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

## Testit

Voit testa ohjelman komennolla: 

```bash
poetry run invoke test
```

Testikattavuusraportti komennolla: 

```bash
poetry run invoke coverage-report
```

Pylint raportti komennolla: 

```bash
poetry run invoke pylint
```

