import logging
import json
import random
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def recommend_agents(description):
    """
    Recommend 10-20 random agent IDs based on the input description.
    NOTE: This is a placeholder function. It will be replaced with a real recommender system soon.
    """
    # Load the agent profiles from the JSON file
    with open('agent_profiles.json', 'r') as f:
        agent_profiles = json.load(f)

    # Extract all agent IDs
    agent_ids = [profile['id'] for profile in agent_profiles]

    # Randomly select between 10 to 20 agent IDs
    recommended_agents = random.sample(agent_ids, k=random.randint(10, 20))

    return recommended_agents