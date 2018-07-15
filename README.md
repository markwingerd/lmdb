# lmdb
Local music database

# Requirements
- Django version 1.11.8
- MySql

# Setup

Setup MySql Database
```
mysql -u root -p
CREATE DATABASE {database name};
GRANT ALL PRIVILEGES ON *.* TO '{username}'@'localhost' IDENTIFIED BY '{password}';
```

Add environment variables
```
LMDB_DB_NAME={database_name}
LMDB_DB_USER={username}
LMDB_DB_PASS={password}
LMDB_SECRET_KEY={random_string}
export LMDB_DB_NAME
export LMDB_DB_USER
export LMDB_DB_PASS
export LMDB_SECRET_KEY
```

Run migrations on Django
```
python manage.py migrate
```
