import os
import json
import time
import logging

logger = logging.getLogger("SmartTrip")


class MemoryBank:
    def __init__(self, path="memory_bank.json"):
        self.path = path
        self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.store = json.load(f)
        else:
            self.store = {"users": {}}
            self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.store, f, indent=2)

    def get_user(self, user_id):
        return self.store["users"].get(user_id, {
            "preferences": {},
            "trips": []
        })

    def update_user(self, user_id, data):
        logger.info(f"Updating user memory for: {user_id}")
        self.store["users"][user_id] = data
        self.save()

    def add_trip(self, user_id, trip_record):
        user = self.get_user(user_id)
        user["trips"].append(trip_record)
        self.update_user(user_id, user)
