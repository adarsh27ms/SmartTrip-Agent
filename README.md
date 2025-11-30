🧭 SmartTrip — AI Multi-Agent Travel Itinerary Generator
Google × Kaggle Agents Intensive Capstone Project

🚀 Overview

SmartTrip is a modular AI multi-agent system that automatically generates personalized multi-day travel itineraries.
Built as part of the Google × Kaggle AI Agents Intensive, this project demonstrates:

Multi-agent architecture

LLM integration (OpenAI)

Memory and user-state management

Orchestration pipeline

Logging and observability

Clean, production-style code structure

✨ Key Features
🧠 InfoGatherer Agent

Collects POIs (mock data) and uses LLM refinement.

📝 Planner Agent

Constructs day-wise itineraries based on user preferences.

⏱ Scheduler Agent

Adds time blocks and estimated travel durations.

💾 MemoryBank

Stores user preferences + trip history in JSON.

🤖 SmartTrip Orchestrator

Runs the full pipeline end-to-end and returns a structured itinerary.

🏗 Architecture Diagram
                          ┌────────────────────┐
                          │   SmartTripAgent   │
                          │  (Orchestrator)    │
                          └─────────┬──────────┘
                                    │
         ┌───────────────┬──────────┴──────────┬────────────────┐
         │               │                      │                │
┌────────▼──────┐ ┌──────▼───────────┐ ┌────────▼──────┐ ┌───────▼─────────┐
│ InfoGatherer  │ │     Planner      │ │   Scheduler    │ │   MemoryBank    │
│ Collect POIs  │ │ Build itinerary  │ │ Add timings    │ │ Save user data  │
└───────────────┘ └──────────────────┘ └───────────────┘ └──────────────────┘

📦 Project Structure
SmartTrip-Agent/
│
├── smarttrip/
│   ├── agents.py        # InfoGatherer, Planner, Scheduler
│   ├── memory.py        # MemoryBank
│   └── core.py          # SmartTripAgent orchestrator
│
├── SmartTrip.ipynb      # Main demo notebook (Kaggle)
├── README.md
└── requirements.txt

🧪 Example Usage
from smarttrip.core import SmartTripAgent
from openai import OpenAI

client = OpenAI(api_key="your_api_key")
def llm_complete(prompt):
    return client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    ).output_text

agent = SmartTripAgent(llm_complete)

result = agent.build_itinerary(
    user_id="demo_user",
    destination="Paris",
    days=3,
    preferences={"pace": "relaxed", "interests": ["art", "food"]}
)

print(result)

📊 Example Output (Formatted)
Trip for: Paris  
Days: 3  

Day 1:
  • 09:00 – Visit Eiffel Tower  
  • 13:00 – Lunch Break  
  • 15:00 – Explore nearby areas  

Day 2:
  • 09:00 – Visit Louvre Museum  
  • 13:00 – Lunch Break  
  • 15:00 – Explore nearby areas  

🛠 Technologies Used

Python

OpenAI API

Modular multi-agent design

Logging

JSON-based memory

Kaggle Notebook

🔮 Future Improvements

Live Google Search with Tools

Map-based routing & distance estimation

Budget-aware itineraries

Multi-city itineraries

Web UI / API deployment

🏆 Kaggle Submission

SmartTrip was submitted to the Concierge Agents Track of the Google × Kaggle AI Agents Capstone.

👤 Author

Adarsh
Kaggle: adarsh2006ms
GitHub: adarsh27ms
