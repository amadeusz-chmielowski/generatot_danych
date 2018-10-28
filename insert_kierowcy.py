import random
def create_insert_file():
    pesel = open("pesel_kierowcy.txt", "r")
    imie = open("imie.txt", "r")
    nazwisko = open("nazwisko.txt", "r")
    nr_telefonu = open("nr_telefonu.txt", "r")
    nr_prawa_jazdy = open("nr_prawa_jazdy.txt", "r")
    zdjecie = open("zdjecie_link.txt", "r")

    peseltable = pesel.readlines()
    imietable = imie.readlines()
    nazwiskotable = nazwisko.readlines()
    nr_telefonutable = nr_telefonu.readlines()
    nr_prawa_jazdy_table = nr_prawa_jazdy.readlines()
    zdjecietable = zdjecie.readlines()

    kierowca = open("kierowcy.sql", "w")

    for i in range(150):
        if zdjecietable[i].strip()[0] == '?':
            zdjecietable[i] = "https://placeholdit.imgix.net/default"
        FK_marka = random.randint(0, 2500)
        kierowca.write("insert into KIEROWCY values (" + "\'" + peseltable[i].strip() + "\'" + ", "
                     + "\'" + imietable[i].strip() + "\'" + ", "
                     + "\'" + nazwiskotable[i].strip() + "\'" + ", "
                     + "\'" + nr_telefonutable[i].strip() + "\'" + ", "
                     + "\'" + nr_prawa_jazdy_table[i].strip() + "\'" + ", "
                     + "\'" + zdjecietable[i].strip() + "\'" + ", "
                     + "\'" + str(FK_marka) + "\'"
                     + ");\n")


create_insert_file()