from data.scripts.entities.collision_lists import CollisionLists
import data.scripts.rapid_potato.entities as e
from data.scripts.config import *
from data.scripts.core_funcs import *


class EntityManager():
    def __init__(self, game):
        self.game = game
        self.collisions = CollisionLists()

        e.set_global_colorkey((0, 0, 0))
        e.load_animations2('data/images/animations')
        e.load_particle_images('data/images/particles')

        self.entity_config = {
            'player': {'offset': [-2, -2]},
        }

        self.items = []

    def reset_entities(self):
        self.items = []

    def spawn_item(self, item_type, location):
        self.items.append(
            {'type': item_type, 'obj': e.PhysicsObj(*location, *ITEM_CONFIG[item_type]), 'velocity': [0, 0],
             'existence': 'drop'})

    # TODO: add item-specific physics parameters
    def update_items(self):
        for item in self.items:
            item['velocity'][1] = min(item['velocity'][1] + 0.1, 1.5)
            item['velocity'][0] = normalize(item['velocity'][0], 0.04)
            item_collisions = item['obj'].move(item['velocity'],
                                               self.game.entities.collisions.collision_tiles,
                                               self.game.entities.collisions.collision_ramps,
                                               self.game.entities.collisions.collision_platforms)
            if item_collisions['right'] or item_collisions['left']:
                item['velocity'][0] *= -0.7
            self.game.window.display.blit(self.game.assets.item_images[item['type']],
                                          (item['obj'].x - self.game.level.scroll[0],
                                           item['obj'].y - self.game.level.scroll[1]))

    def update(self):
        self.update_items()
