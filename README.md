<h1>Курсовая 7. Django REST framework (DRF)</h1>
<br><br>
Django REST framework (DRF) — это библиотека, которая работает со стандартными моделями Django для создания гибкого и
мощного API для проекта.<br><br>
Задание
<br><br>
Контекст<br>
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и<br>
искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер<br>
полезных привычек.<br>

В рамках курсового проекта реализуйте бэкенд-часть SPA веб-приложения.
<br><br><h2>Критерии приемки курсовой работы</h2><br><br>
* Настроили CORS.<br>
* Настроили интеграцию с Телеграмом.
* Реализовали пагинацию.
* Использовали переменные окружения.
* Все необходимые модели описаны или переопределены.
* Все необходимые эндпоинты реализовали.
* Настроили все необходимые валидаторы.
* Описанные права доступа заложены.
* Настроили отложенную задачу через Celery.
* Проект покрыли тестами как минимум на 80%.
* Код оформили в соответствии с лучшими практиками.
* Имеется список зависимостей.
* Результат проверки Flake8 равен 100%, при исключении миграций.
* Решение выложили на GitHub.<br><br>
<h2>Описание задач</h2><br><br>
* Добавьте необходимые модели привычек.
* Реализуйте эндпоинты для работы с фронтендом.
* Создайте приложение для работы с Telegram и рассылками напоминаний.
<br><br><h2>Модели</h2>
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:
<br><br>
* я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]<br><br>
За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка <br>
не должна расходовать на выполнение больше двух минут. Исходя из этого получаем первую модель — «Привычка».<br><br>

<br><br><h2>Привычка:</h2>
* Пользователь — создатель привычки.
* Место — место, в котором необходимо выполнять привычку.
* Время — время, когда необходимо выполнять привычку.
* Действие — действие, которое представляет собой привычка.
* Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
* Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
* Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
* Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
* Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
* Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

 
<h5>Чем отличается полезная привычка от приятной и связанной?</h5><br>
Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение определенное
вознаграждение (приятная привычка или любое другое вознаграждение).

Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в
качестве связанной для полезной привычки (в поле «Связанная привычка»).

Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим
вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь
связанную привычку.

Рассмотрим другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В
качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не
приятную привычку.

Признак приятной привычки — булево поле, которые указывает на то, что привычка является приятной, а не полезной.

Чтобы удержать текущих клиентов, часто используют вспомогательные, или «прогревающие», рассылки для информирования и
привлечения клиентов.

Разработайте сервис управления рассылками, администрирования и получения статистики.
Валидаторы
Исключить одновременный выбор связанной привычки и указания вознаграждения.

В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только
одно из двух полей.
Время выполнения должно быть не больше 120 секунд.

В связанные привычки могут попадать только привычки с признаком приятной привычки.

У приятной привычки не может быть вознаграждения или связанной привычки.

Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю, но не раз в 2 недели. За
одну неделю необходимо выполнить привычку хотя бы один раз.
Пагинация
Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.
Права доступа
Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.
Эндпоинты
Регистрация.
Авторизация.
Список привычек текущего пользователя с пагинацией.
Список публичных привычек.
Создание привычки.
Редактирование привычки.
Удаление привычки.
Интеграция
Для полноценной работы сервиса необходимо реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Телеграм, который будет заниматься рассылкой уведомлений.

Вспомнить, как работать с API Телеграма, можно в разделе «Подготовка к практике» в уроке Celery.
Безопасность
Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.
Документация
Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. При необходимости эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную!