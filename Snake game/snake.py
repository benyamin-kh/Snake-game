import consts


class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys  # dict
        self.cells = [pos]  # it is a list that every cell of this list is tuple
        self.game = game
        print('in mar constractor')
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        print('self.direction is {}'.format(self.direction))
        dx = self.dx[self.direction]
        dy = self.dy[self.direction]
        x, y = self.get_head()
        x += dx
        y += dy
        x = self.val(x)
        y = self.val(y)
        next_pos = (x, y)
        print('khane badi dar location {} mibashad '.format(next_pos))
        if self.game.get_cell(next_pos).color != consts.back_color and self.game.get_cell(
                next_pos).color != consts.fruit_color:
            print('dar tabe next_move hastam mar koshte shod')
            self.game.kill(self)

        elif self.game.get_cell(next_pos).color == consts.fruit_color:
            print('dar tabe next_move hastam mar ghaza khord')
            self.cells.append(next_pos)
            self.game.get_cell(next_pos).set_color(self.color)

        else:
            print('dar tabe next_move hastam mar adie')

            remove_cell = self.game.get_cell(self.cells.pop(0))
            remove_cell.set_color(consts.back_color)
            self.cells.append(next_pos)
            self.game.get_cell(next_pos).set_color(self.color)

    def handle(self, keys):
        print('dar mar handle : ', keys)
        print('klid haye mar :', self.keys)
        for key in keys:

            if key in self.keys:
                if self.direction == self.keys[self.opposite_side(key)]:
                    continue
                else:

                    self.direction = self.keys[key]
                    print(self.direction)
                    break

    def opposite_side(self, key):
        if self.keys[key] == "UP":
            for t in self.keys:
                if self.keys[t] == 'DOWN':
                    return t
        if self.keys[key] == "DOWN":
            for t in self.keys:
                if self.keys[t] == 'UP':
                    return t

        if self.keys[key] == 'RIGHT':
            for t in self.keys:
                if self.keys[t] == 'LEFT':
                    return t

        if self.keys[key] == 'LEFT':
            for t in self.keys:
                if self.keys[t] == 'RIGHT':
                    return t
