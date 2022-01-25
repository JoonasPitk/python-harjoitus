# Luodaan lista viikonpäivistä.
viikonpaivat = [
    'maanantai',
    'tiistai',
    'keskiviikko',
    'torstai',
    'perjantai',
    'lauantai',
    'sunnuntai'
]

# Testataan tulostuskomennolla.
print('Viikon ensimmäinen päivä on', viikonpaivat[0])

# Sanakirja eli dict viikonpäivistä suomi-englanti.
day_names = {
    'maanantai':'Monday',
    'tiistai':'Tuesday',
    'keskiviikko':'Wednesday',
    'torstai':'Thursday',
    'perjantai':'Friday',
    'lauantai':'Saturday',
    'sunnuntai':'Sunday'
}

# Testataan tulostuskomennossa.
print('Tiistai on englanniksi', day_names['tiistai'])
