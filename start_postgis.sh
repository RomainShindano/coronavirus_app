docker run \
--name "covid_app-postgis" \
-p 5433:5433 \
-e -t POSTGRES_USER=test \
-e POSTGRES_PASS=testing321 \
-e POSTGRES_DBNAME=coronavirus_app_db \