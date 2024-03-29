create table PUBLISHER
(
	publisher_id integer primary key,
	org_name varchar(128) not null,
	address text not null
);
create table BOOK
(
	book_id int4 primary key,
	title varchar(512) not NULL,
	ISBN varchar(32) not NULL,
	fk_book_publisher integer REFERENCES publisher(publisher_id) ON DELETE CASCADE NOT NULL
);
	
insert into book 
values
(1, 'Серебряные глаза', '978-5-699-99773-2', 1),
(2, 'Гарри Поттер и Принц-полукровка', '5-353-02187-8', 2),
(3,'Гравити Фолз. Дневник 3', '978-5-699-90656-7', 3),
(4, 'Четвёртый шкаф', ' 978-5-04-097360-6 ', 1),
(5,'Тарас бульба', ' 978-5-17-151222-4 ',4)
;
insert into publisher
values
(1,'Эксмо','123308, город Москва, улица Зорге, дом 1, строение 1, этаж 20, каб 2013'),
(2,'Росмэн','Москва, Ленинградский проспект, д. 36, стр. 11, м. Динамо.'),
(3,'Эксмодетство','123308, город Москва, улица Зорге, дом 1, строение 1'),
(4,'АСТ','г. Москва, Пресненская наб., д.6, стр.2, БЦ «Империя»')
;

DROP TABLE book;
DROP TABLE publisher;

SELECT * FROM book;