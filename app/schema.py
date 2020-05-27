TABLES = {}

TABLES['form'] = (
    "CREATE TABLE `devopstestedb.form` ("
    "  `nome` VARCHAR(100) not NULL,"
    "  `email` VARCHAR(100) not NULL,"
    "  `comentario` VARCHAR(100) not NULL"
    ") ENGINE=InnoDB")