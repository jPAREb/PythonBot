import psycopg2
from postgres.p_dades import postgres_credencials


conn = psycopg2.connect(
    host= postgres_credencials.ip,
    database=postgres_credencials.base_dades,
    user=postgres_credencials.usuari,
    password=postgres_credencials.contra)