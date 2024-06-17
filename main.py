import Prog1, Prog2, Prog3, Prog4
import Prog5, Prog6, Prog7, Prog8
import Prog9, claves

def login():
    user = input("\nIngrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    service_id = input("\nIndique el servicio al que se desea comunicar: ")
    return user, password, service_id

def main(user, password, service_id):
    claves.generateAS()
    claves.generateTGS()
    Prog1.exec(user, password)
    Prog2.exec()
    Prog3.exec(user, password, service_id)
    Prog4.exec()
    Prog5.exec(service_id)
    Prog6.exec()
    Prog7.exec()
    Prog8.exec()
    Prog9.exec()
    
################### Main code #######################

user, password, service_id = login()

main(user, password, service_id)