# блядские хуесосы блять я сделаю этот ебанный ревард юр блять подавсиь сука

# блять если нахуй я открою порт и мне снесёт всё нахуй блять сука заработай блять




# код перплексити мб заработает

from fastapi import FastAPI
app = FastAPI()

@app.get("/reward")
def give_reward(userid: str):  # userid заменится на tg id
    # Здесь дай награду: монеты, XP и т.д.
    print(f"Дал награду юзеру {userid}")
    return {"status": "ok"}  # Просто 200 OK

# Запусти: uvicorn main:app --host 0.0.0.0 --port 443 --reload (нужен HTTPS!)