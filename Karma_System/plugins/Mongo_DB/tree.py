from Karma_System import MONGO_CLIENT
from datetime import datetime
from random import choice

db = MONGO_CLIENT["Karma"]["Main"]


async def get_data() -> dict:
    data = await db.find_one({"_id": 4})
    return data


async def add_inspector(Karma: int, inspector: int) -> True:
    data = await get_data()
    data["data"][str(Karma)][str(inspector)] = []
    data["standalone"][str(inspector)] = {
        "addedby": Karma,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)


async def add_enforcers(inspector: int, enforcer: int) -> True:
    data = await get_data()
    Karma = data["standalone"][str(inspector)]["addedby"]
    if Karma == 777000:
        s = data["data"][str(inspector)]
        s[list(choice(s.keys()))].append([enforcer])
    else:
        data["data"][str(Karma)][str(inspector)].append([enforcer])
    data["standalone"][str(enforcer)] = {
        "addedby": inspector,
        "timestamp": datetime.timestamp(datetime.now()),
    }
    await db.replace_one(await get_data(), data)
