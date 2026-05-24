import psycopg2
import os


def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=5432
    )


# ───────────── CREAR TABLA ─────────────
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS imagenes (
            id SERIAL PRIMARY KEY,
            usuario VARCHAR(100) NOT NULL,
            s3_key TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT NOW()
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


# ───────────── INSERTAR IMAGEN ─────────────
def insert_image(usuario: str, s3_key: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO imagenes (usuario, s3_key)
        VALUES (%s, %s)
        RETURNING id, fecha
    """, (usuario, s3_key))

    result = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()

    return result


# ───────────── OBTENER IMAGEN ─────────────
def get_image(usuario: str, nombre_imagen: str):
    conn = get_connection()
    cur = conn.cursor()

    s3_key = f"{usuario}/{nombre_imagen}"

    cur.execute("""
        SELECT id, usuario, s3_key, fecha
        FROM imagenes
        WHERE usuario = %s AND s3_key = %s
    """, (usuario, s3_key))

    row = cur.fetchone()

    cur.close()
    conn.close()

    return row