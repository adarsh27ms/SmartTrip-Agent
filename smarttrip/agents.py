import logging

logger = logging.getLogger("SmartTrip")


class InfoGatherer:
    def __init__(self, llm_complete):
        self.llm_complete = llm_complete

    def run(self, destination, preferences):
        logger.info(f"InfoGatherer: Collecting basic POIs for {destination}")

        # Mock POI list
        pois = [
            {"name": "Eiffel Tower", "desc": "Iconic landmark"},
            {"name": "Louvre Museum", "desc": "World's largest art museum"},
            {"name": "Seine River Cruise", "desc": "Relaxing river experience"},
        ]

        summary_prompt = f"Summarize attractions in {destination}: {pois}"
        summary = self.llm_complete(summary_prompt)

        return {"pois": pois, "summary": summary}


class Planner:
    def __init__(self, llm_complete):
        self.llm_complete = llm_complete

    def run(self, gathered_data, days, preferences):
        logger.info("Planner: Creating itinerary plan")

        pois = gathered_data["pois"]
        plan = []

        for i in range(days):
            poi = pois[i % len(pois)]
            plan.append({
                "day": i+1,
                "activities": [
                    {"time": "09:00", "plan": f"Visit {poi['name']}"},
                    {"time": "13:00", "plan": "Lunch Break"},
                    {"time": "15:00", "plan": "Explore nearby areas"},
                ]
            })

        summary_prompt = f"Write a friendly summary for this itinerary: {plan}"
        summary = self.llm_complete(summary_prompt)

        return {"plan": plan, "summary": summary}


class Scheduler:
    def __init__(self):
        pass

    def run(self, plan_data):
        logger.info("Scheduler: Adding travel times")
        for day in plan_data["plan"]:
            for activity in day["activities"]:
                activity["travel_hours"] = 0.2
        return plan_data
