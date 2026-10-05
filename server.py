from mcp.server import Server
import sqlite3

app = Server("1c-metadata")
conn = sqlite3.connect('1c.db', check_same_thread=False)

@app.tool()
def find_object(name: str):
    cur = conn.execute("SELECT * FROM bsl_fts WHERE bsl_fts MATCH ?", (name,))
    return cur.fetchall()

@app.tool()
def find_usage(method: str):
    cur = conn.execute("SELECT module_name FROM bsl_fts WHERE bsl_fts MATCH ?", (method,))
    return cur.fetchall()
