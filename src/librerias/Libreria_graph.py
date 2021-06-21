# Graph – Implementación con matrix adyacente


'''
    Represent Vertex in Graph
'''


class Vertex:   # Clase Vertex

    def __init__(self, node):
        self.id = node #Iniciador de la clase, solo tendra un atributo que sera "id", y este tomara el valor de node que debera ser introducido al crear el objeto

    def getId(self):    # Encapsulamiento del atributo "id"
        return self.id

    def setId(self, id):
        self.id = id


'''
    Represent a Graph
'''


class Graph:    # Clase Graph

    def __init__(self, numVertices, cost=-1):   # La clase pedira datos para el parametro numVertices y se asigna -1 al parametro cost, este parametro tambien se puede cambiar si lo indicamos al momento de crear la clase
        self.adjMatrix \
            = [[cost for u in range(numVertices)]   # NOTA : el "/" nos permite hacer un salto de linea
                for v in range(numVertices)]        # Al atributo adjMatrix se le asigna una lista, esta lista contendra mas lista y estas tendra los valores de cost, habra tantas listas segun el numero de vertices se introdusca, usaremos estas listas, esto se da por que se esta iterando sobre la lista usando un bucle,
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setId(id)

    def getVertexIndex(self, n):
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getId():
                return vertxin
        return (-1)

    def getVertex(self, index):
        return self.vertices[index]

    def addEdge(self, frm, to, cost=0):
        if self.getVertexIndex(frm) != -1 \
        and self.getVertexIndex(to) != -1:
            idx_frm = self.getVertexIndex(frm)
            idx_to = self.getVertexIndex(to)
            self.adjMatrix[idx_frm][idx_to] = cost
            ''' For directed graph do not add this'''
            self.adjMatrix[idx_to][idx_frm] = cost

    def getVertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
            id_vert = self.vertices[vertxin].getId()
            vertices.append(id_vert)
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getId()
                    uid = self.vertices[u].getId()
                    edges.append((vid, uid, self.adjMatrix[u][v]))
        return edges

