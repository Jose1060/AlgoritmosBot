#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:27:44 2019
@author: vanaurum
"""

import random
import sys
import time


class Node:
    """Esta clase es una implementación completa de un árbol binario con métodos para ejecutar una amplia variedad
    operaciones de árbol binario.
    Attributos:
    ___________
    data : int, str
    """

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:  # self.data > data
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

    def eval(self):  # Metodo que evalua los nodos en el arbol

        # Comprobamos que tenga dos nodos hijos
        if self.right is not None and self.left is not None:
            # Si el nodo tiene el valor de (+), suma el nodo que esta a la derecha
            # con el que esta a la izquierda
            if self.data == '+':
                return self.left.eval() + self.right.eval()
            # Si el nodo tiene el valor de (-), resta el nodo que esta a la derecha
            # con el que esta a la izquierda
            elif self.data == '*':
                return self.left.eval() * self.right.eval()

            elif self.data == '/':
                return self.left.eval() / self.right.eval()

            elif self.data == '-':
                return self.left.eval() - self.right.eval()

        else:  # Devolvemos el valor del nodo si no se cumple la condicion anterior
            return float(self.data)

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Devuelve una lista de cadenas, ancho, alto y coordenada horizontal de la raíz"""
        # No child exists.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child exists.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child exists.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# def build_tree(n, min_num, max_num, start=None):
#     if start:
#         initial = start
#     else:
#         initial = random.randint(min_num, max_num)
#     root = Node(initial)
#     for _ in range(n - 1):
#         root.insert(random.randint(min_num, max_num))
#     return root


# def is_balanced(root):
#     '''
#     Un árbol binario está equilibrado si:
#         - esta vacio
#         - el subárbol izquierdo está equilibrado
#         - el subárbol derecho está equilibrado
#         - la diferencia de profundidad entre la izquierda y la derecha es <= 1
#     '''
#     if root is None:
#         return True
#     # La función abs() calcula el valor absoluto de un número
#     return is_balanced(root.right) and is_balanced(root.left) and abs(
#         get_height(root.left) - get_height(root.right)) <= 1


def get_height(root):
    '''
    Devuelve la profundidad máxima del árbol.
    '''
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


# def inorderTraversal(root):
#     '''
#     Return an array of tree elements using inorder traversal.
#     Left-->Root-->Right
#     '''
#     res = []
#     if root:
#         res = inorderTraversal(root.left)
#         res.append(root.data)
#         res = res + inorderTraversal(root.right)
#     return res


# def postorderTraversal(root):
#     '''
#     Returns an array of tree elements using post order traversal.
#     Post order is often used to delete tree elements
#     Left-->Right-->Root
#     '''
#     res = []
#     if root:
#         res = postorderTraversal(root.left)
#         res = res + postorderTraversal(root.right)
#         res.append(root.data)
#
#     return res


# def preorderTraversal(root):
#     '''
#     Returns an array of tree elements using pre order traversal.
#     Pre order is often used to copy a tree
#     Root-->Left-->Right
#     '''
#     res = []
#     if root:
#         res.append(root.data)
#         res = res + preorderTraversal(root.left)
#         res = res + preorderTraversal(root.right)
#
#     return res


# def balance_tree(array):
#     '''
#     Balances an unbalanced binary tree in O(n) time from the inorder traversal
#     stored in an array
#     steps:
#         - Take inorder traversal of existing tree and store in array.
#         - Find value at mid point of this array.
#         - create new binary tree using this midpoint as root node.
#     '''
#     if not array:
#         return None
#
#     midpoint = len(array) // 2
#     new_root = Node(array[midpoint])
#     new_root.left = balance_tree(array[:midpoint])
#     new_root.right = balance_tree(array[midpoint + 1:])
#     return new_root


'''
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print ("Height of tree is %d" %(maxDepth(root)))
'''


# def getLeafCount(node):
#     '''
#     Count the number of leaf nodes in a tree
#     '''
#     if node is None:
#         return 0
#     if (node.left is None and node.right is None):
#         return 1
#     else:
#         return getLeafCount(node.left) + getLeafCount(node.right)


# def _deepestLeftLeafUtil(root, lvl, maxlvl, isLeft):
#     '''
#     # A utility function to find deepest leaf node.
#     # lvl:  level of current node.
#     # maxlvl: pointer to the deepest left leaf node found so far
#     # isLeft: A bool indicate that this node is left child
#     # of its parent
#     # resPtr: Pointer to the result
#     '''
#
#     # Base CAse
#     if root is None:
#         return
#
#     # Update result if this node is left leaf and its
#     # level is more than the max level of the current result
#     if (isLeft is True):
#         if (root.left == None and root.right == None):
#             if lvl > maxlvl[0]:
#                 _deepestLeftLeafUtil.resPtr = root
#                 maxlvl[0] = lvl
#                 return
#
#     # Recur for left and right subtrees
#     _deepestLeftLeafUtil(root.left, lvl + 1, maxlvl, True)
#     _deepestLeftLeafUtil(root.right, lvl + 1, maxlvl, False)
#

# A wrapper for left and right subtree
# def deepestLeftLeaf(root):
#     '''
#     Used with the above utility function to calculate deepest LEFT leaf
#     '''
#     maxlvl = [0]
#     _deepestLeftLeafUtil.resPtr = None
#     _deepestLeftLeafUtil(root, 0, maxlvl, False)
#     return _deepestLeftLeafUtil.resPtr


# def printRoute(stack, root):
#     '''
#     Print all routes down a binary tree
#     '''
#     if root == None:
#         return
#
#     # append this node to the path array
#     stack.append(root.data)
#     if (root.left == None and root.right == None):
#         # print out all of its
#         # root - to - leaf
#         print(' '.join([str(i) for i in stack]))
#
#         # otherwise try both subtrees
#     printRoute(stack, root.left)
#     printRoute(stack, root.right)
#     stack.pop()
#

def size(node):
    '''
    Compute the total number of nodes in a tree
    '''
    if node is None:
        return 0
    else:
        return (1 + size(node.left) + size(node.right))


operatorPrecedence = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def parserToTree(postfix):
    stack = []
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)
    return stack.pop()


def evalManual():
    opeNodeA = Node(5)
    opeNodeB = Node(3)

    sumNode = Node('+')
    sumNode.left = opeNodeA
    sumNode.right = opeNodeB

    opeNodeC = Node(6)
    mulNode = Node('*')
    mulNode.left = sumNode
    mulNode.right = opeNodeC

    print(mulNode.eval())


def evalPostfixExpression():
    postfix = "53+6*"
    rootNode = parserToTree(postfix)
    print(rootNode.eval())


def menu():
    print("********  Arboles  ********")
    x = int(input("Ingrese data de root >> "))
    root = Node(x)
    lim = int(input("Defina el cuantos elementos desea introducir al arbol =====> "))
    c = 0
    print("Recuerder que no se permiten NODOS REPETIDOS")
    while lim >= c:
        print("Introduzca el nodo: ", c, "de", lim)
        y = int(input("------>"))
        root.insert(y)
        c = c + 1

    print("Introduccion Finalizada")
    print("-" * 25)
    r = True
    while r:
        print("MENU")
        print(" 1.Mostrar arbol \n 2.Agregar \n 3.Mostrar Profundidad")
        op = int(input("------> "))
        if op == 0:
            r = False
        elif op == 1:
            root.display()
        elif op == 2:
            x = int(input("Ingrese el numero =====>"))
            root.insert(x)
        elif op == 3:
            a = get_height(root)
            print("La profundidad es de: ", a)
        else:
            print("/// NUMERO INVALIDO ///")
        print("-" * 25)
    return root


operatorPrecedence = {      # Diccionario con algunos operadores
    '(': 0,                # Cada operador tiene un valor
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# Se crea la funcion de parserPostfixToBinaryTree, para que funcione es necesario darle un parametro


def parserPostfixToBinaryTree(postfix):
    # con el orden de postfix como "53+6*", para mas informacion:

    # https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html

    stack = []                                  # Creamos una lista vacia
    for char in postfix:                        # Recorremos el string que introducimos en la funcion con el valor char
        # "char" ira tomando el valor de cada caracter del string
        if char not in operatorPrecedence:      # si char no esta en el diccionario de operadores
            # Se crea un Nodo donde el atributo "Data" tomara el valor de char.
            node = Node(char)
            # Se agrega el nodo a la lista stack
            stack.append(node)
        else:
            # Se crea un Nodo donde el atributo "Data" tomara el valor de char.
            node = Node(char)
            # Eliminamos el ultimo valor de la lista, pero lo guardamos en la variable local right
            right = stack.pop()
            # Eliminamos el ultimo valor de la lista, pero lo guardamos en la variable local left
            left = stack.pop()
            # Ponemos el atributo right de "node" la variable right, estariamos armando el arbol y este seria su primer hijo
            node.right = right
            # Ponemos el atributo left de "node" la variable left, segundo hijo
            node.left = left
            # Se añade node a la lista, "node" ya estaria siendo un binarytree
            stack.append(node)

    # Devolvemos y eliminamos el ultimo objeto de la lista stack
    return stack.pop()

#################################

# Declaramos la funcion evalPostfixExpression


def evalPostfixExpression(post):

    # Guardamos un string en la variable "postfix"
    postfix = post
    # Llamamos a la funcion de parserPostfixToBinaryTree y le pasamos el parametro de "postfix" , (linea 47)
    rootNode = parserPostfixToBinaryTree(postfix)
    # Ademas como la funcion nos devuelve un BinaryTree lo guardamos en "rootNode"

    # Usamos lel metodo de "eval" con nuestro BinaryTree y nos imprime el valor que nos devuelve, (linea 7)
    rootNode.display()
    return rootNode.eval()
    # print(rootNode.eval())


#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    # evalManual()

    # llamamos al funcion evalPostfixExpression, (linea 86)
    # (7+5)*(4/(2+2))
    # 4/8+5-1*7


def postfixConvert(infix):
    stack = []  #->     
    postfix = []  #     75+422+/*          ->      48/5+17*-

    for char in infix:  # Recorrido por los caracteres de infix
        if char not in operatorPrecedence:  # Si el caracter no esta en nuestro diccionario de operadores
            postfix.append(char)  # Se agrega a la lista de postfix
        else:
            if len(stack) == 0:  # Si el tamaño de la lista stack es0
                stack.append(char)  # Se agrega el caracter a la lista stack
            else:
                if char == "(":  # Si el caracter es un parentesis abierto
                    stack.append(char)  # Se agrega a la lista stack
                elif char == ")":   # Si el caracter es un parentesis cerrado
                    while stack[len(stack) - 1] != "(": #Mientras el ultimo elemento de la lista no sea parentesis cerrado
                        postfix.append(stack.pop()) #Se elimina los elementos de la lista stack y son agregados a la lista postfix
                    stack.pop() # Se elimina el parentesis abierto
                elif operatorPrecedence[char] > operatorPrecedence[stack[len(stack) - 1]]:  # Si el valor del caracter en el diccionario es mayor al valor en el diccionario de la ultima ultimo elemento de la lista stack
                    stack.append(char) # Se agrega a la lista stack
                else:
                    while len(stack) != 0:  # Mientras el tamaño de la lista stack no sea 0
                        if stack[len(stack) - 1] == '(': # Si el ultimo elemento de la lista stack es un (
                            break   # Se sale del bucle
                        postfix.append(stack.pop()) # Se agrega a la lista postfix el ultimo elemento de la lista stack y este es elimado de su lista
                    stack.append(char)  # Se agrega a la lista stack el caracter

    while len(stack) != 0:      # Mientras el tamaño de la lista stack no sea 0
        postfix.append(stack.pop()) # Se va eliminando de la lista stack y agregando a la lista postfix

    return "".join(postfix)     # Con un return regresamos la lista postfix, pero en formato de string, (una cadena de texto) con el comando join,ademas especificamos que no queremos separadores con las comillas vacias al principio de la funcion

#################################
# Third Case :  Convert indor to
#               postfix expression
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
#################################


def convertIndorToPostfixExp(indor):
    indor = indor
    postfix = postfixConvert(indor)  # “53+6*”
    return postfix


# ///////////////////////////////////////////////////////////////////////////////

def find(root, data):  # Buscar por el valor de nodo en los nodos del arbol
    '''
    Method to find data in BST
    Rparam root: Recursive
    :return:
    '''
    currentNode = root

    if currentNode == None:
        return None
    else:
        if data == currentNode.data:
            return currentNode
        if data < currentNode.data:
            return find(currentNode.left, data)
        else:   #data > currentNode.data
            return find(currentNode.right, data)


def findIterative(root, data):
    '''
    Method to find data in BST
    Iterative mode
    :param root:
    :return:
    '''
    currentNode = root

    while currentNode:
        if data == currentNode.data:
            return currentNode
        if data < currentNode.data:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

    return None


def findMin(root):
    '''
    Find the minimum value. Recursive mode
    :param root:
    :return:
    '''

    currentNode = root
    if currentNode.left == None:
        return currentNode
    else:
        return findMin(currentNode.left)


def findMinIterative(root):
    '''
    Find the minimum value. Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode.left != None:
        currentNode = currentNode.left
    return currentNode


def findMax(root):
    '''
    Find the maximum value. Recursive mode
    :param root:
    :return:
    '''
    currentNode = root
    if currentNode.right == None:
        return currentNode
    else:
        return findMax(currentNode.right)


def findMaxIterative(root):
    '''
    Find the maximum value. Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode.right != None:
        currentNode = currentNode.right
    return currentNode


#root1 = menu()

# root1.display()
