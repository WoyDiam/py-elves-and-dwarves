from abc import ABC

from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        nk = self.nickname
        mi = self._musical_instrument
        print(f"{nk} is playing a song on the {mi}")
