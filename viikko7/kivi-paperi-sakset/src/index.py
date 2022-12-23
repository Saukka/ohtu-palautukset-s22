from kivi_paperi_sakset import KiviPaperiSakset

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus == 'a' or vastaus == 'b' or vastaus == 'c':
            peli = KiviPaperiSakset(vastaus)
            peli.pelaa()
        break

if __name__ == "__main__":
    main()
