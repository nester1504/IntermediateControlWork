import json
from datetime import datetime

# Файл для хранения заметок в формате JSON
NOTES_FILE = "notes.json"


def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": msg,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена!")


def show_notes():
    for note in notes:
        print(
            f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}")
        print(note["message"])
        print("=" * 30)


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


def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    print("Заметка с таким ID не найдена.")


def filter_notes_by_date():
    date_str = input(
        "Введите дату для фильтрации заметок (в формате ГГГГ-ММ-ДД): ")
    try:
        filter_date = datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if datetime.strptime(
            note["created_at"], "%Y-%m-%d %H:%M:%S").date() == filter_date.date()]
        print("Список заметок за указанную дату:")
        show_notes(filtered_notes)
    except ValueError:
        print("Некорректный формат даты. Попробуйте ещё раз.")


def main():
    global notes
    notes = load_notes()

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
