## viikko3
-poetry install wheel ongelma aiheutti GUI vaihdoiksen
-Alkuperäinen pyqt5 ohjelma jouduttiin hyllyttämään

-uusi ohjelma on aloitoittu
-Ohjelma käyttää Chat-GPT-4:n luomaa luokka-arkkitehtuuri ehdotusta.
-Ohjelmassa on graafinen käyttöliittymä, joka on toteutettu käyttämällä tkinter-kirjastoa
-Ohjelmassa on luokka MindmapApp, joka hallinnoi ohjelman komponentteja ja niiden näyttämistä
-MindmapApp sisältää eri komponentit, kuten LoadingScreen ja UserSelectionScreen
-MindmapApp:ssa on funktiot näytettävien komponenttien vaihtamiseksi
-UserSelectionScreen-luokka esittää käyttäjille valintanäkymän
-Käyttäjät voivat valita olemassa olevan käyttäjän tai luoda uuden käyttäjän
-UserSelectionScreen käyttää UserManagement-luokkaa käyttäjien hallintaan
-MindmapApp-luokan instanssi luodaan ja suoritetaan ohjelman lopussa
-Koodissa on kommentoitu pois muita komponentteja ja toiminnallisuuksia, kuten FolderSelectionScreen ja MindmapScreen, mutta ne eivät ole käytössä nykyisessä versiossa.
## viikko4
-nyt poetry run invoke start komennolla käyttäjälle avautuu aloitus näkymä (ei skaalaudu oikein linuxilla), tämä kestää viisi sekuntia jonka jälkeen käyttäjä valitsee käyttäjän.
-Käyttäjän valinnasta avautuu käyttäjän oma kansio valinta jossa ei ole kansioita. Käyttäjä voi luoda sellaisen (ei tallennu vielä ) 
-Tämän jälkeen käyttäjä voi siirtyä kansioonsa, jossa hänelle aukea mindmap pohja jossa on yksi masternode. 
-Käyttäjä voi luoda uuden noden tupla-klikkaamalla tyhjää aluetta ja syöttämällä noden nimen.
-Käyttäjä voi siirtää noden paikkaa painamalla shift pohjaan ja raahaamalla nodea.
-Käyttäjä voi piirtää viivoja yhdistämään kaksi nodea klikkaamalla kahta erillistä nodea.
-Käyttäjä voi liikkua näkymässä raahaamalla tyhjää aluetta hiirellään.
-Käyttäjä voi zoomata (+-) midmappia. 

-ohjelmalle on luotu 15kpl testejä
-pylint on otettu käyttöön ja ja olen siivonnut ohjeiden mukaan tiedostoja
