'''PRUEBA TECNICA 1 (Tom necesita ayuda)
Tom es estudiante de ciencias de la computación y se encuentra estudiando una misteriosa Dirección websocket que encontró
en un profundo foro de internet que le planteaba un reto a Todos los lectores, que de lograrlo, descubriría la identidad
de nada más ni nada menos que de Satoshi Nakamoto. El funcionamiento de este stream websocket es muy simple: consiste
en conectarse y recibir cada 100 ms 100 JSON diferentes con la misma estructura:
{
"a": 1, // Rango -> [1, 100]
"b": 0 // Rango -> [0, 2^32)
}
Tom analizando se dio cuenta de algo, de un patrón, y es que si organizamos los datos de cierta forma, se podía conseguir
información muy valiosa que nos ayudaría a completar el reto. Tom piensa que el parámetro “a” representa un índice y el
“b” es un número sacado de una secuencia numérica extraña y desconocida, el cual aún no conoce la fórmula. Por
ello, creó un sistema de 100 bloques de información con igual estructura que contenía un resumen de un minuto, con el
comportamiento de los valores que se obtenían de “b”. La estructura usada es la siguiente:
struct {_max_number;
min_number;
first_number;
last_number;
number_of_prime_numbers;
number_of_even_numbers;
number_of_odd_numbers;
}
● El primer dato representa cuál fue el número mayor obtenido de “b” en ese periodo de tiempo.
● El segundo, el número menor.
● El tercero, el primer número obtenido.
● El cuarto, el último.
● El quinto es un contador que nos dice cuántos de esos números fueron números primos.
● El sexto, otro contador pero de cuantos fueron números pares.
● El séptimo, un contador que nos dice cuántos números fueron impares.
Tom necesita recolectar toda esa información en los diferentes bloques e imprimirlos cada vez que pase un minuto y luego
reiniciarlos, para seguir procesando nuevos datos venideros, esto le servirá para analizar su comportamiento a través del
tiempo. Pero tiene un problema, Tom a pesar de ser un estudiante de ciencias de la computación ¡no sabe programar!,
Entonces nos pide su ayuda, ¿estás dispuesto a ayudar a Tom?
'''

from websocket import create_connection


def connection():
    ws = create_connection('ws://209.126.82.146:8080')
    print("Receiving... \n ----------------")
    result = ws.recv()
    print("Received Json: '%s'" % result)
    ws.close()
    return result

class ManagementInformation():
    def get_information(self):
        cont = 0
        number_of_even_numbers = 0
        number_of_odd_numbers = 0

        while True:
            result = connection()
            final_str = result[:-1]
            b = final_str[13:30]
            print("numero b: ", b)

            if cont == 0:
                max_number = b
                min_number = b
                first_number = b
                last_number = b
                number_of_prime_numbers = self._sum_prime(int(b))
                if self._is_even_odd(int(b)) == 1:
                    number_of_even_numbers = 1
                else:
                    number_of_odd_numbers = 1

                bloque = {
                    "max_number": max_number,
                    "min_number": min_number,
                    "first_number": first_number,
                    "last_number": last_number,
                    "number_of_prime_numbers": number_of_prime_numbers,
                    "number_of_even_numbers": number_of_even_numbers,
                    "number_of_odd_numbers": number_of_odd_numbers,
                }
                print("\n Bloque de informacion inicial\n ")
                print(bloque)

            if cont == 10:
                bloque = {
                    "max_numberrr": max_number,
                    "min_number": min_number,
                    "first_number": first_number,
                    "last_number": last_number,
                    "number_of_prime_numbers": number_of_prime_numbers,
                    "number_of_even_numbers": number_of_even_numbers,
                    "number_of_odd_numbers": number_of_odd_numbers,
                }
                print("\n Bloque de informacion \n ")
                print(bloque)
                cont = 0
            max_number = self._compare_max(max_number, b)
            min_number = self._compare_min(min_number, b)
            number_of_prime_numbers = number_of_prime_numbers + self._sum_prime(int(b))
            cont = cont + 1
            last_number = b

            if self._is_even_odd(int(b)) == 1:
                number_of_even_numbers = number_of_even_numbers + 1
            else:
                number_of_odd_numbers = number_of_odd_numbers + 1

    def _compare_max(self, max_number, b):
        if b > max_number:
            return b
        else:
            return max_number

    def _compare_min(self, min_number, b):
        if b < min_number:
            return b
        else:
            return min_number

    def _sum_prime(self, b):
        for i in range(2, b):
            if b % i == 0:
                return 0
            return 1

    def _is_even_odd(self, b):
        if b % 2 == 0:
            return 1
        else:
            return 0

prueba = ManagementInformation()
prueba.get_information()