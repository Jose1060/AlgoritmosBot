# Clase Nodo
class Nodo:
    def __init__(self, info):
        self.Info = info
        self.sig = None


# Clase Lista
class Lista:
    def __init__(self, *elem):
        self.__primero = None
        self.__ultimo = None
        self.__ant_actual = None

        for i in elem:
            self.insertar_ultimo(i)

    def insertar_inicio(self, *elem):
        for i in elem:
            nodo = Nodo(i)
            if (self.__primero != None):
                nodo.sig = self.__primero
            else:
                self.__ultimo = nodo

            self.__primero = nodo

    def insertar_ultimo(self, *elem):
        for i in elem:
            nodo = Nodo(i)
            if (self.__ultimo != None):
                self.__ultimo.sig = nodo
                self.__ant_actual = self.__ultimo
            else:
                self.__primero = nodo

            self.__ultimo = nodo

    def elimina_primero(self):
        if (self.__primero == None):
            return

        nodo = self.__primero
        self.__primero = nodo.sig
        del nodo

    def __add__(self, list2):
        list3 = Lista()

        nodo = self.__primero
        while (nodo != None):
            list3.insertar_ultimo(nodo.Info)
            nodo = nodo.sig

        if (type(elem) == int):
            list3.insertar_ultimo(elem)
            return list3

        nodo = list2.__primero
        while (nodo != None):
            list3.insertar_ultimo(nodo.Info)
            nodo = nodo.sig

        return list3

    def info_anterior(self):
        if (self.__primero == None or self.__ant_actual == None):
            return

        return self.__ant_actual.Info

    def eliminar_elem(self, elem):
        while (self.__primero != None and self.__primero.Info == elem):
            temp = self.__primero
            self.__primero = temp.sig
            del temp

        nodo = self.__primero
        while (nodo != None):
            while (nodo.sig != None and nodo.sig.Info == elem):
                temp = nodo.sig
                if (temp == self.__ultimo):
                    self.__ultimo = nodo
                nodo.sig = temp.sig
                del temp
            nodo = nodo.sig

    def sig(self):
        if (self.__primero == None):
            return
        if (self.__ant_actual == None):
            self.__ant_actual = self.__primero
            return
        actual = self.__ant_actual.sig
        if (actual.sig != None):
            self.__ant_actual = actual

    def elimina_actual(self):
        if (self.__primero == None):
            return
        if (self.__ant_actual == None):
            temp = self.__primero
            self.__primero = temp.sig
            del temp
        else:
            temp = self.__ant_actual.sig
            self.__ant_actual.sig = temp.sig
            del temp

    def cons(self):
        if (self.__primero == None):
            return
        if (self.__ant_actual == None):
            return self.__primero.Info
        return self.__ant_actual.sig.Info

    def inicio(self):
        self.__ant_actual = None

    def actual_es_ultimo(self):
        if (self.__ant_actual != None):
            if (self.__ant_actual.sig == self.__ultimo):
                return True
        return False

    def mostrar(self):
        nodo = self.__primero
        while (nodo != None):
            print (nodo.Info)
            nodo = nodo.sig
        print


# def menu():
#     print("MENU")
#     print(" 1.Listar \n 2.Agregar \n 3.Eliminar el ultimo \n 4.Eliminar el primero \n 5.Insertar al inicio \n "
#           "6.Insertar al final \n 0.Salir")
#     op = input("------> ")
#     if op == 0:
#         r = False
#         return r
#     elif op == 1:
#         Lista.mostrar()
#     elif op == 2:
#         print("HOLA")
#         a = input("Numero")
#         print("HOLA2")
#         Lista(a)

"""
node1 = Nodo(10)
node2 = Nodo(20)
node1.sig = node2
print(Lista)
l = Lista()

r = True
while r == True:
    print("MENU")
    print(" 1.Listar \n 2.Agregar \n 3.Eliminar el ultimo \n 4.Eliminar el primero \n 5.Insertar al inicio \n "
          "6.Insertar al final \n 0.Salir")
    b = input("::::::> ")
    if b == "0":
        r = False

    elif b == "1":
        print("-"*35)
        l.mostrar()
        print("-" * 35)

    elif b == "2":
        num = int(input("========>"))
        l.insertar_inicio(num)

    elif b == "3":
        l.elimina_actual()

    elif b == "4":
        l.elimina_primero()

    elif b == "5":
        num = int(input("========>"))
        l.insertar_inicio(num)

    elif b == "6":
        num = int(input("========>"))
        l.insertar_ultimo(num)
"""