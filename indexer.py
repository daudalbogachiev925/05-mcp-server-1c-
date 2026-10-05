import sqlite3, re

def index_module(conn, module_name, code):
    for m in re.finditer(r'Процедура\s+(\w+)\s*\(([^)]*)\)', code):
        conn.execute("INSERT INTO procedures (module_name, procedure_name, signature) VALUES (?,?,?)",
                     (module_name, m.group(1), m.group(2)))
    conn.execute("INSERT INTO bsl_fts (module_name, body) VALUES (?,?)", (module_name, code))
