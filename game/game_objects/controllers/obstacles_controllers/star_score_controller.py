from pygame.math import Vector2
from game.game_objects.mesh_objects.star import Star
from pygame import mixer
from game_engine.time import Time
from game.scripts.material import Material
from game_engine.game_object import GameObject
from game_engine.color import Color
from random import uniform as randfloat
from game.scripts.constants import Constants

class StarScoreController(GameObject):

    def start(self):
        self.fall_velocity = 250
        self.angular_speed = 0
        self.game_object_list = []
        self.size = Constants.screen_width * 0.03
        self.points_per_start = 100

    def update(self):
        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.fall(self.fall_velocity * Time.delta_time(), self.angular_speed * Time.delta_time())

    def get_star(self):
        self.play_star_collect_sound()
        GameObject.find_by_type("ScoreController")[0].score += self.points_per_start

    def play_star_collect_sound(self):
        mixer.Sound('assets/soundtrack/star_collect.wav').play()

    def generate_obstacle(self):
        random_pos = int(randfloat(self.size / 2 + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.size / 2 + Constants.circCenter_x - Constants.circRadius)))

        star = Star(Vector2(random_pos, -self.size), self.size,
                    Material(Color.yellow))
        self.game_object_list.append(star)
