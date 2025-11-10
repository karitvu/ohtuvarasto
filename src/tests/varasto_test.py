import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tehdaan_virheellisen_kokoinen(self):
        self.varasto = Varasto(-1)
        # varaston tilavuuden pitäisi olla 0
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_alkusaldo(self):
        self.varasto = Varasto(10, -1)
        # varastossa pitäisi olla tilaa 10
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_negatiivista(self):
        self.varasto.lisaa_varastoon(-1)
        # varastossa pitäisi olla tilaa 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisataan_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(11)
        # varaston pitäisi olla täynnä
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otetaan_negatiivista(self):
        # palauttaa 0
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(8)
        # palauttaa kaiken mitä on, eli 8
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)

    def test_teksti(self):
        testi = Varasto(10, 2)
        # palauttaa tekstimuotoisen informaation
        self.assertEqual(str(testi), "saldo = 2, vielä tilaa 8")

    # uusi muutos
