--
-- initialization
--

-- dropdb fraud_db on the command line
--drop database if exists fraud_db;

drop table if exists card_holder cascade;
drop table if exists credit_card cascade;
drop table if exists merchant_category cascade;
drop table if exists merchant cascade;
drop table if exists transaction cascade;

drop view if exists transactions_per_card_holder;
drop view if exists micro_transactions;
drop view if exists count_micro_transactions;
drop view if exists micro_transactions_morning;
drop view if exists count_micro_transactions_morning;
drop view if exists top_hacked_merchants_micro_transactions;

-- createdb fraud_db -O postgres on the command line
create database fraud_db owner postgres;
\c fraud_db;

--
-- tables
--

create table if not exists card_holder (
  id int not null,
  name varchar(50),
  primary key (id)
);

create table if not exists credit_card (
  card varchar(20) not null,
  id_card_holder int,
  foreign key (id_card_holder) references card_holder (id),
  primary key (card)
);

create table if not exists merchant_category (
  id int not null,
  name varchar(20),
  primary key (id)
);

create table if not exists merchant (
  id int not null,
  name varchar(50),
  id_merchant_category int not null,
  foreign key (id_merchant_category) references merchant_category (id),
  primary key (id)
);

create table if not exists transaction (
  id int not null,
  date timestamp not null,
  amount float,
  card varchar(20),
  id_merchant int,
  foreign key (card) references credit_card (card),
  foreign key (id_merchant) references merchant (id),
  primary key (id)
);

--
-- data import
--

\copy card_holder (id, name) from 'data/card_holder.csv' csv header;
\copy credit_card (card, id_card_holder) from 'data/credit_card.csv' csv header;
\copy merchant_category (id, name) from 'data/merchant_category.csv' csv header;
\copy merchant (id, name, id_merchant_category) from 'data/merchant.csv' csv header;
\copy transaction (id, date, amount, card, id_merchant) from 'data/transaction.csv' csv header;

--
-- views
--

-- transactions, ordered by card holder
create view transactions_per_card_holder as
select ch.name, cc.card, t.date, t.amount, m.name as merchant, mc.name as category
from transaction as t
join credit_card as cc on cc.card = t.card
join card_holder as ch on ch.id = cc.id_card_holder
join merchant as m on m.id = t.id_merchant
join merchant_category as mc on mc.id = m.id_merchant_category
order by ch.name;

-- transactions less than $2.00
create view micro_transactions as
select *
from transaction as t
where t.amount < 2
order by t.card, t.amount desc;

-- the number of transactions that are less than $2.00
create view count_micro_transactions as
select count(t.amount) as "Transactions less than $2.00"
from transaction as t
where t.amount < 2;

-- top 100 transactions between 07:00 and 09:00
create view micro_transactions_morning as
select *
from transaction as t
where date_part('hour', t.date) >= 7 and date_part('hour', t.date) <= 9
order by amount desc
limit 100;

-- the number of transactions less than $2.00 between 07:00 and 09:00
create view count_micro_transactions_morning as
select count(t.amount) as "Transactions less than $2.00 between 07:00 and 09:00"
from transaction as t
where t.amount < 2 and date_part('hour', t.date) >= 7 and date_part('hour', t.date) <= 9;

-- top 5 merchants prone to being hacked using small transactions
create view top_hacked_merchants_micro_transactions as
select m.name as merchant, mc.name as category, count(t.amount) as micro_transactions
from transaction as t
join merchant as m on m.id = t.id_merchant
join merchant_category as mc on mc.id = m.id_merchant_category
where t.amount < 2
group by m.name, mc.name
order by micro_transactions desc
limit 5;
