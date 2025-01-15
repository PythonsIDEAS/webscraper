# Book_finder
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>Проект для базы данных библиотеки</h1>

<p>Это простое приложение для базы данных библиотеки, созданное с использованием Python и Streamlit. Оно позволяет пользователям просматривать, искать и добавлять книги в базу данных библиотеки. Приложение использует базу данных SQLite для хранения информации о книгах, авторах, издателях и жанрах.</p>

<div class="section">
        <h2>Возможности</h2>
        <ul>
            <li>Просмотр всех книг в библиотеке с подробной информацией (название, автор, издатель, жанр, цена, количество доступных экземпляров).</li>
            <li>Поиск книг по названию и автору.</li>
            <li>Добавление новых книг в базу данных (ввод названия книги, ID автора, издателя, жанра, год издания, ISBN, цена, страницы, доступные экземпляры).</li>
            <li>Обработка ошибок при указании несуществующих ID авторов, издателей или жанров при добавлении книг.</li>
        </ul>
    </div>

<div class="section">
        <h2>Требования</h2>
        <p>Для запуска приложения потребуется установленный Python 3.x и библиотека Streamlit.</p>
        <p>Чтобы установить необходимые зависимости, выполните команду:</p>
        <pre><code>pip install streamlit</code></pre>
</div>

<div class="section">
    <h2>Структура файлов</h2>
    <h3>db.py</h3>
        <p>Этот файл содержит функции для взаимодействия с базой данных SQLite (library.db). Он управляет соединением с базой данных и предоставляет функции для получения книг, поиска книг по названию или автору и добавления новых книг в базу данных. Также этот файл инициализирует базу данных, если она не существует.</p>
        
<h4>Главные функции:</h4>
        <ul>
            <li><strong>get_db_connection()</strong>: Устанавливает и возвращает соединение с базой данных SQLite.</li>
            <li><strong>initialize_db()</strong>: Инициализирует базу данных и создает необходимые таблицы (authors, publishers, genres, books).</li>
            <li><strong>fetch_books()</strong>: Извлекает все книги из базы данных и возвращает их с дополнительной информацией (автор, издатель, жанр).</li>
            <li><strong>search_books_by_title(title)</strong>: Ищет книги по названию.</li>
            <li><strong>search_books_by_author(author_name)</strong>: Ищет книги по имени автора.</li>
            <li><strong>add_new_book()</strong>: Добавляет новую книгу в базу данных с указанными данными.</li>
        </ul>

<h3>main.py</h3>
        <p>Этот файл создаёт интерфейс Streamlit для взаимодействия с базой данных библиотеки. Он отображает все книги, позволяет искать книги по названию или автору и предоставляет форму для добавления новых книг в базу данных.</p>

<h4>Главные возможности:</h4>
        <ul>
            <li><strong>Отображение всех книг</strong>: Отображает все книги с их подробной информацией.</li>
            <li><strong>Поиск книг по названию</strong>: Позволяет искать книги по названию.</li>
            <li><strong>Поиск книг по автору</strong>: Позволяет искать книги по имени автора.</li>
            <li><strong>Добавление новой книги</strong>: Форма для добавления новых книг в базу данных.</li>
        </ul>
</div>

<div class="section">
        <h2>Как запустить</h2>
        <ol>
            <li>Клонируйте или скачайте этот репозиторий.</li>
            <li>Перейдите в папку проекта в терминале.</li>
            <li>Запустите приложение Streamlit командой:</li>
        </ol>
        <pre><code>streamlit run main.py</code></pre>
        <p>Откройте веб-браузер и перейдите по адресу <strong>http://localhost:8501</strong>, чтобы взаимодействовать с приложением.</p>
</div>

<div class="section">
    <h2>Лицензия</h2>
    <p>Этот проект лицензирован на условиях лицензии MIT - см. файл LICENSE для подробностей.</p>
</div>

</body>
</html>

