# Harjoitus, jossa tehdään luokkia ja olioita.

# MODULIEN JA KIRJASTOJEN LATAUKSET

# LUOKKIEN MÄÄRITTELY

# Määritellään Henkilö-luokka (yliluokka, superclass tai parent class), joka määrittelee yleiset ominaisuudet.
class Henkilo:
    def __init__(self, etunimi, sukunimi, osasto):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.osasto = osasto

# Opiskelija-luokka (aliluokka, subclass tai child), perii Henkilö-luokan ominaisuudet.
class Opiskelija(Henkilo):
    def __init__(self, etunimi, sukunimi, osasto, opiskelijanumero):
        super().__init__(etunimi, sukunimi, osasto)
        self.opiskelijanumero = opiskelijanumero

# Opettaja-luokka, perii Henkilo-luokan ominaisuudet.
class Opettaja(Henkilo):
    def __init__(self, etunimi, sukunimi, osasto, tyohuone):
        super().__init__(etunimi, sukunimi, osasto)
        self.tyohuone = tyohuone

# VARSINAINEN OHJELMA

# Luodaan Opiskelija-olio.
opiskelija1 = Opiskelija(
    'Jakke',
    'Jäynä',
    'ICT',
    123456
)

# Luodaa Opettaja-olio.
opettaja1 = Opettaja(
    'Mari',
    'Lounavaara',
    'ICT',
    'A228'
)

# Testataan olioita.
print('Opiskelija', opiskelija1.etunimi, opiskelija1.sukunimi, 'opiskelee', opiskelija1.osasto, '-osastolla')
print(opettaja1.etunimi, opettaja1.sukunimi, 'työskentelee huoneessa', opettaja1.tyohuone)
