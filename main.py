# File: main.py

from structures import ManagedString, BinaryTree


def demonstrate_task_1():
    """Демонстрація виконання Завдання 1: Робота з класом."""
    print("--- Завдання 1: Демонстрація класу ---")
    ms = ManagedString("Lab_Work_3_version_2")
    print(f"Оригінальний об'єкт: {ms}")
    print(f"Підрядок з буквами: {ms.get_letters_substring()}")
    print(f"Підрядок з цифрами: {ms.get_digits_substring()}")
    print(f"Перегрупований рядок: {ms.regroup_letters_first()}")
    print("-" * 20)


def demonstrate_task_2():
    """Демонстрація виконання Завдання 2: Робота з колекціями."""
    print("\n--- Завдання 2: Демонстрація роботи з колекцією (списком) ---")
    string_objects = [ManagedString("py100"), ManagedString("data25"), ManagedString("algo75")]
    print("Початковий список:")
    for item in string_objects: print(f"  - {item}")

    # Додавання
    string_objects.append(ManagedString("web30"))
    print("\nСписок після додавання 'web30':")
    for item in string_objects: print(f"  - {item}")

    # Видалення
    string_objects.pop(1)  # Видаляємо 'data25'
    print("\nСписок після видалення другого елементу:")
    for item in string_objects: print(f"  - {item}")

    # Оновлення
    string_objects[0] = ManagedString("python101")
    print("\nСписок після оновлення першого елементу:")
    for item in string_objects: print(f"  - {item}")

    # Пошук
    print("\nПошук елементу зі значенням 'algo75':")
    found = any(item.value == 'algo75' for item in string_objects)
    print(f"  - Елемент знайдено: {found}")
    print("-" * 20)


def demonstrate_tasks_3_and_4():
    """Демонстрація Завдань 3 і 4: Дерево, сортування, ітератор."""
    print("\n--- Завдання 3 та 4: Дерево, порівняння, сортування, ітератор ---")

    # Демонстрація сортування
    print("\n1. Демонстрація сортування:")
    sort_list = [
        ManagedString("Kyiv1"), ManagedString("Lviv"),
        ManagedString("Kharkiv2022"), ManagedString("Odesa"), ManagedString("Dnipro7")
    ]
    print("Несортований список:")
    for item in sort_list: print(f"  - {item}")

    sort_list.sort()
    print("\nСписок, відсортований за довжиною (вбудоване порівняння):")
    for item in sort_list: print(f"  - {item}")

    # Демонстрація дерева та ітератора (Завдання 3 + 4)
    print("\n2. Демонстрація бінарного дерева та ітератора:")
    tree = BinaryTree()
    elements_for_tree = [
        ManagedString("node8"), ManagedString("a3"), ManagedString("longstring12"),
        ManagedString("b44"), ManagedString("middle777"), ManagedString("z")
    ]
    print("Додаємо елементи в дерево:")
    for el in elements_for_tree:
        tree.insert(el)

    print("\nОбхід дерева у зворотньому порядку (post-order) за допомогою ітератора:")
    for item in tree:
        print(f"  - {item}")
    print("-" * 20)


if __name__ == "__main__":
    demonstrate_task_1()
    demonstrate_task_2()
    demonstrate_tasks_3_and_4()