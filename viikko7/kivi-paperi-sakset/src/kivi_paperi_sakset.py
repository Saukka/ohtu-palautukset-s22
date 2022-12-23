from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly
 
class KiviPaperiSakset:
    def __init__(self, toinen_pelaaja):
        self.toinen_pelaaja = toinen_pelaaja
        if toinen_pelaaja == 'b':
            self.tekoaly = Tekoaly()
        if toinen_pelaaja == 'c':
            self.tekoaly = TekoalyParannettu(10)


    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        self._tietokoneen_valinta(tokan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            self._tietokoneen_valinta(tokan_siirto)

        print("Kiitos!")
        print(tuomari)



    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tietokoneen_valinta(self, siirto):
        if self.toinen_pelaaja != 'a':
            print(f"Tietokone valitsi: {siirto}")

    def _toisen_siirto(self, ensimmaisen_siirto):

        if self.toinen_pelaaja == 'a':
            tokan_siirto = input("Toisen pelaajan siirto: ")
            return tokan_siirto
        
        tokan_siirto = self.tekoaly.anna_siirto()
        if self.toinen_pelaaja == 'c':
            self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        
        return tokan_siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
