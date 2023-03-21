import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    #valmiiksi annetut testit
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")
    #tehtävän 3 testit
    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()
    
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_negatiivisen_summan_lataaminen(self):
        self.kortti.lataa_rahaa(-2500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")	
    
    def test_edullinen_kun_saldo_250snt(self):
        self.kortti = Maksukortti(250)
        self.kortti.syo_edullisesti()
    
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.00 euroa")

    def test_maukkaasti_kun_saldo_400snt(self):
        self.kortti = Maksukortti(400)
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.00 euroa")

    #tehtävä 6 testit 
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_oikein(self):
        self.kortti.lataa_rahaa(1000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 20.00 euroa")
    #rahan ottaminen toimii
    def test_rahan_ottaminen_rahaa_true(self):
        self.kortti = Maksukortti(250)
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.00 euroa")
    
    def test_rahan_ottaminen_rahaa_false(self):
        self.kortti = Maksukortti(250)
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.50 euroa")

    def true_jos_rahaa(self):
        assert self.kortti.syo_edullisesti() == True
    
    def false_jos_ei_rahaa(self):
        self.kortti = (100)
        assert self.kortti.syo_edullisesti() == False