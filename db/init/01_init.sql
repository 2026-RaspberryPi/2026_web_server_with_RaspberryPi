create database if not exists shopping_db character set utf8mb4 collate utf8mb4_general_ci;

create user if not exists 'bssmMrchoi'@'localhost' identified by '비밀번호';
create user if not exists 'appuser'@'%' identified by '비밀번호';

grant select, insert, update, delete on shopping_db.* to 'appuser'@'%';
flush privileges;
