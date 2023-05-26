#!/usr/bin/env python3
import tcod

import copy

from engine import Engine

import entity_factories

# from game_map import GameMap

from input_handlers import EventHandler

from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    oPlayer = copy.deepcopy(entity_factories.player)

    # oNpc = Entity(int(screen_width /2 -5), int(screen_height /2), "@", (255, 255, 0))

    # entities ={oNpc, oPlayer}

    o_game_map = generate_dungeon(
        max_rooms = max_rooms,
        room_min_size = room_min_size,
        room_max_size = room_max_size,
        map_width = map_width,
        map_height = map_height,
        max_monsters_per_room = max_monsters_per_room,
        player = oPlayer
    )

    oEngine = Engine(event_handler = event_handler, game_map = o_game_map, player = oPlayer)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title="Roguelike Tutorial",
        vsync = True,
    ) as context:

        root_console = tcod.Console(screen_width, screen_height, order="F")

        while True:
            oEngine.render(console = root_console, context = context)

            events = tcod.event.wait()

            oEngine.handle_events(events)

if __name__ == "__main__":
    main()