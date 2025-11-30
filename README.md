📌 SmartTrip — AI Multi-Agent Travel Itinerary Generator

This project was built as part of the Google × Kaggle Agents Intensive Capstone Project.
SmartTrip is a multi-agent system that automatically builds personalized travel itineraries.

🚀 Features

🧠 InfoGatherer Agent — fetches attractions & summaries

📝 Planner Agent — creates day-by-day itinerary

⏱ Scheduler Agent — adds timing & travel estimates

💾 MemoryBank — stores user preferences & past trips

🤖 LLM Integration — uses OpenAI (fallback safe)

📦 Fully modular & extensible design

📂 Project Architecture
User → SmartTripAgent → InfoGatherer → Planner → Scheduler → Itinerary
           ↓
       MemoryBank

🧪 Example Usage
agent = SmartTripAgent()

trip = agent.build_itinerary(
    user_id="demo_user",
    destination="Paris",
    days=3,
    preferences={"pace": "relaxed", "interests": ["art", "food"]}
)

print(trip)

🛠 Technologies Used

Python

OpenAI API (gpt-4o-mini)

Kaggle Notebook

JSON Memory System

Logging & modular architecture

🏆 Kaggle Submission

This repository is linked to the official kaggle writeup:
SmartTrip — Personal Travel Itinerary Agent (Concierge Track)

📌 Future Improvements

Real-time Google Search tool

POI ranking agent

Budget-based planning

Cloud deployment endpoint

✔ Part of Google × Kaggle Agents Intensive Capstone
