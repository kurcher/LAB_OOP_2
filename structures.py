# File: structures.py

import re

class ManagedString:
    """
    Клас для роботи з рядком, що містить букви та цифри.
    Містить логіку для порівняння об'єктів за довжиною.
    """
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Значення повинно бути рядком")
        self.value = value
        self.length = len(value)

    def get_digits_substring(self) -> str:
        """Повертає підрядок, що складається тільки з цифр."""
        return "".join(re.findall(r'\d', self.value))

    def get_letters_substring(self) -> str:
        """Повертає підрядок, що складається тільки з букв."""
        return "".join(re.findall(r'[a-zA-Zа-яА-Я]', self.value))

    def regroup_letters_first(self) -> str:
        """Перегруповує рядок: спочатку всі букви, потім усі цифри."""
        return self.get_letters_substring() + self.get_digits_substring()

    def __str__(self) -> str:
        """Повертає рядкове представлення об'єкта для виведення."""
        return f"ManagedString(value='{self.value}', length={self.length})"

    def __repr__(self) -> str:
        """Повертає репрезентацію об'єкта для його відтворення."""
        return f"ManagedString('{self.value}')"

    # --- Реалізація порівняння (аналог IComparable<T>) ---
    def __eq__(self, other):
        if not isinstance(other, ManagedString):
            return NotImplemented
        return self.length == other.length

    def __lt__(self, other):
        if not isinstance(other, ManagedString):
            return NotImplemented
        return self.length < other.length

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class Node:
    """Вузол бінарного дерева."""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    """
    'Узагальнене' бінарне дерево пошуку.
    Реалізує ітератор для зворотного обходу (post-order).
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Вставляє новий вузол у дерево, якщо дані є об'єктом ManagedString."""
        if not isinstance(data, ManagedString):
             raise TypeError("Дерево може зберігати лише об'єкти ManagedString")
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    # --- Реалізація ітератора (аналог IEnumerable/IEnumerator) ---
    def __iter__(self):
        """Повертає генератор для зворотного обходу (post-order)."""
        return self._post_order_traversal(self.root)

    def _post_order_traversal(self, node):
        """Рекурсивний генератор для зворотного обходу."""
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield node.data