import functools


# --- Завдання 1: Опис класу ---
# Клас: Рядок (MyString)
# Властивості: Значення, довжина
# Методи: Отримання підрядка з цифрами, отримання підрядка з буквами,
#          перегрупування (букви, потім цифри), виведення рядка

@functools.total_ordering  # Автоматично реалізує всі методи порівняння
class MyString:
    """
    Клас для демонстрації роботи з рядками, що реалізує
    вимоги варіанту 14.
    """

    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Значення має бути рядком (str)")
        self._value = value

    @property
    def value(self) -> str:
        """Повертає значення рядка."""
        return self._value

    @value.setter
    def value(self, new_value: str):
        """Встановлює нове значення рядка."""
        if not isinstance(new_value, str):
            raise TypeError("Значення має бути рядком (str)")
        self._value = new_value

    @property
    def length(self) -> int:
        """Повертає довжину рядка (обчислювана властивість)."""
        return len(self._value)

    def get_digits(self) -> str:
        """Повертає підрядок, що складається тільки з цифр."""
        return "".join(c for c in self._value if c.isdigit())

    def get_letters(self) -> str:
        """Повертає підрядок, що складається тільки з букв."""
        return "".join(c for c in self._value if c.isalpha())

    def regroup(self) -> str:
        """
        Перегруповує символи: спочатку букви, потім цифри,
        потім всі інші символи.
        """
        letters = ""
        digits = ""
        other = ""
        for c in self._value:
            if c.isalpha():
                letters += c
            elif c.isdigit():
                digits += c
            else:
                other += c
        return letters + digits + other

    def print_string(self):
        """Виводить рядок у консоль."""
        print(self._value)

    # --- Допоміжні методи для Завдань 2 і 4 ---

    def __str__(self) -> str:
        """Для дружнього виведення (напр. print(obj))."""
        return self._value

    def __repr__(self) -> str:
        """Для представлення об'єкта (напр. у списку)."""
        return f"MyString(value='{self._value}')"

    def __eq__(self, other) -> bool:
        """
        Реалізація порівняння (необхідно для list.remove()
        та @total_ordering).
        """
        if isinstance(other, MyString):
            return self._value == other._value
        return False

    def __lt__(self, other) -> bool:
        """
        Реалізація "менше ніж" (для сортування та @total_ordering).
        Порівнюємо за алфавітом.
        """
        if not isinstance(other, MyString):
            return NotImplemented
        return self._value < other._value


# --- Завдання 2: Робота з колекціями ---

def demonstrate_collections():
    print("--- Завдання 2: Демонстрація колекцій ---")

    # У Python 'list' є універсальною структурою. Він одночасно є:
    # 1. "Узагальненою колекцією" (аналог List<T>):
    #    list[MyString] - це сучасний спосіб з підказками типів.
    # 2. "Звичайною колекцією" (аналог ArrayList):
    #    звичайний list може містити об'єкти будь-яких типів.
    # 3. "Масивом": list в Python - це динамічний масив.

    # Створимо "масив" / "список"
    collection: list[MyString] = [
        MyString("Test123String"),
        MyString("Py45Go"),
        MyString("Data90")
    ]
    print(f"Початкова колекція: {collection}")

    # 1. Додавання
    s4 = MyString("NewItem777")
    collection.append(s4)
    print(f"Після додавання: {collection}")

    # 2. Оновлення
    collection[1] = MyString("UpdatedItem45")
    print(f"Після оновлення: {collection}")

    # 3. Пошук елементу (за значенням)
    search_value = "Data90"
    found_item = None
    for item in collection:
        if item.value == search_value:
            found_item = item
            break
    print(f"Пошук '{search_value}': {found_item}")

    # 4. Видалення (за індексом та за значенням)
    # Видалення за індексом (видаляємо "Test123String")
    removed_by_index = collection.pop(0)
    print(f"Видалено за індексом: {removed_by_index}, Залишилось: {collection}")

    # Видалення за значенням (видаляємо "NewItem777")
    # Це працює, оскільки ми реалізували __eq__ в MyString
    collection.remove(s4)
    print(f"Видалено за значенням 'NewItem777', Залишилось: {collection}")

    # 5. Прохід по набору (Ітерація)
    print("Прохід по колекції:")
    for item in collection:
        item.print_string()

    print("\nПояснення відмінностей (C# vs Python):")
    print(" * C# Array (масив) має фіксований розмір. Python 'list' - динамічний.")
    print(
        " * C# List<T> (узагальнена) вимагає вказання типу під час компіляції. Python 'list' - ні, але підтримує 'type hints' (list[MyString]).")
    print(
        " * C# ArrayList (звичайна) - застаріла, зберігає 'object', що вимагає приведення типів. Python 'list' природно зберігає будь-які об'єкти без приведення.")
    print("Отже, в Python 'list' є основною і найбільш гнучкою колекцією.")


# --- Завдання 3: Узагальнене бінарне дерево ---
# У Python класи є "узагальненими" за замовчуванням.
# Обмеження C# "where T : class" (не структура) не має прямого
# аналога в Python, оскільки тут все є об'єктами.

class TreeNode:
    """Вузол бінарного дерева."""

    def __init__(self, value):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __repr__(self) -> str:
        return f"TreeNode(value={self.value})"


class BinaryTree:
    """
    Узагальнене бінарне дерево.
    У Завданні 4 ми додамо логіку вставки для BST (Binary Search Tree)
    та ітератор.
    """

    def __init__(self):
        self.root: TreeNode | None = None
        print("\n--- Завдання 3: Створено пусте бінарне дерево ---")

    # --- Методи для Завдання 4 ---

    def insert(self, value):
        """
        Вставляє значення в дерево, перетворюючи його
        на Бінарне Дерево Пошуку (BST).
        Потрібно, щоб об'єкти 'value' підтримували порівняння (<, >).
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value):
        if value < node.value:
            # Йдемо вліво
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            # Йдемо вправо
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        # else: значення вже існує, нічого не робимо

    def __iter__(self):
        """
        Реалізація ітератора (аналог IEnumerable).
        Використовує генератор для обходу дерева.
        """
        # "yield from" делегує ітерацію іншому генератору
        yield from self._postorder_traverse(self.root)

    def _postorder_traverse(self, node: TreeNode | None):
        """
        Приватний генератор, що реалізує ітератор (аналог IEnumerator)
        для зворотного обходу (postorder): Ліво -> Право -> Корінь.
        """
        if node is not None:
            yield from self._postorder_traverse(node.left)
            yield from self._postorder_traverse(node.right)
            yield node.value


# --- Завдання 4: Порівняння та Ітератори ---

def demonstrate_sorting_and_tree():
    print("\n--- Завдання 4: Порівняння та Ітератори ---")

    # --- Демонстрація сортування (IComparable та IComparer) ---

    sort_list = [
        MyString("gamma50"),
        MyString("alpha10"),
        MyString("zeta99"),
        MyString("beta30")
    ]
    print(f"\nСписок для сортування: {sort_list}")

    # 1. Сортування за замовчуванням (аналог IComparable<T>)
    # Використовує методи __lt__, __eq__ з класу MyString (алфавітне сорт.)
    sorted_default = sorted(sort_list)
    print(f"Сортування за замовчуванням (алфавіт): {sorted_default}")

    # 2. Сортування з ключем (аналог IComparer<T>)
    # Ми передаємо "стратегію" сортування - функцію (lambda)
    # Сортуємо за довжиною рядка
    sorted_by_length = sorted(sort_list, key=lambda s: s.length)
    print(f"Сортування за довжиною (key=...): {sorted_by_length}")

    # Сортуємо за цифровою частиною
    sorted_by_digits = sorted(sort_list, key=lambda s: s.get_digits())
    print(f"Сортування за цифрами (key=...): {sorted_by_digits}")

    # --- Демонстрація дерева (BST та Ітератор) ---

    bst = BinaryTree()  # Створюється в Завданні 3

    # Додаємо елементи. Це використовує методи порівняння з MyString
    print("\nДодавання елементів у бінарне дерево пошуку (BST)...")
    bst.insert(MyString("m50"))
    bst.insert(MyString("f20"))
    bst.insert(MyString("r80"))
    bst.insert(MyString("a10"))
    bst.insert(MyString("g30"))
    bst.insert(MyString("z90"))

    # Демонстрація ітератора (postorder)
    # Порядок (L, R, Root): a10, g30, f20, z90, r80, m50
    print("\nОбхід дерева (Ітератор) - Зворотний порядок (Postorder):")

    # 'for item in bst:' автоматично викликає bst.__iter__()
    for item in bst:
        item.print_string()


# --- Головна функція для запуску демонстрацій ---
def main():
    print("=== Лабораторна робота 3.2 (Варіант 14) - Виконання на Python ===")

    # Завдання 1: Демонстрація методів класу
    print("\n--- Завдання 1: Демонстрація класу MyString ---")
    my_str = MyString("PyTest_123!Go")
    print(f"Створено об'єкт: {my_str!r}")
    print(f"Довжина (length): {my_str.length}")
    print(f"Тільки букви (get_letters): {my_str.get_letters()}")
    print(f"Тільки цифри (get_digits): {my_str.get_digits()}")
    print(f"Перегрупування (regroup): {my_str.regroup()}")

    # Завдання 2
    demonstrate_collections()

    # Завдання 3 та 4 (вони пов'язані)
    demonstrate_sorting_and_tree()

    print("\n=== Виконання завершено ===")


if __name__ == "__main__":
    main()