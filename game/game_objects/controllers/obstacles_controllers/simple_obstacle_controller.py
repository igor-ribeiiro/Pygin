from pygame.math import Vector2
from game_engine.time import Time
from random import randint as rand
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.obstacle_rectangle import Rectangle
from game.scripts.constants import Constants
from game_engine.material import Material
from game.animations.obstacle_pulsing_animation import ObstaclePulsingAnimation
from game_engine.components.animator import Animator

class SimpleObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 300
        self.game_object_list = []


    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        direction = rand(0, 1) < 0.5
        rect = Rectangle(Vector2(direction * 0.5 * Constants.screen_width + 12, - 0.06 * Constants.screen_height),
                         Vector2(0.45 * Constants.screen_width,0.06 * Constants.screen_height),
                         Material((255, 255, 255)))
        rect.animation = ObstaclePulsingAnimation(rect)
        rect.animator = Animator(rect, [rect.animation])
        rect.animator.play()
        self.game_object_list.append(rect)
