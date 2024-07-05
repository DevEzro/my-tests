from main import suma

def test_suma():
    #Inserta los párametros al método y comprueba que la suma de ese resultado
    assert suma(1,2) == 3
    assert suma(7,54) == 61
    assert suma(3,1) == 4
    assert suma(8,9) == 16 #Aquí el test fallará
    assert suma(8,20) == 28