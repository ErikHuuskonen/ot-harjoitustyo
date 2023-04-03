
# Ohjelmistotekniikka, harjoitustyö Tietotila 

Tietotila on säännölliseen tiedon omaksumiseen tarkoitettu mindmapien ja muistikorttien hyvät puolet kokoava apuohjelma. Ohjelma vaattii python 3.8 (tai uudemman) 

## Dokumentaatio 

- [työaikakirjanpito](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [vaatimusmäärittely](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [chanelog](https://github.com/ErikHuuskonen/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Asennus 

1. Asenna riippuvuudet komennolla: 

'''bash
poetry install
'''

2. Sovelluksen käynnistäminen komennolla:

'''bash
poetry run invoke start
'''

## Testit

Voit testa ohjelman komennolla: 

'''bash
poetry run invoke test
'''

Testikattavuusraportti komennolla: 

'''bash
poetry run invoke coverage-report
'''



