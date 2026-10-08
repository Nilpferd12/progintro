def uloha_1():
    input_str = input("Zadej delku v mm: ")
    input_float = float(input_str)
    print(f"Delka: {input_float} mm")
    print(f"Delka: {input_float / 10:06.3f} cm = {input_float / 1000:09.3f} m = {input_float / 25.4:09.3f} in")
    #:09.3f -- :09 udava minimalni delku stringu, ktery ma byt vypsan(doplni se pripadne odsazenim nulamy kdyz neni dost dlouhy), .3f udava pocet desetinych mist


uloha_1 ()