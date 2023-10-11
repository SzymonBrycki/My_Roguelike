from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, BumpAction, EscapeAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler(tcod.event.EventDispatch[Action]):
    '''
    Class that handles events based upon pressing buttons.

    METHODS:

    ev_quit()

    ev_keydown()
    '''
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov() # Update the FOV before the player's next action

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        '''
        Method that exits the game.
        '''
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        '''
        Method that reacts to pressed buttons.
        '''
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key == tcod.event.K_UP:
            action = BumpAction(player, dx= 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(player, dx = 0, dy = 1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(player, dx = -1, dy = 0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(player, dx = 1, dy = 0)

        elif key == tcod.event_K_ESCAPE:
            action = EscapeAction(player)

        # no valid key was pressed

        return action
