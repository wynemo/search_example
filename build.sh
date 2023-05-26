docker build --build-arg http_proxy=$http_proxy -t search_service -f Dockerfile .
docker compose up -d
echo "sleeping for 60s"
sleep 60
docker compose exec search /venv/bin/python /search_example/manage.py migrate
echo "generate csv"
docker compose exec search /venv/bin/python /search_example/csv_generator.py
echo "insert data"
docker compose exec search /venv/bin/python /search_example/manage.py insert_data user_table.csv
