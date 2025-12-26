from google.adk.agents import Agent

# -------------------------
# PLANNER AGENT
# -------------------------
planner_agent = Agent(
    name="planner_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a trip planner agent.\n"
        "The user will provide a trip location in India.\n"
        "Your task is to break the trip planning into clear, ordered steps.\n"
        "Do NOT execute the steps.\n"
        "Only return a numbered step-by-step plan.\n\n"
        "Steps should typically include:\n"
        "1. Identify major attractions\n"
        "2. Create a day-wise itinerary\n"
        "3. Suggest food and local experiences\n"
        "4. Provide travel and safety tips"
    )
)

# -------------------------
# EXECUTOR AGENT
# -------------------------
executor_agent = Agent(
    name="executor_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are a trip execution agent.\n"
        "You receive a step-by-step trip plan.\n"
        "Execute each step sequentially and provide detailed, practical information.\n"
        "Ensure the trip plan is suitable for travel within India.\n"
        "Present the final output clearly for the user."
    )
)

# -------------------------
# ROOT AGENT (ENTRY POINT)
# -------------------------
root_agent = planner_agent
