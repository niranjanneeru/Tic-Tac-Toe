import random

from rich import box
from rich.prompt import Prompt
from rich.table import Table


class State:
    state = [" "] * 9
    opponent = None

    def get_move(self):
        raise NotImplementedError
        pass

    def get_slots(self):
        return [str(i + 1) for i, j in enumerate(self.state) if j == " "]


class MachinePlayer(State):
    def get_move(self):
        return random.choice(self.get_slots())


class PvPlayer(State):
    def get_move(self):
        return Prompt.ask("Enter Slot for O: ",
                          choices=self.get_slots())


class Game(State):
    vsCPU = "vsCPU"
    vsPlayer = "vsPlayer"

    turn = True
    game_var = True

    def __init__(self, console):
        self.console = console
        self.console.rule("[bold red]Tic Tac Toe")
        mode = Prompt.ask("Select Mode: ",
                          choices=[self.vsPlayer, self.vsCPU],
                          default=self.vsCPU)
        self.mode_select(mode)
        self.game_loop()

    def mode_select(self, mode):
        if mode == self.vsCPU:
            self.opponent: State = MachinePlayer()
        elif mode == self.vsPlayer:
            self.opponent: State = PvPlayer()

    def game_loop(self):
        while self.game_var:
            self.display_board()
            self.play()
            self.results(*self.validate())

    def display_board(self):
        state = self.state.copy()

        for i in range(len(state)):
            if state[i] == "X":
                state[i] = "[bold magenta]X"
            elif state[i] == "O":
                state[i] = "[blue]O"

        table = Table(title="Tic Tac Toe",
                      show_lines=True,
                      box=box.HEAVY,
                      border_style="border",
                      title_style="heading")

        for i in range(3):
            table.add_column(state[i])
        for i in range(3, 9, 3):
            table.add_row(state[i], state[i + 1], state[i + 2])

        self.console.print(table)

    def play(self):
        if self.turn:
            move = Prompt.ask("Enter Slot for X: ",
                              choices=self.get_slots())
            self.state[int(move) - 1] = 'X'
        else:
            move = self.opponent.get_move()
            self.state[int(move) - 1] = 'O'
        self.turn = not self.turn

    def validate(self):
        # row check
        for i in range(0, 9, 3):
            if self.state[i] == self.state[i + 1] == self.state[i + 2] == 'X':
                return False, 'X'
            if self.state[i] == self.state[i + 1] == self.state[i + 2] == 'O':
                return False, 'O'

        # col check
        for i in range(3):
            if self.state[i] == self.state[i + 3] == self.state[i + 6] == 'X':
                return False, 'X'
            if self.state[i] == self.state[i + 3] == self.state[i + 6] == 'O':
                return False, 'O'

        # diag check
        if self.state[0] == self.state[4] == self.state[8] == 'X':
            return False, 'X'
        if self.state[0] == self.state[4] == self.state[8] == 'O':
            return False, 'O'
        if self.state[2] == self.state[4] == self.state[6] == 'X':
            return False, 'X'
        if self.state[2] == self.state[4] == self.state[6] == 'O':
            return False, 'O'

        # draw check
        if len(self.get_slots()) == 0:
            return False, None

        return True, None

    def results(self, res, winner):
        print(res)
        if res:  # continue game
            return
        self.game_var = False
        self.display_board()
        if winner:
            if isinstance(self.opponent, MachinePlayer):
                if winner == "X":
                    self.console.print("Victory", style="success")
                else:
                    self.console.print("Lost", style="lost")
            else:
                self.console.print(f"{winner} Won", style="success")
        else:
            self.console.print("Draw", style="draw")
