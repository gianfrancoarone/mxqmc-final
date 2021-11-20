class SpriteKindLegacy(Enum):
    Player = 0
    Projectile = 1
    Food = 2
    Enemy = 3
class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
    Walking_right = 3
    Walking_left = 4
    Idle_right = 5
    Idle_left = 6
def setLevel(num: number, mySprite: Sprite):
    global myTile, facingRight
    scene.set_background_color(15)
    scene.set_tile(14,
        img("""
            . . . . . f . . . . . . . . . . 
                    . . . . . f 3 3 . . 1 1 . . . . 
                    . . . . . f 3 3 . . 1 . 1 . . . 
                    . . . . . f 4 4 4 4 1 . . 1 . . 
                    . d d d d d d d d d d d d d d . 
                    . . e e e e e e e e e e e e . . 
                    . . e . e f 6 6 6 . . e . e . . 
                    . . e . e . f 6 6 . . e . e . . 
                    . . e . e . . . f d . e . e . . 
                    . . e . e . . f . f . e . e . . 
                    . . e . e . f . . . f e . e . . 
                    . . e . f . . . . . . f . e . . 
                    . . e . . . . . . . . . . e . . 
                    . . e . . . . . . . . . . e . . 
                    . . e . . . . . . . . . . e . . 
                    . . f . . . . . . . . . . f . .
        """),
        True)
    scene.set_tile(7,
        img("""
            . . . . . . . . . . . . . . . . 
                    e e e e e e e e e e e e e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d c c c d b d c c c d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d c c c d b d c c c d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d c c c f b f c c c d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d d d d d b d d d d d e . . . 
                    e d b b b d b d b b b d e . . . 
                    e d b b b d b d b b b d e . . . 
                    e d b b b d b d b b b d e . . .
        """),
        False)
    scene.set_tile(5,
        img("""
            . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . 1 6 6 6 6 1 . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . . . 1 1 . . . . . . . 
                    . e e e e e e e e e e e e e e . 
                    . . f f f f f f f f f f f f . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . e . e . . . . . . e . e . . 
                    . . f . f . . . . . . f . f . .
        """),
        False)
    scene.set_tile(2,
        img("""
            d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b d e 
                    d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e d b b b b b b e
        """),
        True)
    scene.set_tile(3,
        img("""
            2 2 5 4 2 2 2 2 5 2 2 2 4 2 2 2 
                    2 2 2 2 2 2 4 2 2 2 2 5 5 2 5 2 
                    4 2 2 2 5 5 2 2 4 5 2 5 5 2 2 2 
                    5 2 2 2 5 5 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 5 2 2 2 2 2 2 2 2 
                    2 2 4 2 2 2 2 2 2 2 2 2 2 2 4 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 4 2 2 2 4 4 2 2 2 2 
                    2 2 2 4 4 2 2 2 2 2 4 4 2 5 5 2 
                    2 2 2 4 4 2 2 2 5 2 2 2 2 5 5 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 5 2 2 4 2 2 2 2 2 2 2 2 2 4 2 
                    2 2 2 2 2 2 2 5 2 2 2 2 2 2 2 2 
                    2 2 2 2 4 2 2 2 2 2 2 2 5 2 2 2 
                    2 2 2 5 2 2 2 2 2 2 4 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        True)
    scene.set_tile(8,
        img("""
            d 1 1 1 1 b 1 1 1 1 1 1 1 1 1 b 
                    1 d d d d d b d d d d d d d d b 
                    1 d d d d d b d d d d d d d d b 
                    1 d d d d d d b d d d d d d d b 
                    1 d d d d d d b d d d d d d d b 
                    1 d d d d d d b d d d d d d d b 
                    1 d d d d d d d b d d d d d d b 
                    1 d d d d d d d d b d d d d d b 
                    1 d d d d d d d d b d d d d d b 
                    1 d d d d d d d b 1 b b d d d b 
                    1 d d d d d d d b 1 d d b b d b 
                    1 d d d d d d b 1 d d d d d b b 
                    1 d d d d d b b 1 d d d d d d b 
                    1 d d d d d b 1 d d d d d d d b 
                    1 d d d d b b 1 d d d d d d d b 
                    b b b b b b b b b b b b b b b b
        """),
        True)
    scene.set_tile(9,
        img("""
            d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e b b b b b b d e 
                    d 1 1 1 1 1 1 b d 1 1 1 1 1 1 b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d b 1 d d d d d d b 
                    1 d d d d d d d 1 d d d d d d d 
                    b b b b b b d e d b b b b b b e
        """),
        True)
    scene.set_tile(15,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . 5 3 3 5 . . . . . . 
                    . . . . . . 5 3 3 5 . . . . . . 
                    . . . . . . 5 3 3 5 . . . . . . 
                    d d d d d d d e e e . . . . . . 
                    d b b b b b d e e e . . . . . . 
                    d b b b b b d e e e . 9 . . . . 
                    d d d f d d d e e 3 . 1 . . . . 
                    . . d f . . 4 4 4 4 . 1 . . . . 
                    b b b b b b b b b b b b b b b . 
                    6 6 6 6 b . f e e f . . 6 6 b . 
                    6 6 6 6 b . f e e f . . 6 6 b . 
                    6 6 6 6 b . f f f f . . 6 6 b . 
                    6 6 6 6 b . . f f . . . 6 6 b . 
                    6 6 6 6 b . f . . f . . 6 6 b .
        """),
        True)
    scene.set_tile(1,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . b d b . . . . . . 
                    . . . . . . . b d b c . . . . . 
                    . . . . b b c 5 5 5 c b b . . . 
                    . . . . b 5 5 5 1 5 5 5 b . . . 
                    . . . c c 5 5 5 1 5 5 5 c c . . 
                    . . b b 5 5 5 1 1 1 5 5 5 b b . 
                    . . d d 5 1 1 1 1 1 1 1 5 d d . 
                    . . b b 5 5 5 1 1 1 5 5 5 b b . 
                    . . . c c 5 5 5 1 5 5 5 c c . . 
                    . . . . b 5 5 5 1 5 5 5 b . . . 
                    . . . . b b c 5 5 5 c b b . . . 
                    . . . . . . c b d b c . . . . . 
                    . . . . . . . b d b . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        True)
    scene.set_tile(10,
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        False)
    scene.set_tile(13,
        img("""
            . . . . . . f f f f . . . . . . 
                    . . . . . . f f f f . . . . . . 
                    . . . . . . f e e f . . . . . . 
                    . . . . . . f e e f . . . . . . 
                    . . . . . . . e e . . . . . . . 
                    d d d d d d d 8 8 8 . . . . . . 
                    d b b b b b d 8 8 8 . . . . . . 
                    d b b b b b d 8 8 8 . . . . . . 
                    d d d f d d d 8 8 e . . . . . . 
                    . . d f . . 9 9 9 9 . . . . . . 
                    b b b b b b b b b b b b b b b . 
                    6 6 6 6 b . f 8 8 f . . 6 6 b . 
                    6 6 6 6 b . f 8 8 f . . 6 6 b . 
                    6 6 6 6 b . f f f f . . 6 6 b . 
                    6 6 6 6 b . . f f . . . 6 6 b . 
                    6 6 6 6 b . f . . f . . 6 6 b .
        """),
        True)
    if num == 0:
        scene.set_tile_map(img("""
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
                        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                        e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e
        """))
    elif num == 1:
        scene.set_background_image(assets.image("""
            office1
        """))
        scene.set_tile(2,
            img("""
                . . . . . . f f f . . . . . . . 
                            . . . . . . . f . . . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . f f d d d f f . . . . . 
                            . . . . f d d d d d f . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . f c f f f f f c f . . . . 
                            . . f . c c f f f c c . f . . . 
                            . . f . b c d d d c b . f . . . 
                            . . . . . b f f f b . . . . . . 
                            . . . . . . b f b . . . . . . . 
                            . . . . . . . f . . . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . f . . . . . f . . . . .
            """),
            True)
        scene.set_tile(3,
            img("""
                . . . . . . . . . . . . . . . . 
                            . b f f f f f f f f f f f f f . 
                            . b f c c c c c c c c c c c f . 
                            . b f c 6 6 6 6 6 6 6 6 c c f . 
                            . b f c 1 1 1 1 1 1 1 1 c c f . 
                            . b f c 1 9 1 9 1 9 1 1 c c f . 
                            . b f c 1 1 1 1 1 1 1 1 c c f . 
                            . b f c 1 9 1 9 1 1 1 1 c c f . 
                            . b f f f f f f f f f f f f f . 
                            . b d d d d d d d d d d d d d . 
                            . b d d d d d d f d d d d d d . 
                            . b d d d d d d d d d d d d d . 
                            . . . . . . b b b b b . . . . . 
                            . . . . . . b d d d d . . . . . 
                            . . . . . . b b d d d d d . . . 
                            . . . . . . . . . . . . . . . .
            """),
            True)
        scene.set_tile(1,
            img("""
                . . . . . . . . . . . . . . . . 
                            . . . b b b b b b b b b b c . . 
                            . . . d d d d d d d d d b c . . 
                            . . . d b b c d b b c d b c . . 
                            . . . d b 6 c d b 6 c d b c . . 
                            . . . d b 6 c d b 6 c d b c . . 
                            . . . d b 9 c d b 9 c d b c . . 
                            . . . d c c c d c c c d b c . . 
                            . . . f d d d d d d d d b c . . 
                            . . . f f f d d d d d d b c . . 
                            . . . d d d d d d d d d b c . . 
                            . . . d b b b b b b c d b c . . 
                            . . . d b b b b b b c d b c . . 
                            . . . d c c c c c c c d b c . . 
                            . . . d d d d d d d d d b c . . 
                            . . . c c c c c c c c c c c . .
            """),
            True)
        myTile = scene.get_tile(0, 5)
        myTile.place(mySprite)
        effects.bubbles.start_screen_effect()
        scene.set_tile_map(img("""
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        5 . . . . . . . . . . . . . . . . . . 7 . . . . . . . . . . . . 
                        8 8 8 8 8 8 8 . 8 8 8 8 8 8 8 . 8 8 8 8 8 8 8 . . . . . . . . 1 
                        8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8
        """))
        myTile = scene.get_tile(0, 3)
        myTile.place(mySprite)
        effects.bubbles.start_screen_effect()
    elif num == 2:
        scene.set_background_image(assets.image("""
            office2
        """))
        scene.set_tile(2,
            img("""
                . . . . . . f f f . . . . . . . 
                            . . . . . . . f . . . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . f f d d d f f . . . . . 
                            . . . . f d d d d d f . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . f c f f f f f c f . . . . 
                            . . f . c c f f f c c . f . . . 
                            . . f . b c d d d c b . f . . . 
                            . . . . . b f f f b . . . . . . 
                            . . . . . . b f b . . . . . . . 
                            . . . . . . . f . . . . . . . . 
                            . . . . . f f f f f . . . . . . 
                            . . . . f . . . . . f . . . . .
            """),
            True)
        scene.set_tile(1,
            img("""
                . . . . . . . . . . . . . . . . 
                            . . . b b b b b b b b b b c . . 
                            . . . d d d d d d d d d b c . . 
                            . . . d b b c d b b c d b c . . 
                            . . . d b 6 c d b 6 c d b c . . 
                            . . . d b 6 c d b 6 c d b c . . 
                            . . . d b 9 c d b 9 c d b c . . 
                            . . . d c c c d c c c d b c . . 
                            . . f d d d d d d d d d b c . . 
                            . . f f f d d d d d d d b c . . 
                            . . . d d d d d d d d d b c . . 
                            . . . d b b b b b b c d b c . . 
                            . . . d b b b b b b c d b c . . 
                            . . . d c c c c c c c d b c . . 
                            . . . d d d d d d d d d b c . . 
                            . . . c c c c c c c c c c c . .
            """),
            True)
        scene.set_tile(3,
            img("""
                . . . . . . . . . . . . . . . . 
                            . b f f f f f f f f f f f f f . 
                            . b f c c c c c c c c c c c f . 
                            . b f c 6 6 6 6 6 6 6 6 c c f . 
                            . b f c 1 1 1 1 1 1 1 1 c c f . 
                            . b f c 1 9 1 9 1 9 1 1 c c f . 
                            . b f c 1 1 1 1 1 1 1 1 c c f . 
                            . b f c 1 9 1 9 1 1 1 1 c c f . 
                            . b f f f f f f f f f f f f f . 
                            . b d d d d d d d d d d d d d . 
                            . b d d d d d d f d d d d d d . 
                            . b d d d d d d d d d d d d d . 
                            . . . . . . b b b b b . . . . . 
                            . . . . . . b d d d d . . . . . 
                            . . . . . . b b d d d d d . . . 
                            . . . . . . . . . . . . . . . .
            """),
            True)
        scene.set_tile_map(img("""
            ................
                        ................
                        .1..............
                        .8..............
                        ................
                        ...d2f..........
                        ...999..........
                        ......88........
                        ........888.....
                        ................
                        ...........99...
                        ................
                        .........99.....
                        ................
                        ......99........
                        ................
                        ...99...........
                        ................
                        99..............
                        ....d2..........
                        ...9999.........
                        ................
                        ........9999....
                        ................
                        .............99.
                        .........f2.....
                        ........9999....
                        ........88883333
                        .....99.88888888
                        ........88888888
                        9999....88888888
                        8888333388888888
        """))
        myTile = scene.get_tile(0, 29)
        myTile.place(mySprite)
        effects.bubbles.start_screen_effect()
    elif num == 3:
        scene.set_background_image(assets.image("""
            office3
        """))
        scene.set_tile(3,
            img("""
                . . . . . . . . . . . . . . . . 
                            . b f f f f f f f f f f f f f . 
                            . b f c c c c c c c c c c c f . 
                            . b f c 6 6 6 6 6 6 6 6 c c f . 
                            . b f c 1 1 1 1 1 1 1 1 c c f . 
                            . b f c 1 9 1 9 1 9 1 1 c c f . 
                            . b f c 1 1 1 1 1 1 1 1 c c f . 
                            . b f c 1 9 1 9 1 1 1 1 c c f . 
                            . b f f f f f f f f f f f f f . 
                            . b d d d d d d d d d d d d d . 
                            . b d d d d d d f d d d d d d . 
                            . b d d d d d d d d d d d d d . 
                            . . . . . . b b b b b . . . . . 
                            . . . . . . b d d d d . . . . . 
                            . . . . . . b b d d d d d . . . 
                            . . . . . . . . . . . . . . . .
            """),
            True)
        scene.set_tile_map(img("""
            ................................
                        ................................
                        ................................
                        ................................
                        ................................
                        ................................
                        ..........................eeee..
                        .............99.........999999..
                        ................................
                        ...........9....9..9..9.........
                        ................................
                        .........9......................
                        ...............................1
                        .......9................99.....8
                        ...............................8
                        .....9.........................8
                        ...............................8
                        ...9.............3323332.....888
                        .............................888
                        99..........................8888
                        ............................8888
                        ...99......................88888
                        ...........................88888
                        ......99..................888888
                        ..........................888888
                        .........99..............8888888
                        .........................8888888
                        ............99..........88888888
                        ........................88888888
                        ...............99......888888888
                        .......................888888888
                        ..................99..8888888888
                        ......................8888888888
                        ...............99....88888888888
                        ..................33388888888888
                        ............99....88888888888888
                        ...............33388888888888888
                        .........99....88888888888888888
                        ............33388888888888888888
                        ......99....88888888888888888888
                        .........33388888888888888888888
                        ...99....88888888888888888888888
                        ......33388888888888888888888888
                        99....88888888888888888888888888
                        ...33388888888888888888888888888
                        33388888888888888888888888888888
                        88888888888888888888888888888888
                        88888888888888888888888888888888
        """))
        myTile = scene.get_tile(0, 42)
        myTile.place(mySprite)
        effects.bubbles.start_screen_effect()
    else:
        effects.blizzard.start_screen_effect()
    game.splash("Level " + str(num))
    facingRight = 1
    animation.set_action(mySprite, ActionKind.Idle_right)

def on_a_pressed():
    if mySprite2.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite2.vy = -160
        mySprite2.start_effect(effects.bubbles, 500)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_hit_tile_player(sprite):
    scene.camera_shake(4, 100)
scene.on_hit_tile(SpriteKindLegacy.Player, 13, on_hit_tile_player)

def on_left_pressed():
    global facingRight
    facingRight = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_hit_tile_player2(sprite2):
    scene.camera_shake(4, 100)
scene.on_hit_tile(SpriteKindLegacy.Player, 15, on_hit_tile_player2)

def on_hit_tile_player3(sprite3):
    scene.camera_shake(8, 1000)
scene.on_hit_tile(SpriteKindLegacy.Player, 14, on_hit_tile_player3)

def on_right_pressed():
    global facingRight
    facingRight = 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_combos_attach_combo():
    global level
    if level < 10:
        level += 1
        setLevel(level, mySprite2)
controller.combos.attach_combo("d+b", on_combos_attach_combo)

def on_hit_tile_player4(sprite4):
    global level
    # 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY';
    if level == 3:
        game.over(True, effects.star_field)
    else:
        level += 1
        setLevel(level, mySprite2)
scene.on_hit_tile(SpriteKindLegacy.Player, 1, on_hit_tile_player4)

def on_hit_tile_player5(sprite5):
    game.over(False, effects.bubbles)
scene.on_hit_tile(SpriteKindLegacy.Player, 3, on_hit_tile_player5)

def intitPlayer():
    global mySprite2, anim_idle_right, anim_idle_left, anim_walk_right, anim_walk_left
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . b d b . . . . . . 
                    . . . . . . . b d b c . . . . . 
                    . . . . b b c 5 5 5 c b b . . . 
                    . . . . b 5 5 5 1 5 5 5 b . . . 
                    . . . c c 5 5 5 1 5 5 5 c c . . 
                    . . b b 5 5 5 1 1 1 5 5 5 b b . 
                    . . d d 5 1 1 1 1 1 1 1 5 d d . 
                    . . b b 5 5 5 1 1 1 5 5 5 b b . 
                    . . . c c 5 5 5 1 5 5 5 c c . . 
                    . . . . b 5 5 5 1 5 5 5 b . . . 
                    . . . . b b c 5 5 5 c b b . . . 
                    . . . . . . c b d b c . . . . . 
                    . . . . . . . b d b . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKindLegacy.Player)
    anim_idle_right = animation.create_animation(ActionKind.Idle_right, 300)
    anim_idle_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d f d d f . . . . 
                . . . . e d d d f d d f . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_idle_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d f d d f . . . . 
                . . . . e d d d f d d f . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_idle_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d b d d b . . . . 
                . . . . e d d d b d d b . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    animation.attach_animation(mySprite2, anim_idle_right)
    anim_idle_left = animation.create_animation(ActionKind.Idle_left, 300)
    anim_idle_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . f d d f d e d e . . . . 
                . . . . f d d f d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_idle_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . f d d f d e d e . . . . 
                . . . . f d d f d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_idle_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . b d d b d e d e . . . . 
                . . . . b d d b d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    animation.attach_animation(mySprite2, anim_idle_left)
    anim_walk_right = animation.create_animation(ActionKind.Walking_right, 100)
    anim_walk_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d f d d f . . . . 
                . . . . e d d d f d d f . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_walk_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d f d d f . . . . 
                . . . . e d d d f d d f . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . d d . 6 6 6 6 . d d . . . 
                . . . d d . 6 6 6 6 . d d . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . . 6 . . . . . 
                . . . . . 6 . . . . 6 . . . . . 
                . . . . . f . . . . f . . . . .
    """))
    anim_walk_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d f d d f . . . . 
                . . . . e d d d f d d f . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 1 1 6 . . . . . . 
                . . . . . 6 6 1 1 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_walk_right.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . e e e e e e e . . . . 
                . . . . e e e e e e e e e . . . 
                . . . . e e e e d e e e e . . . 
                . . . . e e e d d d d d e . . . 
                . . . . e d e d f d d f . . . . 
                . . . . e d d d f d d f . . . . 
                . . . . . e d d d d d d . . . . 
                . . . . . . 6 6 1 6 . . . . . . 
                . . . . . 6 6 6 1 6 6 . . . . . 
                . . . . . d d 6 1 6 d . . . . . 
                . . . . . d d 6 6 6 d . . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . . 6 6 . . . . . . . 
                . . . . . . . 6 6 . . . . . . . 
                . . . . . . . f f . . . . . . .
    """))
    animation.attach_animation(mySprite2, anim_walk_right)
    anim_walk_left = animation.create_animation(ActionKind.Walking_left, 100)
    anim_walk_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . f d d f d e d e . . . . 
                . . . . f d d f d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 1 1 6 6 . . . . . . 
                . . . . . 6 1 1 6 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_walk_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . f d d f d e d e . . . . 
                . . . . f d d f d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 1 1 6 6 . . . . . . 
                . . . . . 6 1 1 6 6 6 . . . . . 
                . . . d d . 6 6 6 6 . d d . . . 
                . . . d d . 6 6 6 6 . d d . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . 6 . . . 6 . . . . . . 
                . . . . . 6 . . . . 6 . . . . . 
                . . . . . f . . . . f . . . . .
    """))
    anim_walk_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . f d d f d e d e . . . . 
                . . . . f d d f d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 1 1 6 6 . . . . . . 
                . . . . . 6 1 1 6 6 6 . . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . d d 6 6 6 6 d d . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . 6 . . 6 . . . . . . 
                . . . . . . f . . f . . . . . .
    """))
    anim_walk_left.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . e e e e e e e . . . . . 
                . . . e e e e e e e e e . . . . 
                . . . e e e e d e e e e . . . . 
                . . . e d d d d d e e e . . . . 
                . . . . f d d f d e d e . . . . 
                . . . . f d d f d d d e . . . . 
                . . . . d d d d d d e . . . . . 
                . . . . . . 6 1 6 6 . . . . . . 
                . . . . . 6 6 1 6 6 6 . . . . . 
                . . . . . d 6 1 6 d d . . . . . 
                . . . . . d 6 6 6 d d . . . . . 
                . . . . . . e e e e . . . . . . 
                . . . . . . . 6 6 . . . . . . . 
                . . . . . . . 6 6 . . . . . . . 
                . . . . . . . f f . . . . . . .
    """))
    animation.attach_animation(mySprite2, anim_walk_left)
    mySprite2.ay = 300
    mySprite2.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    scene.camera_follow_sprite(mySprite2)

def on_combos_attach_combo2():
    if level == 1:
        music.play_melody("B - - - - G A D ", 300)
    game.splash("***release date***")
controller.combos.attach_combo("babb", on_combos_attach_combo2)

anim_walk_left: animation.Animation = None
anim_walk_right: animation.Animation = None
anim_idle_left: animation.Animation = None
anim_idle_right: animation.Animation = None
facingRight = 0
myTile: tiles.Tile = None
mySprite2: Sprite = None
level = 0
game.set_dialog_cursor(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . b d b . . . . . . 
        . . . . . . . b d b c . . . . . 
        . . . . b b c 5 5 5 c b b . . . 
        . . . . b 5 5 5 1 5 5 5 b . . . 
        . . . c c 5 5 5 1 5 5 5 c c . . 
        . . b b 5 5 5 1 1 1 5 5 5 b b . 
        . . d d 5 1 1 1 1 1 1 1 5 d d . 
        . . b b 5 5 5 1 1 1 5 5 5 b b . 
        . . . c c 5 5 5 1 5 5 5 c c . . 
        . . . . b 5 5 5 1 5 5 5 b . . . 
        . . . . b b c 5 5 5 c b b . . . 
        . . . . . . c b d b c . . . . . 
        . . . . . . . b d b . . . . . . 
        . . . . . . . . . . . . . . . .
"""))
game.splash("MXQMC")
level = 1
intitPlayer()
setLevel(level, mySprite2)

def on_on_update():
    mySprite2.x += controller.dx(50)
game.on_update(on_on_update)

def on_on_update2():
    if mySprite2.is_hitting_tile(CollisionDirection.BOTTOM):
        if controller.right.is_pressed():
            animation.set_action(mySprite2, ActionKind.Walking_right)
        elif controller.left.is_pressed():
            animation.set_action(mySprite2, ActionKind.Walking_left)
        else:
            if facingRight == 1:
                animation.set_action(mySprite2, ActionKind.Idle_right)
            else:
                animation.set_action(mySprite2, ActionKind.Idle_left)
    else:
        if mySprite2.vy < 0:
            if facingRight == 1:
                mySprite2.set_image(img("""
                    . . . . . . . . . . . . . . . . 
                                        . . . . . e e e e e e e . . . . 
                                        . . . . e e e e e e e e e . . . 
                                        . . . . e e e e d e e e e . . . 
                                        . . . . e e e d f d d f e . . . 
                                        . . . . e d e d f d d f . . . . 
                                        . . . . e d d d d d d d . . . . 
                                        . . . . . e d d d d d d . . . . 
                                        . . . . . . 6 1 1 6 . . . . . . 
                                        . . . . . 6 6 1 1 6 6 . . . . . 
                                        . . . d d . 6 6 6 6 d . . . . . 
                                        . . . d d . 6 6 6 6 d . . . . . 
                                        . . . . . . e e e e . . . . . . 
                                        . . . . . . 6 . . 6 . . . . . . 
                                        . . . . . 6 . . f . . . . . . . 
                                        . . . . f . . . . . . . . . . .
                """))
            else:
                mySprite2.set_image(img("""
                    . . . . . . . . . . . . . . . . 
                                        . . . . e e e e e e e . . . . . 
                                        . . . e e e e e e e e e . . . . 
                                        . . . e e e e d e e e e . . . . 
                                        . . . e f d d f d e e e . . . . 
                                        . . . . f d d f d e d e . . . . 
                                        . . . . d d d d d d d e . . . . 
                                        . . . . d d d d d d e . . . . . 
                                        . . . . . . 6 1 1 6 . . . . . . 
                                        . . . . . 6 6 1 1 6 6 . . . . . 
                                        . . . . . d 6 6 6 6 . d d . . . 
                                        . . . . . d 6 6 6 6 . d d . . . 
                                        . . . . . . e e e e . . . . . . 
                                        . . . . . . 6 . . 6 . . . . . . 
                                        . . . . . . . f . . 6 . . . . . 
                                        . . . . . . . . . . . f . . . .
                """))
        else:
            if facingRight == 1:
                mySprite2.set_image(img("""
                    . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . e e e e e e e . . . . 
                                        . . . . e e e e e e e e e . . . 
                                        . . . . e e e e d e e e e . . . 
                                        . . . . e e e d d d d d e . . . 
                                        . . . . e d e d f d d f . . . . 
                                        . . . . e d d d f d d f . . . . 
                                        . . . . . e d d d d d d . . . . 
                                        . . . . . 6 6 1 1 6 6 . . . . . 
                                        . . . . . d d 1 1 6 . d d . . . 
                                        . . . . . d d 6 6 6 . d d . . . 
                                        . . . . . . e e e e . . . . . . 
                                        . . . . . . 6 . . 6 . . . . . . 
                                        . . . . . . . f . . f . . . . . 
                                        . . . . . . . . . . . . . . . .
                """))
            else:
                mySprite2.set_image(img("""
                    . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . e e e e e e e . . . . . 
                                        . . . e e e e e e e e e . . . . 
                                        . . . e e e e d e e e e . . . . 
                                        . . . e d d d d d e e e . . . . 
                                        . . . . f d d f d e d e . . . . 
                                        . . . . f d d f d d d e . . . . 
                                        . . . . d d d d d d e . . . . . 
                                        . . . . . 6 1 1 6 6 6 . . . . . 
                                        . . . d d . 1 1 6 d d . . . . . 
                                        . . . d d . 6 6 6 d d . . . . . 
                                        . . . . . . e e e e . . . . . . 
                                        . . . . . . 6 . . 6 . . . . . . 
                                        . . . . . f . . f . . . . . . . 
                                        . . . . . . . . . . . . . . . .
                """))
game.on_update(on_on_update2)
