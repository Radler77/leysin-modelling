import unittest

from snowpiercer.world.world import World
from snowpiercer.agents.normie_agent import NormieAgent

class TestWorld(unittest.TestCase):
    
    def test_collect_dead_agents(self):
        world = World()
        agent1 = NormieAgent(0, satiety=1)
        agent2 = NormieAgent(0, satiety=0.2)
        agent3 = NormieAgent(0, satiety=0.5)
        world.agents = [agent1, agent2, agent3]
        world.collect_dead_agents()
        self.assertEqual(len(world.agents), 2)
        self.assertIn(agent1, world.agents)
        self.assertNotIn(agent2, world.agents)
        self.assertIn(agent3, world.agents)