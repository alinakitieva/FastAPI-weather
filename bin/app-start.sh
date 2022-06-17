set -e

cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -d "$DATABASE_NAME" -c '\q'; do
  echo >&2 "Wait Postgres..."
  sleep 1
done

echo >&2 "Postgres is up - continue"
exec $cmd


echo "Running app..."
uvicorn app.main:app --host 0.0.0.0 --port 80
