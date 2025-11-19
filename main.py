import redis

db = redis.Redis(
    host = "localhost",
    port = 6379,
    db = 0,
    decode_responses = True
)

db.set("Aluno", "Luis")

valor = db.get("Aluno")

print("Valor armazenado: ", valor)