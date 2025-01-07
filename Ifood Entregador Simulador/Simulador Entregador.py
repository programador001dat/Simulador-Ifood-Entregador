import os
import random
import time


#   coding: UTF-8   #   Author: Caio Ramos  #
os.system("clear")
def __main__():
    if __name__ == "__main__":
        """ IFOOD ENTREGADOR.py"""
        pass



class Ifood_Entregador:

    def __init__(self, online, offline):

        self.online = online
        self.offline = offline
        print("=================| OFFLINE |==================")
        self.usuario = str(input("(*)S\\n: "))

        if self.usuario == "s":
            print(f"\n[+]{self.online}\n")
            time.sleep(5)
            os.system("clear")
            print("==================| ONLINE |==================\n\n\n\n\n")
            pass

        elif self.usuario == "n":
            print(f"[-]{self.offline}\n")
            quit()

        else:
            print(f"[+]Name not defined >> {self.usuario}!\n")
            quit()

    def corrida_entregador(self):
        args_high = [15.65, 17.50, 19.23, 21.0, 25.10]
        args_low = [6.50, 7.93, 8.32, 10.0, 12.98]
        route = [6.12, 7.93, 8.0, 10.0, 14.12, 16.96, 18.21, 21.0]

        x = random.choice(args_high)
        y = random.choice(args_low)
        w = random.choice(route)

        if w < 13:
            time.sleep(3)
            print("..............................................")
            import dicionario
            print(f"(rota: {w}km\t<-|->\tdinheiro: {y}$)")
            print("==============================================")


            def accept_route_low(yes, no):
                code = ["4293", "3882", "5822", "9292", "0232"]
                self.yes = yes
                self.no = no
                self.user = input("(*)S\\n: ")
                if self.user == "s":
                    print(f"\n(C)Route accept: {yes}\n")
                    time.sleep(1)
                    codes_random = random.choice(code)
                    print(f"(?)codigo da coleta:\t\t\t|{codes_random}|\n")
                    print("..............................................\n\n")



                elif self.user == "n":
                    print(f"(X)Route reject: {no}\n")
                    quit()

                else:
                    print(f"*Name not defined: {self.user}")
                    quit()

            accept_route_low(yes="yes", no="no")

        elif w > 14:
            time.sleep(3)
            print("..............................................")
            import dicionario
            print(f"(rota: {w}km\t<-|->\tdinheiro: {x}$)")
            print("==============================================")

            def route_high(yes, no):
                code = ["5593", "3080", "5822", "1292", "0232"]
                self.yes = yes
                self.no = no
                self.user = input("(*)S\\n: ")
                if self.user == "s":
                    print(f"\n(C)Route accept: {self.yes}\n")
                    time.sleep(1)
                    codes_random = random.choice(code)
                    print(f"(?)codigo da coleta:\t\t\t|{codes_random}|\n")
                    print("..............................................\n\n")



                elif self.user == "n":
                    print(f"(X)Route reject: {self.no}\n")
                    quit()

                else:
                    print(f"*Name not defined: {self.user}")
                    quit()

            route_high(yes="yes", no="no")


Dev_Codigo = Ifood_Entregador(online="online", offline="offline")

Dev_Codigo.corrida_entregador()