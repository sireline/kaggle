class User:
    ddl = {
        'table_name': 'users',
        'cols': [
            {'name': 'id', 'type': 'INT UNSIGNED', 'null': True, 'auto_increment': True},
            {'name': 'name', 'type': 'VARCHAR(255)', 'null': True},
            {'name': 'age', 'type': 'TINYINT UNSIGNED', 'null': True},
            {'name': 'gender', 'type': 'VARCHAR(10)'}
        ],
        'index': ['id']
    }

    def create():
        stmt = []
        stmt.append('CREATE TABLE ' + User.ddl.table_name + ' (')
        for col in User.ddl.cols:
            stmt += col.name + ' ' + col.type
            stmt += ' NOT NULL' if col.null
            stmt += ' AUTO_INCREMENT' if col.auto_increment
            stmt += ','
        return stmt
