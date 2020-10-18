import unittest, pygame
import consts
from cell import Cell
from snake import Snake
from game_manager import GameManager


class TestPygame(unittest.TestCase):

    def transfer(self, map_ls):

        snake_color_to_id = {}

        for ind, snk in enumerate(self.snakes):
            snake_color_to_id[(*snk.color,)] = str(ind)

        color_to_char = {
            (*consts.back_color,): ".",
            (*consts.fruit_color,): "F",
            (*consts.block_color,): "B",
            **snake_color_to_id
        }

        s = ""
        for ind, cell_color in enumerate(map_ls):
            s += color_to_char[(*cell_color,)]
            if ind % consts.table_size == consts.table_size - 1:
                s += "\n"

        return s

    def get(self, gameManager, snake, events):
        self.screen = pygame.display.set_mode((consts.height, consts.width))
        self.screen.fill(consts.back_color)
        self.game = gameManager(consts.table_size, self.screen, consts.sx, consts.sy, consts.block_cells)
        self.snakes = list()
        for sn in consts.snakes:
            self.snakes.append(
                snake(sn['keys'], self.game, (sn['sx'], sn['sy']), sn['color'], sn['direction']))

        for event in events:
            self.game.handle(event)

        ret = []
        for x in range(consts.table_size):
            for y in range(consts.table_size):
                ret.append(self.game.get_cell((y, x)).color)

        return ret

    def clean(self, s):
        lines = s.split('\n')
        lines = lines[1:-1]
        ret = ""
        for line in lines:
            ret += line.strip()
            ret += "\n"

        return ret

    def test_snake_init(self):
        events = []

        content = self.transfer(self.get(GameManager, Snake, events))
        expected_map = """
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ..........0.........
            ....................
            ....................
            ....................
            ............BBBBB...
            .1..................
            ....................
            ....................
            ....................
            ....................
        """
        self.assertEqual(self.clean(expected_map), content)

    def test_sample_1(self):
        events = ['d', 'l', 'k', 'k', 's', 'w', 'd', 'd', 'j', 'l', 'i', 'l', 'l', 's', 'a', 'k', 'l', 'a', 'a', 'w']

        content = self.transfer(self.get(GameManager, Snake, events))
        expected_map = """
            ....................
            .....1..............
            ....................
            F...................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ........0...........
            ....................
            ............BBBBB...
            ....................
            ....................
            ....................
            ....................
            F...................
        """
        self.assertEqual(self.clean(expected_map), content)

    def test_sample_2(self):
        events = [
            'a', 'l', 's', 'a', 'w', 'd', 'l', 'l', 'i', 'd', 's', 'l', 'j', 'k', 'l', 'k', 'i', 'w', 'j', 'k', 'j',
            'w', 'j', 'l', 'i',
        ]

        content = self.transfer(self.get(GameManager, Snake, events))
        expected_map = """
            F...................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ............0.......
            ............BBBBB...
            .............1......
            ....................
            ....................
            ....................
            F...................
        """
        self.assertEqual(self.clean(expected_map), content)

    def test_sample_3(self):
        events = [
            'k', 's', 'd', 'l', 'j', 'w', 'k', 'i', 'j', 'd', 'k', 'i', 'l', 'l', 'w', 's', 'j', 'l', 'w', 'i', 'i',
            'w', 'w', 'j', 'k',
            's', 'a', 'i', 'k', 'i'
        ]

        content = self.transfer(self.get(GameManager, Snake, events))
        expected_map = """
            ...................F
            ....................
            ....................
            ....................
            ........1...........
            F...................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            ............BBBBB...
            .............0......
            ....................
            ....................
            ....................
            F...................
        """
        self.assertEqual(self.clean(expected_map), content)

    def test_sample_4(self):
        events = [
            'j', 'l', 'l', 'i', 'l', 'l', 'w', 'l', 'k', 'l', 'j', 'w', 's', 'j', 'i', 'a', 's', 'w', 'd', 'k', 'l',
            's', 'w', 'l', 'a',
            'l', 'i', 'd', 'w', 'l', 'j', 'd', 'j', 'k', 's', 'j', 'l', 's', 'l', 's', 'l', 'a', 'd', 'k', 's', 'k',
            's', 'j', 'w', 'i',
            'j', 'i', 'a', 'k', 'j', 'j', 'a', 'd', 'j', 'a', 'i', 'i', 'j', 'j', 'd', 'a', 'j', 'j', 'w', 'k', 'j',
            'a', 'l', 'l', 's',
            'a', 'i', 'd', 'a', 's', 'w', 'w', 'j', 'j', 'a', 'w', 's', 'j', 'j', 'w', 'k', 's', 'i', 'a', 'k', 'w',
            'd', 'd', 'd', 'w',
        ]

        content = self.transfer(self.get(GameManager, Snake, events))
        expected_map = """
            F..................F
            ....................
            .........F..........
            ....................
            ....................
            ...............F....
            ....................
            ....................
            F...................
            ...................1
            ...................1
            ...................0
            ....F..............0
            ....................
            ............BBBBB...
            ....................
            ....................
            .......F............
            ....................
            F...................
        """
        self.assertEqual(self.clean(expected_map), content)