# MODULI MITTAUSSANOMIEN KÄSITTELYYN


# Sanoma koostuu alkumerkistä <, datasta, loppumerkistä > ja varmistussummasta
# Varmistussumma lasketaan siten, että kirjainten ascii koodit
# lasketaan yhteen ja summasta otetaan jakojäännös modulo 127
# Sanoman sisältö koostuu kentistä: sivuA, sivuB, ristimitta ja virhe
# Erottimena kenttien välillä on pystyviiva |
# Pohdittavaksi: varmistussumma ennen vai jälkeen loppumerkin

# <3000|4007|5080|74.4|103>

# Sanoman sisältämät tiedot tallennetaan avain-arvopareiksi
# Esim. {'seinä 1' : 2400, 'seinä 2' : 2500 ...}
# Tietojen oikeellisuus tarkistetaan laskemalla varmistussumma
# uudelleen ja vertaamalla sitä sanoman mukana tulleeseen

# Kirjastojen ja modulien lataukset

# Lasketaan merkkijonon ASCII-arvot yhteen
def summaa_merkit(merkkijono):
    """Laskee merkkijonon kirjainten ASCII-arvot yhteen

    Args:
        merkkijono (string): merkkijono, jonka kirjaimista summa lasketaan

    Returns:
        integer: kirjainten ASCII-koodien summa
    """
    summa = 0
    for kirjain in merkkijono:
        numeroarvo = ord(kirjain)
        summa = summa + numeroarvo
    return summa

# Muodostetaan merkeistä modulovarmiste valittua jakajaa käyttäen
def muodosta_varmiste(merkit, jakaja):
    return str(summaa_merkit(merkit) % jakaja)

#Yleispätevä funktio sanoman muodostamiseen 
def luo_sanoma(arvot, alkumerkki, loppumerkki, erotin, jakaja):
    """ Muodostaa sanoman, joka koostuu alkumerkistä, arvoista, varmistussummasta \n
    ja loppumerkistä. Arvojen välillä on haluttu erotinmerkki

    Args:
        arvot (list): sanomaan sisällöksi halutut arvot
        alkumerkki (string): merkki, jolla ilmaistaan sanoman alku
        loppumerkki (string): merkki, jolla ilmaistaan sanoman päättyminen
        erotin (string): arvojen välille tuleva välimerkki
        jakaja (int): jakojäännöksen laskennassa käytettävä jakaja

    Returns:
        string: Valmis sanoma 
    """
    sanoma = '' # Alustetaan sanoma tyhjäksi

    # Luetaan listan arvot ja muutetaan merkkijonoksi sekä lisätään erotinmerkki
    for arvo in arvot:
        sanoma = sanoma + str(arvo) + erotin

    # Lisätaan sanomaan alkumerkki, varmiste ja loppumerkki
    sanoma = alkumerkki + sanoma + muodosta_varmiste(sanoma, jakaja) + loppumerkki    
    return sanoma

 # Rakenna purkutestin perusteella funktio ja tee sille testi
def pura_sanoma(sanoma,alkumerkki,loppumerkki,erotin, jakaja):
    """Purkaa sanoman, kun sille kerrotaan muodostussäännöt

    Args:
        sanoma (string): Vastaanotettu sanoma
        alkumerkki (string): Sanoman aloittava erikoismerkki
        loppumerkki (string): Sanoman päättävä erikoismerkki
        erotin (string): kenttien välinen erotinmerkki
        jakaja (int): modulotarkistuksen jakaja

    Returns:
        list: lista arvoista (list string), virhekoodi (integer), virhesanoma (string)
    """
    arvot = [] # Alustetaan arvoksi tyhjä lista
    osat = [] # Alustetaan sanoman osat tyhjäksi listaksi
    virhekoodi = 0 # Normaalitilanteen virhekoodi
    virhesanoma = "Data OK" # Normaalitilanteen virhesanoma

    # Varmistetaan, että ensimmäinen merkki on alkumerkki
    if sanoma[0] == alkumerkki:

        # Varmistetaan, että viimeinen merkki on loppumerkki
        if sanoma[-1] == loppumerkki:
            sanoma = sanoma[1:-1] # Poistetaan alku- ja loppumerkit
            
            osat = sanoma.split(erotin) # Muodostetaan osat jakamalla sanoma erottimen kohdalta

            # Osia pitää ollä vähintää 2: arvo ja varmistussumma
            if len(osat) >= 2:
                alkuperainen_varmiste = int(osat[-1]) # Luetaan varmiste ja muutetaan se kokonaisluvuksi
                arvo_osat = f"{'|'.join(osat[0:-1])}|"
                # Muodostetaan arvoista ja erottimesta sanoman arvot sisältävä osa
                laskettu_varmiste = int(muodosta_varmiste(arvo_osat, jakaja)) # Lasketaan varmiste uudelleen
               
                # Varmistetaan, että alkuperäinen ja uudelleenlaskettu varmiste ovat samat
                if alkuperainen_varmiste == laskettu_varmiste:
                    arvot = (osat[0:-1]) # Muodostetaan arvoluettelo

                else:
                    virhekoodi = 4
                    virhesanoma = 'Sanoma vahingoittunut, varmistussumma ei täsmää'
            else:
                virhekoodi = 3
                virhesanoma = "Sanoma ei sisällä tarvittavaa dataa, viestissä ainoastaan varmiste"
                
            
            
            

        else:
            virhekoodi = 2
            virhesanoma = 'Sanoma vajaa, loppumerkki puuttuu'
    else:
        virhekoodi = 1
        virhesanoma = 'Sanoma vajaa, alkumerkki puuttuu'

    # Palautetaan arvot             
    return [arvot, virhekoodi, virhesanoma]


if __name__ == "__main__":
    pass
