"""Moduuli Pylintille"""
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Varaston testaus"""
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testataan varaston luonti"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testataan varaston tilavuus"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testataan varastoon lisäys"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testataan pieneekö tila"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testataan ottamista"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testataan ottamisen vaikutusta"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tehdaan_virheellisen_kokoinen(self):
        """Testataan virheellisen kokoisen luontia"""
        self.varasto = Varasto(-1)
        # varaston tilavuuden pitäisi olla 0
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_alkusaldo(self):
        """Testataan virheellista alkusaldoa"""
        self.varasto = Varasto(10, -1)
        # varastossa pitäisi olla tilaa 10
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_negatiivista(self):
        """Testataan negatiivisen lisäystä"""
        self.varasto.lisaa_varastoon(-1)
        # varastossa pitäisi olla tilaa 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisataan_enemman_kuin_mahtuu(self):
        """Testataan ylimenevää lisäystä"""
        self.varasto.lisaa_varastoon(11)
        # varaston pitäisi olla täynnä
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otetaan_negatiivista(self):
        """Testataan negatiivisen ottamista"""
        # palauttaa 0
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_otetaan_liikaa(self):
        """Testataan liiallista ottamista"""
        self.varasto.lisaa_varastoon(8)
        # palauttaa kaiken mitä on, eli 8
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)

    def test_teksti(self):
        """Testataan teksti-ominaisuutta"""
        testi = Varasto(10, 2)
        # palauttaa tekstimuotoisen informaation
        self.assertEqual(str(testi), "saldo = 2, vielä tilaa 8")

    # uusi muutos
