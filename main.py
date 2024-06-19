from AS import Prog1, Prog2
from TGS import Prog3, Prog4, Prog8
from SS import Prog5, Prog6, Prog7,Prog9
import claves

def login():
    user = input("\nIngrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    service_id = input("\nIndique el servicio al que se desea comunicar: ")
    return user, password, service_id

def main(user, password, service_id):

    Prog1.exec(user, password)
    Prog2.exec()
    Prog3.exec(user, password, service_id)
    Prog4.exec()
    Prog5.exec(service_id)
    Prog6.exec()
    Prog7.exec()
    claves.generateAS()
    claves.generateTGS()
    Prog8.exec()
    Prog9.exec()
    
################### Main code #######################

user, password, service_id = login()

main(user, password, service_id)
