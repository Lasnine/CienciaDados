create database prova1;

use prova1;

create table cadastro(
	id int auto_increment primary key,
	nome varchar(255) not null,
	email varchar(255) not null,
	telefone varchar(255) not null
);

SELECT * FROM cadastro