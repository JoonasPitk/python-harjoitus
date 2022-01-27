# Harjoitus, jossa tehdään luokkia ja olioita.

# MODULIEN JA KIRJASTOJEN LATAUKSET

# LUOKKIEN MÄÄRITTELY

# Määritellään Lainaaja-luokka, joka ei peri mitään.
class Lainaaja:
    # Uuden olion luonti (constructor). Olion luontimetodi.
    def __init__(self, opiskelijanumero, etunimi, sukunimi):
        # Ominaisuudet: self viittaa tulevaan olioon, jonka nimi ei vielä ole tiedossa.
        self.opiskelijanumero = opiskelijanumero
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    # Olion metodi: mitä olio osaa tehdä.
    def tulosta_opiskelijanumero(self):
        print('Opiskelijanumero on', self.opiskelijanumero)

    def tulosta_kaikki_tiedot(self):
        print(
            'Opiskelijanumero:', self.opiskelijanumero, '\n'
            'Etunimi:', self.etunimi, '\n'
            'Sukunimi:', self.sukunimi
        )

# VARSINAINEN OHJELMA

# Luodaan lainaaja-olio Lainaaja-luokasta.
lainaaja1 = Lainaaja(
    123456,
    'Matti',
    'Meikäläinen'
)

# Testataan lainaaja1-oliota.
print('Lainaaja1 on', lainaaja1.etunimi, lainaaja1.sukunimi)

lainaaja1.tulosta_opiskelijanumero()
lainaaja1.tulosta_kaikki_tiedot()
