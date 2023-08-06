import json
from datetime import datetime

NOTES_FILE = "notes.json"

# Функция для загрузки заметок из файла


def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []  # Если файл не найден, начинаем с пустого списка заметок
    return notes

# Функция для сохранения заметок в файл


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

# Функция для добавления новой заметки


def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": msg,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    notes.append(note)  # Добавляем новую заметку в список
    save_notes(notes)    # Сохраняем список заметок в файл
    print("Заметка успешно добавлена!")

# Функция для вывода всех заметок


def show_notes(notes_to_show=None):
    if not notes_to_show:
        notes_to_show = notes
    for note in notes_to_show:
        print(
            f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}")
        print(note["message"])
        print("=" * 30)

# Функция для редактирования заметки


def edit_note():
    note_id = int(
        input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            msg = input("Введите новое тело заметки: ")
            note["title"] = title
            note["message"] = msg
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с таким ID не найдена.")

# Функция для удаления заметки


def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    print("Заметка с таким ID не найдена.")

# Функция для фильтрации заметок по дате


def filter_notes_by_date():
    date_str = input(
        "Введите дату для фильтрации заметок (в формате ГГГГ-ММ-ДД): ")
    try:
        filter_date = datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if datetime.strptime(
            note["created_at"], "%Y-%m-%d %H:%M:%S").date() == filter_date.date()]
        if filtered_notes:
            print("Список заметок за указанную дату:")
            show_notes(filtered_notes)
        else:
            print("Заметки за указанную дату не найдены.")
    except ValueError:
        print("Некорректный формат даты. Попробуйте ещё раз.")

# Основная функция


def main():
    global notes
    notes = load_notes()  # Загружаем заметки из файла при запуске программы

    while True:
        print("\n===== Команды =====")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Фильтровать заметки по дате")
        print("0. Выход")

        command = input("Введите номер команды: ")

        if command == "1":
            add_note()
        elif command == "2":
            show_notes()
        elif command == "3":
            edit_note()
        elif command == "4":
            delete_note()
        elif command == "5":
            filter_notes_by_date()
        elif command == "0":
            break
        else:
            print("Некорректная команда. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
