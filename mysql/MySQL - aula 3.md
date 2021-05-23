# MySQL - aula 3

Class: MySQL
Created: May 20, 2021 5:21 PM
Professor: Guanabara
Reviewed: No
Type: Online

- As tabelas dos bancos de dados guardam dados de coisas que possuem características semelhantes;
- Um banco de dados pode ter várias tabelas;
- Os dados dentro das tabelas são chamados de registros;
- Banco de dados ← tabelas ← registros ← campos
- Tipos primitivos:
    1. Numéricos
        1. Inteiro;
            1. TinyInt;
            2. SmallInt;
            3. Int;
            4. MediumInt;
            5. BigInt.
        2. Real;
            1. Decimal;
            2. Float;
            3. Double;
            4. Real.
        3. Lógico
            1. Bit;
            2. Boolean.
    2. Data/Tempo;
        1. Date;
        2. DateTime;
        3. TimeStamp;
        4. Time;
        5. Year.
    3. Literal;
        1. Caractere;
            1. Char;
            2. VarChar.
        2. Texto;
            1. TinyText;
            2. Text;
            3. MediumText;
            4. LongText.
        3. Binário;
            1. TinyBlob;
            2. Blob;
            3. MediumBlob;
            4. LongBlob.
        4. Coleção.
            1. Enum;
            2. Set.
    4. Espacial;
        1. Geometry;
        2. Point;
        3. Polygon;
        4. MultiPolygon.

```sql
create database cadastro;
create table pessoas (
nome varchar(30),
idade tinyint,
sexo char(1),
peso float,
altura float,
nacionalidade varchar(20)
);
```

Primeiro criamos o banco de dados usando o create database e logo em seguida damos o nome ao bando de dados que seria

cadastro e sempre colocando ; no final isso no mysql workbench

create database cadastro;

Após criar o banco de dados, podemos excluir o isso de cima, e já entrão criamos a tabela

Criamos a tabela com o create table e logo em seguida damos o nome a tabela que seria pessoas

seguido do () e ; no final

create table pessoas ();

No Banco de dados tempos os tipos primitivos. Que seria lógica de programação em Banco de dados

Tipos Primitivos:

O tipos primitivos são divididos em família, que são:

Família		Subdivisão das famílias

Numérico:

		Inteiro: TinyInt(esse usa menos dados), SmallInt, Int, Medium, BigInt(esse usa muitos dados)
	
		Real: Decimal, Float, Double, Real
	
		Lógico: Bit, Bolean

Data/Tempo:	Date(DATA), DateTime(DATAS, HORAS OU ALGO A MAIS), TimeStamp(DATAS, HORAS OU ALGO A MAIS), Time}(hora), Year(ano)

Literal: 

		Caractere: Char, VarChar
	
		OBSERVAÇÃO: No Caractere Char é fixo, isso quer dizer que ele não muda,
	
		se você der uma quantidade de caractere Char no banco de dados, por exemplo:
	
		São 30 letras para poder ser preenchidos no nome, se o usuário der apenas 15 letras, o restante é preenchido
	
		com espaço até dar 30 caracteres no bando de dados. Já o VarChar, ele é um variante, ele vai dar até
	
		30 letras, mesmo se o usuário der 15 letras, o restante ficará disponível para ser ocupado e não vai ser
	
		preenchido nem com espaço nem com nada, somente se o usuário acrescentar mais letras.
	
		Texto: TinyText, Text, MediumText, LongText
	
		Binário: TinyBlob, Blob, MediumBlob, LongBlob (o tipo Blob, é possível guardar qualquer coisa em binário)
	
		Coleção: Enum, Set (esses tipos aceita apenas os valores permitidos)

Espacial:		Geometry, Point, Polygon, MultiPolygon (É um tipo que guarda volumétrico)

Logo depois damos os tipos de cada atributo no banco de dados:

create table pessoas (

	nome varchar(30),
	
	idade tinyint(3),
	
	sexo char(1),
	
	peso flaot,
	
	altura float,
	
	nacionalidade varchar(20)

);

Para descrever o que estiver no bando de dados, basta usar o seguinte comando describe + o nome da tabela ; no final,

por exemplo:

create table pessoas (

	nome varchar(30),
	
	idade tinyint(3),
	
	sexo char(1),
	
	peso flaot,
	
	altura float,
	
	nacionalidade varchar(20)

);

describe pessoas;

LEMBRETE: 1.NÃO SE SALVA IDADE EM BANCO DE DADOS, POÍS ELA SEMPRE VARIA COM O TEMPO,

	   NO BANDO DE DADOS NÃO DA PRA MUDAR ISSO SEMPRE

**Show less**