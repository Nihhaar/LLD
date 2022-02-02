db = {}


def add_entry(table, item):
    if table in db:
        db[table].append(item)
    else:
        db[table] = [item]


def get_entry(table):
    if table in db:
        return db[table]
    else:
        return []
