use projeto_ouvidoria;

create table Manifestacoes(
	codigo int auto_increment,
    manifestacao varchar(120),
	primary key (codigo)
);

insert into Manifestacoes (manifestacao)
	values('Falta de pagamento');

insert into Manifestacoes (manifestacao)
	values('Demissões em massa');

select * from Manifestacoes;
