from Ejercicio_02 import CancionNoEncontradaError

## Ejercicio 4 — Playlist sobre lista enlazada (14 pts)

##Implementar, con nodos propios:

#```python
#class Nodo:
#    def __init__(self, dato, siguiente=None): ...

#class ListaEnlazada:
#    def esta_vacia(self) -> bool: ...
#    def tamanio(self) -> int: ...
#    def insertar_al_inicio(self, dato): ...
#    def insertar_al_final(self, dato): ...
#    def quitar_primero(self): ...
#    def __iter__(self): ...
#```

#`quitar_primero` devuelve el dato que estaba al frente y lo saca de la lista. El iterador recorre desde el primero hasta el último y termina con `StopIteration` (o con `yield`).

#Definir `Playlist`, que guarda canciones en una `ListaEnlazada`. No tiene tope de cantidad.

#- `agregar(cancion)` la inserta al final.
##- `quitar(id)` saca la canción con ese `id`. Si no está en la playlist, lanza `CancionNoEncontradaError`.
#- `listar()` devuelve los `__str__` recorriendo el iterador de la lista.
#- `duracion_total()` devuelve la suma de `duracion_seg` recorriendo el iterador. Playlist vacía: `0`.

#**Teoría.** La lista solo guarda una referencia al primer nodo. ¿Cuántos nodos se recorren para insertar al final cuando ya hay `n` elementos?

class Nodo:
    def __init__ (self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__ (self):
        self.primero = None

    def esta_vacia (self):
        if self.primero == None:
            return True
        else:
            return False
        
    def tamanio (self):
        cantidad = 0
        nodo_actual = self.primero
        while nodo_actual != None:
            cantidad = cantidad + 1
            nodo_actual = nodo_actual.siguiente
        return cantidad
    
    def insertar_al_inicio (self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo

    def insertar_al_final (self, dato):
        nuevo = Nodo(dato)
        if self.primero == None:
            self.primero = nuevo
        else:
            nodo_actual = self.primero
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo

    def quitar_primero (self):
        if self.primero == None:
            raise IndexError ("La lista esta vacia")
        dato_guardado = self.primero.dato
        self.primero = self.primero.siguiente
        return dato_guardado

    def __iter__ (self):
        nodo_actual = self.primero
        while nodo_actual != None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        
class Playlist:
    def __init__ (self):
        self.lista = ListaEnlazada()
    
    def agregar (self, cancion):
        self.lista.insertar_al_final(cancion)

    def quitar (self, id):
        nueva_lista = ListaEnlazada()
        encontrada = False

        for cancion in self.lista:
            if cancion.id == id and encontrada == False:
                encontrada = True
            else:
                nueva_lista.insertar_al_final(cancion)
            
        if encontrada == False:
            raise CancionNoEncontradaError ("No se encontro la cancion")

        self.lista = nueva_lista

    def listar (self):
        resultado = []    
        
        for cancion in self.lista:
            resultado.append(cancion.__str__())
        return resultado

    def duracion_total (self):
        total = 0
        for cancion in self.lista:
            total = total + cancion.duracion_seg
        return total


#RTA Teorica: Se recorren los nodos existentes desde el primero al ultimo para encontrar el final y enganchar el nuevo nodo