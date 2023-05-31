from typing import Optional

import tcod.event

from actions import Action, BumpAction, EscapeAction

class EventHandler(tcod.event.EventDispatch[Action]):
    '''
    Class that handles events based upon pressing buttons.

    METHODS:

    ev_quit()

    ev_keydown()
    '''
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

        if key == tcod.event.K_UP:
            action = BumpAction(dx= 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx = 0, dy = 1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx = -1, dy = 0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx = 1, dy = 0)

        elif key == tcod.event_K_ESCAPE:
            action = EscapeAction()

        # no valid key was pressed

        return action
