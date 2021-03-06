from data.scripts.entities.collision_lists import CollisionLists
import data.scripts.rapid_potato.entities as e
from data.scripts.config import *
from data.scripts.core_funcs import *


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.collisions = CollisionLists()

        e.set_global_colorkey((0, 0, 0))
        e.load_animations2('data/images/animations')
        e.load_particle_images('data/images/particles')

        self.entity_config = {
            'player': {'offset': [-2, -2]},
        }

        self.entities = []

    def reset_entities(self):
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()
