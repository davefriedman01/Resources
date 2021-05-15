# check to see whether there are headers and, if so, what the column names are
cat data/card_holder.csv | head -n2
cat data/credit_card.csv | head -n2
cat data/merchant_category.csv | head -n2
cat data/merchant.csv | head -n2
cat data/transaction.csv | head -n2

#createdb fraud_db -O postgres
psql -d postgres -U postgres -f seed.sql
psql -d fraud_db -U postgres
