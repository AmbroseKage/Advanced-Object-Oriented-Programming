from typing import List, Tuple, Callable, Set, Dict
 
 
# Funkcja powinna zwracać wartość parametru `x`, przy czym `x` powinien być typu
#   całkowitego oraz mieć domyślną wartość 0.
#
# Dodaj odpowiednie podpowiedzi typu.
#
# ĆWICZENIE NA: podpowiedzi typu, argumenty domyślne
def f_default_arg_immutable(x):
    pass
 
 
# Funkcja powinna przyjmować dwa argumenty:
#   (1) liczbę całkowitą oraz
#   (2) listę elementów typu całkowitego.
# Przekazanie listy jest opcjonalne, jeśli funkcja została wywołana z jednym
#   argumentem, powinno to zostać potraktowane jako przekazanie pustej listy.
# Jeśli przekazana lista zawiera mniej niż 3 elementy, na jej koniec należy
#   dołączyć element `x`.
# Funkcja powinna zwracać listę po ewentualnych modyfikacjach.
#
# Dodaj odpowiednie podpowiedzi typu.
#
# ĆWICZENIE NA: podpowiedzi typu, argumenty domyślne, len(), list.append()
def f_default_arg_mutable(x, data):
    pass
 
 
# Funkcja powinna zwracać trzyelementową krotkę zawierającą kolejno:
#   (1) pierwszy element listy `data`
#   (2) ostatni element listy `data`
#   (3) listę zawierającą elementy `data` od pierwszego do przedostatniego
# Przyjmij, że otrzymana lista zawsze zawiera co najmniej jeden element (nie
#   musisz tego sprawdzać ręcznie).
#
# ĆWICZENIE NA: krotka, indeksy (m.in indeksy ujemne), slicing
def f_indexing_and_slicing(data: List[int]) -> Tuple[int, int, List[int]]:
    pass
 
 
# Funkcja powinna zwrócić reprezentację listy wartości zmiennoprzecinkowych w postaci:
#       "<v1> - <v2> - ... - <vn>"
#   gdzie `<vi>` oznacza i-tą wartość podaną z dokładnością do dwóch miejsc po przecinku.
#   Przykładowo, dla listy [0.356, 1, 0.2] funkcja powinna zwrócić:
#       "0.36 - 1.00 - 0.20"
#
# Uzupenij podpowiedzi typwów.
#
# ĆWICZENIE NA: in, slicing, str.format(), konkatenacja łańcuchów znaków
def f_str_formatting(array):
    pass
 
 
# Funkcja powinna zamienić miejscami pierwszy i ostatni element listy `data`
#   za pomocą JEDNEJ instrukcji (bez używania zmiennych pomocniczych)!
#
# ĆWICZENIE NA: tuple packing, tuple unpacking
def f_swap(data: List[int]) -> None:
    pass
 
 
# Funkcja powinna zwrócić płytką kopię listy `l_in`.
#
# ĆWICZENIE NA: płytka kopia listy
def f_shallow_copy(l_in: List[int]) -> List[int]:
    pass
 
 
# Funkcja powinna zwrócić funkcję zwracającą wartość argumentu powiększoną o 1.
#
# ĆWICZENIE NA: lambda
def f_lambda() -> Callable[[int], int]:
    pass
 
 
# Funkcja powinna zwrócić wartość wyrażenia logicznego:
#   "x należy do przedziału obustronnie otwartego (1, 4)
#       lub (b1 jest prawdziwe i b2 jest fałszywe)"
#
# Uzupenij podpowiedzi typwów.
#
# ĆWICZENIE NA: wyrażenia logiczne, operatory logiczne
def f_logic(x, b1, b2):
    pass
 
 
# Funkcja powinna zwrócić listę składającą się z `n` elementów o wartości 1.
#
# ĆWICZENIE NA: operator `*` dla list
def f_list_creation(n: int) -> List[int]:
    pass
 
 
# Funkcja powinna zwrócić dwuelementową krotkę  zawierającą kolejno:
#   (1) sumę liczb od 2 do 10 z pominięciem 5 i 7
#   (2) zbiór (typ `set`) zawierający te klucze słownika `dct`, których wartość
#       zawiera się w przedziale obustronnie domkniętym [1, 5]
#
# ĆWICZENIE NA: comprehensions, range(), in, not in, dict.items(), set
def f_comprehensions(dct: Dict[int, int]) -> Tuple[int, Set[int]]:
    pass
 
 
# Zdefiniuj nazwaną krotkę `Point`, która służy do reprezentowania punktu na
#   płaszczyźnie (powinna zawierać składowe `x` i `y`, obie typu zmiennoprzecinkowego).
#
# ĆWICZENIE NA: nazwana krotka
class Point:
    pass
