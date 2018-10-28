# -*- coding: utf-8 -*-
from faker import Factory

pesel = []
imie = []
nazwisko = []
nr_telefonu = []
email = []
nip = []
nr_karty = []
data_wygasniecia = []
CVV = []
miasto = []
ulica = []
nr_bloku = []
id = []
marki = []
model = []
nr_rejestracyjny = []
liczba_miejsc = []
klasa = []
nr_prawa_jazdy = []
zdjecie_link= []
oplata = []
kilometry = []
status_platnosci = []
nr_faktury = []
data_godzina = []
fake = Factory.create('pl_PL')
fake2 = Factory.create()


def fill_function():
    for iterator in range(2700):
        pesel_one = fake.random_number(11)
        if len(str(pesel_one)) != 11:
            z = 11 - len(str(pesel_one))
            for _ in range(z):
                pesel_one = str(pesel_one)
                pesel_one = "0" + str(pesel_one)
        pesel.append(pesel_one)
        imie.append(fake.first_name())
        nazwisko.append(fake.last_name())
        nr_telefonu.append(fake.phone_number().replace('+48', '').replace(' ', ''))
        email.append(fake.email())
        nip_one = fake.random_number(10)
        if len(str(nip_one)) != 11:
            z = 11 - len(str(nip_one))
            for _ in range(z):
                nip_one = str(nip_one)
                nip_one = "0" + str(nip_one)
        nip.append(nip_one)
        nr_karty.append(fake.credit_card_number(card_type=None))
        data_wygasniecia.append(fake.date_this_decade(before_today=False, after_today=True))
        CVV.append(fake.credit_card_security_code(card_type=None))
        miasto.append(fake.city())
        ulica.append(fake.street_name())
        nr_bloku.append(fake.random_digit())
        id.append(iterator)
        marki.append(fake2.company())
        model.append(fake.hexify(text="^^^^", upper=False))
        nr_rejestracyjny.append(fake.license_plate())
        liczba_miejsc.append(fake.random_elements(elements=('1', '2', '3', '4', '5', '6'), length=1, unique=False)[0])
        klasa.append(fake.random_elements(elements=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'), length=1, unique=False)[0])
        nr_prawa_jazdy.append(fake.random_number(13))
        zdjecie_link.append(fake.image_url(width=None, height=None))
        oplata.append(fake.pydecimal(left_digits=2, right_digits=2, positive=True))
        kilometry.append(fake.pydecimal(left_digits=2, right_digits=3, positive=True))
        status_platnosci.append(fake.random_elements(elements=('1', '0'), length=1, unique=False)[0])
        data_godzina.append(str(fake.date_this_decade(before_today=False, after_today=True)) +" " +  str(fake.time(pattern="%H:%M:%S", end_datetime=None)))

    for _ in range(1000000):
        nr_faktury.append(str(fake.random_number(11))+"/2018")


def create_file(name, list_of_elements):
    file = open(name+".txt", "a+")
    for i in range(2500):
        file.write(str(list_of_elements[i])+"\n")


def create_faktura(name, list_of_elements):
    file = open(name+".txt", "a+")
    for i in range(1000000):
        file.write(str(list_of_elements[i]) + "\n")

def create_kierowcy():
    file = open("pesel_kierowcy.txt", "a+")
    for i in range(2501, 2700):
        file.write(str(pesel[i]) + "\n")


fill_function()
create_file("pesel", pesel)
create_file("imie", imie)
create_file("nazwisko", nazwisko)
create_file("nr_telefonu", nr_telefonu)
create_file("email", email)
create_file("nip", nip)
create_file("nr_karty", nr_karty)
create_file("data_wygasniecia", data_wygasniecia)
create_file("CVV", CVV)
create_file("miasto", miasto)
create_file("ulica", ulica)
create_file("nr_bloku", nr_bloku)
create_file("id", id)
create_file("marki", marki)
create_file("model", model)
create_file("nr_rejestracyjny", nr_rejestracyjny)
create_file("liczba_miejsc" , liczba_miejsc)
create_file("klasa", klasa)
create_file("nr_prawa_jazdy", nr_prawa_jazdy)
create_file("zdjecie_link", zdjecie_link)
create_file("oplata", oplata)
create_file("kilometry", kilometry)
create_file("data_godzina", data_godzina)
create_file("status_platnosci", status_platnosci)
create_faktura("nr_przejazdu", nr_faktury)
create_kierowcy()