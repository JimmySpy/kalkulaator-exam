class Kalkulaator:
    def __init__(self, a, b):
        """
        Mis leiab kaks arvu.
        """
        self.a = a
        self.b = b

    def liitmine(self):
        """
        Liidab kaks arvu ning tagastab tulemuse.
        """
        return self.a + self.b

    def lahutamine(self):
        """
        Lahutab teise arvu esimesest, ning tagastab tulemuse.
        """
        return self.a - self.b

    def korrutamine(self):
        """
        Korrutab kaks arvu ja tagastab tulemuse.
        """
        return self.a * self.b

    def jagamine(self):
        """
        Jagab esimese arvu teisega, tagastab tulemuse.
        Kui jagamine ei ole võimalik NT:(jagamine nulliga), tagastatakse veateade.
        """
        if self.b == 0:
            return "Viga: jagamine nulliga pole võimalik!"
        return self.a / self.b

    def jääk(self):
        """
        Tagastab jäägi, kui esimene arv jagatakse teisega.
        """
        return self.a % self.b

    def ruutjuur(self):
        """
        Arvutab ja tagastab esimese arvu ruutjuure.
        """
        if self.a < 0:
            return "Viga: negatiivsel arvul pole reaalarvulist ruutjuurt!"
        return self.a ** 0.5

    def astendamine(self):
        """
        Arvutab esimese arvu astendamise teise arvuga ja tagastab tulemuse.
        """
        return self.a ** self.b

    def nurgafunktsioon(self):
        """
        Lisafunktsioon, mis arvutab nurgafunktsiooni, nt sinus.
        """
        import math
        return math.sin(self.a)

def menu():
    """
    Kuvab kasutajale valikute menüü.
    """
    print("Vali üks järgmistest toimingutest:")
    print("1. Liitmine")
    print("2. Lahutamine")
    print("3. Korrutamine")
    print("4. Jagamine")
    print("5. Jäägi leidmine")
    print("6. Ruutjuure leidmine")
    print("7. Astendamine")
    print("8. Nurgafunktsioon (sinus)")
    print("0. Välju")

def kasutaja_valik():
    """
    Küsimine ja töötlemine, milline tehe teha.
    """
    valik = int(input("Sisesta valik: "))
    return valik

def main():
    """
    Põhifunktsioon, kus toimub kogu kalkulaatori töötlus.
    """
    try:
        a = float(input("Sisesta esimene number: "))
        b = float(input("Sisesta teine number: "))
    except ValueError:
        print("Palun sisestage kehtivad arvud!")
        return

    kalk = Kalkulaator(a, b)

    while True:
        menu()
        valik = kasutaja_valik()

        if valik == 1:
            print(f"Vastus: {kalk.liitmine()}")
        elif valik == 2:
            print(f"Vastus: {kalk.lahutamine()}")
        elif valik == 3:
            print(f"Vastus: {kalk.korrutamine()}")
        elif valik == 4:
            print(f"Vastus: {kalk.jagamine()}")
        elif valik == 5:
            print(f"Vastus: {kalk.jaak()}")
        elif valik == 6:
            print(f"Vastus: {kalk.ruutjuur()}")
        elif valik == 7:
            print(f"Vastus: {kalk.astendamine()}")
        elif valik == 8:
            print(f"Vastus: {kalk.nurgafunktsioon()}")
        elif valik == 0:
            print("Väljumine kalkulaatorist.")
            break
        else:
            print("Vale valik, proovige uuesti.")

if __name__ == "__main__":
    main()
