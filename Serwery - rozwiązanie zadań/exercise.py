#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Optional, Union, Dict
import re
from abc import ABC, abstractmethod


N_MAX = 5

class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę
    # produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą
    # atrybuty `name` (typu str) oraz `price` (typu float)
    
    def __init__(self, name: str, price: float):
        # price = float(price)
        if not isinstance(name, str):
            raise TypeError("Incorrect name")
        if not re.match("^[a-zA-Z]+[0-9]+$",name):
            raise ValueError("Incorrect number of characters")

        if not isinstance(price, (float,int)):
            raise TypeError("Cena musi być typu `float`")
        if price < 0:
            raise ValueError("Cena musi być dodatnią wartością")
        
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError(Exception):
    @staticmethod
    def check(server: Union['ListServer', 'MapServer']):
        if len(server._products) > server.get_n_max_returned_entries():
            raise TooManyProductsFoundError("Too many products to process.")


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą
#   atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int)
#   wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę
#   produktów spełniających kryterium wyszukiwania



# TODO:
# 1. Serwery powinny umożliwiać wyszukiwanie produktów, których nazwa składa się z dokładnie `n` liter (dowolnej wielkości),
#    a następnie 2–3 cyfr. Parametr `n` powinien być przekazywany do funkcji, a jego domyślna wartość to 1.
#    Wyniki powinny być zwracane jako lista produktów posortowana według rosnącej ceny.
# 2. Przykład: Dla `n = 2` serwer powinien znaleźć produkty o nazwach takich jak: AB12, ab123, ale nie A12, ab1, Ab1234 czy Abc12.
# 3. Jeśli żaden produkt nie spełnia kryterium, funkcja powinna zwracać pustą listę.
# 4. Jeśli liczba produktów spełniających kryteria przekracza `n_max_returned_entries` (wartość od 3 do 7, zdefiniowana jako atrybut klasowy),
#    funkcja powinna zgłosić wyjątek `TooManyProductsFoundError`.
# 5. Utwórz dwa typy serwerów:
#    - Serwer przechowujący produkty w postaci listy (`ListServer`).
#    - Serwer przechowujący produkty w postaci słownika (`MapServer`), gdzie kluczem jest nazwa produktu, a wartością – obiekt produktu.
# 6. Interfejs (API) obu serwerów powinien być identyczny. Zaleca się utworzenie abstrakcyjnej klasy bazowej, aby zapewnić wspólne
#    funkcjonalności obu typów serwerów.
# 7. Załóż, że w ramach danego serwera nazwy produktów są unikalne, więc nie jest konieczne ich dodatkowe sprawdzanie.
# 8. Upewnij się, że produkty na serwerach są przechowywane wyłącznie w ramach danego serwera i nie są współdzielone między serwerami.



class Server(ABC):
    #? Abstrakcyjna klasa bazowa dla serwerów przechowujących produkty."""
    n_max_returned_entries = N_MAX
    def __init__(self, products: List[Product]):
        self.products = products


    @abstractmethod
    def get_n_max_returned_entries(self) -> int:
        pass

    @abstractmethod
    def get_entries(self, n_letters: int) -> List[Product]:
        pass

    @abstractmethod
    def get_n_max_returned_entries(self) -> int:
        return self.n_max_returned_entries


class ListServer(Server):
    def __init__(self, products: List[Product]):
        if isinstance(products, List):
            for i in products:
                if not isinstance(i, Product):
                    raise TypeError("Item is not a Product")  #? nie wiem / po polsku: Element nie jest obiektem klasy Product
            self.products = products
        else:
            raise TypeError("Argument is not a list")  #? nie wiem / po polsku: Argument nie jest listą

        self.n_max_returned_entries = N_MAX

    def get_n_max_returned_entries(self) -> int:
        return self.n_max_returned_entries

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        #! Tworzenie wzorca na podstawie parametru `n_letters`
        pattern = rf"^[a-zA-Z]{{{n_letters}}}\d{{2,3}}$"

        filtered_products = [
            product for product in self.products if re.match(pattern, product.name)
        ]


        filtered_products.sort(key=lambda product: product.price)

        if len(filtered_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError("Too many products to process.")  #? nie wiem / po polsku: Zbyt wiele produktów do przetworzenia.

        return filtered_products


class MapServer(Server):
    def __init__(self, products: List[Product]):
        if not all(isinstance(product, Product) for product in products):
            raise TypeError("Każdy element na liście produktów musi być instancją klasy Product.")
        
        super().__init__(products)
        self.products: Dict[str, Product] = {product.name: product for product in products}
        self.n_max_returned_entries = N_MAX

    def get_n_max_returned_entries(self) -> int:
        return self.n_max_returned_entries

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        pattern = rf"^[A-Za-z]{{{n_letters}}}\d{{2,3}}$"
        
        filtered_products = [
            product for product in self.products.values()
            if re.fullmatch(pattern, product.name)
        ]


        filtered_products.sort(key=lambda product: product.price)

        if len(filtered_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError("Liczba produktów spełniających kryteria jest zbyt duża.")

        return filtered_products


#abstract class server
class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: Union[ListServer, MapServer]):
        self.server = server
    # kod z ich strony
    # def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
    #     raise NotImplementedError()
    def get_total_price(self, n_letters: Optional[int] = None) -> Optional[float]:
        if n_letters is None:
            return None
        try:
            entries = self.server.get_entries(n_letters)
            if len(entries) == 0:
                return None
            total_price = sum(product.price for product in entries)
            return total_price
        except TooManyProductsFoundError:
            return None
