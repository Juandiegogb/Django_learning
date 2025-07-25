import psycopg2
from dotenv import load_dotenv
from os import makedirs
from os.path import join, exists
import csv

load_dotenv()

conn = psycopg2.connect("postgresql://postgres:Admin@localhost:5400/legacy_db")
cursor = conn.cursor()
cursor.execute("delete from test.new_rules;")
conn.commit()

query = """
    SELECT f.id, f.RULE , split_part(e.NAME,'.',1) as schema , lower(f.RETURN_DATATYPE) as event
    FROM SYST.FIELDRULEGLOBAL F
    inner join SYST.ENTITYCATAL E on F.ENTITYCATAL_ID = E.ID;
"""

cursor.execute(query)
rows = cursor.fetchall()


with open("field_names.csv", "r", encoding="utf-8") as file:
    names = list(csv.reader(file, delimiter=","))  # ← ✅ Lista en memoria

for id, rule, schema, event in rows:
    for old_name, new_name in names:
        if new_name:
            rule = rule.replace(old_name, new_name)

    file_path = f"rules/{schema}/{event}"
    file_name = f"{id}.js"
    if not exists(file_path):
        makedirs(file_path)
    with open(join(file_path, file_name), "w", encoding="utf-8") as file_rules:
        file_rules.write(rule)

    cursor.execute("INSERT INTO test.new_rules(id, rule) VALUES (%s, %s);", (id, rule))


conn.commit()
cursor.close()
conn.close()
