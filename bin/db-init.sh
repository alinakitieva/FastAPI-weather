if [ "$(psql -tAc "SELECT 1 FROM pg_database WHERE datname='$DATABASE_NAME'")" = '1' ]; then
  echo "Database already exists"
  exit
else
  echo "Database does not exist"
  psql -U postgres -c "CREATE DATABASE $DATABASE_NAME OWNER $DATABASE_USER;"
fi
