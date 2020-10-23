import data.scripts.rapid_potato.entities as e


class GameEntity(e.Entity):
    def __init__(self, game, entities, e_type, x, y, x_size, y_size):
        super().__init__(x, y, x_size, y_size, e_type)
        self.game = game
        self.entities_ptr = entities
        self.velocity = [0, 0]
        self.grav_accel = 0.55
        self.jump_force = 8.5
        self.jump_max = 2
        self.jumps = self.jump_max
        self.speed = 3
        self.air_time = 0
        self.drop_through = 0
        self.in_water = False
        self.game.entities.entities.append(self)

    def process_collisions(self, movement):
        return self.move(movement, self.game.entities.collisions.collision_tiles,
                         self.game.entities.collisions.collision_ramps,
                         self.game.entities.collisions.collision_platforms)

    def mouse_is_on(self):
        if self.get_rect().collidepoint(self.game.input.mouse_pos):
            return True
        return False
