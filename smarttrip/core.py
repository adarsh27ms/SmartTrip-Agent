import time
import logging

from .agents import InfoGatherer, Planner, Scheduler
from .memory import MemoryBank

logger = logging.getLogger("SmartTrip")


class SmartTripAgent:
    def __init__(self, llm_complete):
        self.llm_complete = llm_complete
        self.info = InfoGatherer(llm_complete)
        self.planner = Planner(llm_complete)
        self.scheduler = Scheduler()
        self.memory = MemoryBank()

    def build_itinerary(self, user_id, destination, days=3, preferences=None):
        logger.info(f"SmartTripAgent: Building itinerary for {destination}")

        # Load existing user memory
        user_data = self.memory.get_user(user_id)

        # Update preferences
        if preferences:
            user_data["preferences"].update(preferences)
            self.memory.update_user(user_id, user_data)

        # Step 1 — Gather POIs
        gathered = self.info.run(destination, user_data["preferences"])

        # Step 2 — Build itinerary plan
        plan = self.planner.run(gathered, days, user_data["preferences"])

        # Step 3 — Add travel timing
        scheduled = self.scheduler.run(plan)

        # Store the trip
        trip_record = {
            "destination": destination,
            "days": days,
            "preferences": user_data["preferences"],
            "itinerary": scheduled,
            "timestamp": time.time()
        }

        self.memory.add_trip(user_id, trip_record)

        return trip_record
