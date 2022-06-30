-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: std-mysql
-- Время создания: Июн 30 2022 г., 11:16
-- Версия сервера: 5.7.26-0ubuntu0.16.04.1
-- Версия PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `std_1690_exam`
--

-- --------------------------------------------------------

--
-- Структура таблицы `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('4d4c5c5c25f5');

-- --------------------------------------------------------

--
-- Структура таблицы `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `short_description` text NOT NULL,
  `year` int(11) NOT NULL,
  `publishing_house` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `pages` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `books`
--

INSERT INTO `books` (`id`, `name`, `short_description`, `year`, `publishing_house`, `author`, `pages`, `rating_sum`, `rating_num`, `created_at`) VALUES
(10, 'Человек в футляре', 'Учитель греческого языка Беликов, работающий в сельской гимназии, любил держать вещи в футлярчиках, всего боялся и сам жил, словно в футляре, по принципу: «как бы чего не вышло». Этим принципом он буквально «терроризировал» гимназию и жителей села. Надежда появилась, когда в село приехала Варенька — «не девица, а мармелад», хотя уже и в возрасте, и «не прочь была замуж, хотя бы и за учителя греческого языка».', 1939, 'Журнал рассказов', 'Чехов А.П.', 16, 0, 0, '2022-06-30 10:35:22'),
(11, 'Доктор Сон', '«Доктор Сон» — роман американского писателя Стивена Кинга, продолжение истории романа «Сияние». В США роман поступил в продажу 24 сентября 2013 г. Стивен Кинг посвятил книгу американскому рок-музыканту Уоррену Зивону. Кинг и Зивон были близкими друзьями и некогда даже совместно выступали, о чём сказано в предисловии.', 2013, 'АСТ', 'Стивен Кинг', 531, 4, 1, '2022-06-30 10:37:25'),
(12, 'Здесь могут водиться тигры', 'Космический экипаж, прибыв на неизвестную планету, понимает, что она живая и рада их присутствию.', 1989, 'Азбука', 'Рэй Бредбери', 432, 0, 0, '2022-06-30 10:39:35'),
(13, 'Котлован', '«Котлова́н» — философская повесть Андрея Платонова, содержащая элементы гротеска, притчи и экзистенциального романа. Некоторые критики воспринимают повесть как антиутопию и жёсткую сатиру на СССР времён первой пятилетки. ', 1969, 'Грани', 'Платонов А. П.', 119, 0, 0, '2022-06-30 10:41:38'),
(14, 'История СССР в анекдотах', '\"Наши историки ломают голову над тем, каким быть новому Учебнику. А этот - чем плох? Ведь без нашего чувства юмора наша же история была бы короче...\" - из пролога автора.', 1991, 'Апрель', 'Марк Дубровский', 352, 0, 0, '2022-06-30 10:42:57'),
(15, 'Цинковые мальчики', '«Цинковые мальчики» — документальная книга белорусской писательницы Светланы Алексиевич, изданная в 1989 году и посвящённая Афганской войне.', 1989, 'Голоса в голове', 'Аликсевич А. А.', 266, 0, 0, '2022-06-30 10:47:47');

-- --------------------------------------------------------

--
-- Структура таблицы `book_genres`
--

CREATE TABLE `book_genres` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `book_genres`
--

INSERT INTO `book_genres` (`id`, `book_id`, `genre_id`) VALUES
(10, 11, 1),
(6, 12, 2),
(5, 10, 3),
(8, 14, 3),
(12, 15, 4),
(7, 13, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `covers`
--

CREATE TABLE `covers` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `object_id` int(11) DEFAULT NULL,
  `object_type` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `covers`
--

INSERT INTO `covers` (`id`, `file_name`, `mime_type`, `md5_hash`, `book_id`, `object_id`, `object_type`) VALUES
('022523da-d5ff-42dd-8b3d-68245bf239b8', 'kotlovan.jpg', 'image/jpeg', 'a2b423a4874187efb0ef8f05701d48cc', 13, NULL, 'books'),
('5b2c9d91-20af-4017-a66f-3ea2da67e1c0', 'chel.jpg', 'image/jpeg', '95859f80ea9d463574e6eb3dde8e1c44', 10, NULL, 'books'),
('5d86adf4-3d6f-4624-8c92-366eeb502b68', 'malchiki.jpg', 'image/jpeg', '8d0a9a427d35530695736f524d92887d', 15, NULL, 'books'),
('5f4be38a-01fd-4ec8-8cf6-bf5d1b52238d', 'docSleep.jpg', 'image/jpeg', 'b19db522adebfdc7ccf6101ae8b3c9f7', 11, NULL, 'books'),
('e3843642-4a4e-49e3-af83-4718e820a297', 'tigri.jpg', 'image/jpeg', '0c74483096ec88db797c9c9a6c4a9b2b', 12, NULL, 'books'),
('ff107f99-71b8-4e6c-af56-c518c7e63d53', 'story_in_anek.jpeg', 'image/jpeg', '184f75b56fb7ce96dd4c800aa4e6a3ce', 14, NULL, 'books');

-- --------------------------------------------------------

--
-- Структура таблицы `genres`
--

CREATE TABLE `genres` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `genres`
--

INSERT INTO `genres` (`id`, `name`) VALUES
(5, 'Безысходность'),
(4, 'Документальное'),
(3, 'Комедия'),
(2, 'Фантастика'),
(1, 'Хоррор');

-- --------------------------------------------------------

--
-- Структура таблицы `reviews`
--

CREATE TABLE `reviews` (
  `id` int(11) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `reviews`
--

INSERT INTO `reviews` (`id`, `book_id`, `user_id`, `rating`, `text`, `created_at`) VALUES
(2, 11, 1, 4, 'Нравится', '2022-06-30 12:19:30');

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `name`, `description`) VALUES
(1, 'admin', 'chelick'),
(2, 'moder', 'can do some stuff'),
(3, 'user', 'can see photos');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password_hash`, `last_name`, `first_name`, `middle_name`, `role_id`) VALUES
(1, 'user', 'pbkdf2:sha256:260000$lwGPhjCwaMIfREVn$2fd3f2b12b1d51a03a8ff88e52966760ad125ea7bcdcb958a4c5300c251b53b1', 'Motoro', 'Ivan', 'YES', 1),
(2, 'user2', 'pbkdf2:sha256:260000$JFvPvy1YsFFvOGWM$e45d1dffbe4f2b6dfc0b5917399c344e497cee3f3a73a5921931f68fa0844e2f', 'Ivan', 'Modero', 'No', 2),
(3, 'user3', 'pbkdf2:sha256:260000$JFvPvy1YsFFvOGWM$e45d1dffbe4f2b6dfc0b5917399c344e497cee3f3a73a5921931f68fa0844e2f', 'Usero', 'Ivan', 'Wha', 3);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Индексы таблицы `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `book_genres`
--
ALTER TABLE `book_genres`
  ADD PRIMARY KEY (`id`,`book_id`,`genre_id`),
  ADD KEY `fk_book_genres_genre_id_genres` (`genre_id`),
  ADD KEY `fk_book_genres_book_id_books` (`book_id`);

--
-- Индексы таблицы `covers`
--
ALTER TABLE `covers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_covers_md5_hash` (`md5_hash`),
  ADD KEY `fk_covers_book_id_books` (`book_id`);

--
-- Индексы таблицы `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_genres_name` (`name`);

--
-- Индексы таблицы `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reviews_user_id_users` (`user_id`),
  ADD KEY `fk_reviews_book_id_books` (`book_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_users_login` (`login`),
  ADD KEY `fk_users_role_id_roles` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT для таблицы `book_genres`
--
ALTER TABLE `book_genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `book_genres`
--
ALTER TABLE `book_genres`
  ADD CONSTRAINT `fk_book_genres_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_book_genres_genre_id_genres` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`);

--
-- Ограничения внешнего ключа таблицы `covers`
--
ALTER TABLE `covers`
  ADD CONSTRAINT `fk_covers_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `fk_reviews_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_reviews_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
