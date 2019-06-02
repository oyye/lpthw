class Scene(object):
 
    def enter(self):
        print("This scenne is not yet configured")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
 
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current = self.scene_map.opening_scene()
        last = self.scene_map.next_scene('finished')

        while current != last:
            next_name = current.enter()
            current = self.scene_map.next_scene(next_name)

        current.enter()

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class CentralCorridor(Scene):
    def enter(self):
        return 'finished'

class Map(object):

    scenes = {
        'centeral_corridor': CentralCorridor(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

map = Map('central_corridor')
game = Engine(map)
game.play()