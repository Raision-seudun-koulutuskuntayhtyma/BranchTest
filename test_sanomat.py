# SANOMAT.PY-MODULIN TESTIT

# Modulien ja kirjastojen lataukset
import sanomat





# ASCII-koodien summan testi
def test_summaa_merkit():
    assert sanomat.summaa_merkit('3000|4000|5003|3|') == 1138

# Testataan parannettu varmisteenlaskentafunktio
def test_muodosta_varmiste():
    merkit = '3000|4000|5003|3|'
    jakaja = 127
    assert sanomat.muodosta_varmiste(merkit, jakaja) == '122'

# Testataan yleiskäyttöinen sanomanmuodostusfunktio
def test_luo_sanoma():
    mitatut_arvot = [3000, 4000, 5003, 3]
    assert sanomat.luo_sanoma(mitatut_arvot, '<', '>', '|', 127) == '<3000|4000|5003|3|122>'

def test_pura_sanoma():
    # Sanoma on ehjä
    assert sanomat.pura_sanoma('<3000|4000|5003|3|122>','<','>', '|',127) == [['3000', '4000', '5003', '3'], 0, 'Data OK']
    
    # Sanoman alkumerkki puuttuu
    assert sanomat.pura_sanoma('3000|4000|5003|3|122>','<','>', '|',127) == [[], 1, 'Sanoma vajaa, alkumerkki puuttuu']

    # Sanoman loppumerkki puuttuu
    assert sanomat.pura_sanoma('<3000|4000|5003|3|122','<','>', '|',127) == [[], 2, 'Sanoma vajaa, loppumerkki puuttuu']

    # Sanomasta puuttuu joko data tai varmistussumma -> koodissa virhe ks. todo tree bug
    assert sanomat.pura_sanoma('<122>','<','>', '|',127) == [[], 3, "Sanoma ei sisällä tarvittavaa dataa, viestissä ainoastaan varmiste"]

    # Sanoman varmistussumma ei täsmää
    assert sanomat.pura_sanoma('<3000|4000|5003|3|121>','<','>', '|',127) ==[[], 4, 'Sanoma vahingoittunut, varmistussumma ei täsmää']