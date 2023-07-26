# Простое консольное приложение для заметок

Это простое консольное приложение на Python, которое позволяет создавать, просматривать, редактировать и удалять заметки. Каждая заметка содержит идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения.

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.x.

2. Скачайте файл `notes.py` и сохраните его в удобной для вас папке.

3. Запустите скрипт `notes.py` из командной строки.

## Команды

После запуска приложения, вам будут доступны следующие команды:

1. **Добавить заметку**: Команда "1" позволяет добавить новую заметку. Вам будет предложено ввести заголовок и тело заметки.

2. **Просмотреть заметки**: Команда "2" отобразит список всех созданных заметок.

3. **Редактировать заметку**: Команда "3" позволяет изменить заголовок и тело существующей заметки. Вам потребуется ввести ID заметки, которую хотите отредактировать, а затем новый заголовок и текст.

4. **Удалить заметку**: Команда "4" позволяет удалить заметку. Вам нужно будет ввести ID заметки, которую хотите удалить.

5. **Фильтровать заметки по дате**: Команда "5" позволяет отфильтровать заметки по дате создания. Введите дату в формате "ГГГГ-ММ-ДД", чтобы увидеть все заметки, созданные в указанный день.

6. **Выход**: Команда "0" позволяет выйти из приложения.

## Сохранение заметок

Заметки сохраняются в формате JSON в файле `notes.json`. При повторном запуске приложения, созданные заметки будут загружены из этого файла.

**Обратите внимание**: Внесенные изменения в заметки сохраняются немедленно, поэтому важно быть внимательным при редактировании или удалении заметок.

## Завершение работы

Чтобы выйти из приложения, выберите команду "0". Все изменения будут сохранены в файле `notes.json`.

Приятного использования!