import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    
    def test_rahamaara_ja_myytyjen_lounaiden_maara(self):
        Kassapaate.__init__(self)
        self.assertEqual(self.kassassa_rahaa, 100000)
        self.assertEqual(self.edulliset, 0)
        self.assertEqual(self.maukkaat, 0)
    
    def test_kateisosto_edullinen_true(self):
        Kassapaate.__init__(self)
        vaihtoraha = Kassapaate.syo_edullisesti_kateisella(self, 500)
        self.assertEqual(vaihtoraha, 500-240)
        self.assertEqual(self.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.edulliset, 1)

    def test_kateisosto_maukas_true(self):
        Kassapaate.__init__(self)
        vaihtoraha = Kassapaate.syo_maukkaasti_kateisella(self, 1000)
        self.assertEqual(vaihtoraha, 1000-400)
        self.assertEqual(self.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.maukkaat, 1)


    def test_kateisosto_edullinen_false(self):
        Kassapaate.__init__(self)
        vaihtoraha = Kassapaate.syo_edullisesti_kateisella(self, 200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassassa_rahaa, 100000)
        self.assertEqual(self.edulliset, 0)

    def test_kateisosto_maukas_false(self):
        Kassapaate.__init__(self)
        vaihtoraha = Kassapaate.syo_maukkaasti_kateisella(self, 50)
        self.assertEqual(vaihtoraha, 50)
        self.assertEqual(self.kassassa_rahaa, 100000 )
        self.assertEqual(self.maukkaat, 0)
    
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_korttiosto_toimii_edullinen(self):
        Kassapaate.__init__(self)
        vahennetaan_kortilta = Kassapaate.syo_edullisesti_kortilla(self, self.maksukortti)
        self.assertEqual(vahennetaan_kortilta, True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.edulliset, 1)
        self.assertEqual(self.kassassa_rahaa, 100000)
    
    def test_korttiosto_edullinen_false(self):
        Kassapaate.__init__(self)
        self.maksukortti = Maksukortti(100)
        vahennetaan_kortilta = Kassapaate.syo_edullisesti_kortilla(self, self.maksukortti)
        self.assertEqual(vahennetaan_kortilta, False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.edulliset, 0)
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukas(self):
        Kassapaate.__init__(self)
        vahennetaan_kortilta = Kassapaate.syo_maukkaasti_kortilla(self, self.maksukortti)
        self.assertEqual(vahennetaan_kortilta, True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.maukkaat, 1)
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_false(self):
        Kassapaate.__init__(self)
        self.maksukortti = Maksukortti(100)
        vahennetaan_kortilta = Kassapaate.syo_maukkaasti_kortilla(self, self.maksukortti)
        self.assertEqual(vahennetaan_kortilta, False)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.maukkaat, 0)
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_kortille_saldoa(self):
        Kassapaate.__init__(self)
        self.kortti = Maksukortti(500)
        Kassapaate.lataa_rahaa_kortille(self, self.kortti, 1000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 15.00 euroa")
        
        self.assertEqual(self.kassassa_rahaa, 100000 + 1000)
    
    def test_kortille_saldoa_nolla(self):
        Kassapaate.__init__(self)
        self.kortti = Maksukortti(0)
        Kassapaate.lataa_rahaa_kortille(self, self.kortti, -1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassassa_rahaa, 100000 )