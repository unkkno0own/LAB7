# Заданий словник співробітників (прізвище: адреса)
employees = {
    "Іванов": "м. Київ, вул. Миру, 10",
    "Петров": "м. Львів, вул. Грушевського, 5",
    "Сидоров": "м. Харків, вул. Лесі Українки, 14",
    "Кузін": "м. Одеса, вул. Франка, 3",
    "Смирнов": "м. Дніпро, вул. Незалежності, 21",
    "Куравльов": "м. Полтава, вул. Шевченка, 8",
    "Кудін": "м. Чернігів, вул. Пушкіна, 12",
    "Соколов": "м. Суми, вул. Соборна, 4",
    "Кульков": "м. Черкаси, вул. Перемоги, 19",
    "Ковальчук": "м. Житомир, вул. Мазепи, 7"
}

# Список прізвищ для пошуку
target_lastnames = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]

# Функція для виведення всіх значень словника
def display_all_employees():
    print("Список всіх співробітників та їх адреси:")
    for lastname, address in employees.items():
        print(f"{lastname}: {address}")

# Функція для додавання нового запису
def add_employee(lastname, address):
    if lastname in employees:
        print(f"Співробітник з прізвищем {lastname} вже існує.")
    else:
        employees[lastname] = address
        print(f"Співробітника {lastname} успішно додано.")

# Функція для видалення запису
def remove_employee(lastname):
    if lastname in employees:
        del employees[lastname]
        print(f"Співробітника {lastname} успішно видалено.")
    else:
        print(f"Співробітника з прізвищем {lastname} не знайдено.")


# Функція для перегляду вмісту словника за відсортованими ключами
def display_sorted_employees():
    print("Співробітники за відсортованими прізвищами:")
    for lastname in sorted(employees.keys()):
        print(f"{lastname}: {employees[lastname]}")

# Функція для пошуку співробітників за певними прізвищами
def find_target_employees():
    found = False
    for lastname in target_lastnames:
        if lastname in employees:
            print(f"{lastname}: {employees[lastname]}")
            found = True
    if not found:
        print("Співробітників з такими прізвищами не знайдено.")

# Основне меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Вивести всіх співробітників")
        print("2. Додати нового співробітника")
        print("3. Видалити співробітника")
        print("4. Вивести співробітників за відсортованими прізвищами")
        print("5. Перевірити наявність співробітників з заданими прізвищами")
        print("0. Вихід")

        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            display_all_employees()
        elif choice == "2":
            lastname = input("Введіть прізвище нового співробітника: ")
            address = input("Введіть адресу нового співробітника: ")
            add_employee(lastname, address)
        elif choice == "3":
            lastname = input("Введіть прізвище співробітника для видалення: ")
            remove_employee(lastname)
        elif choice == "4":
            display_sorted_employees()
        elif choice == "5":
            find_target_employees()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main_menu()
