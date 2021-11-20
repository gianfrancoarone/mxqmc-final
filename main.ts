namespace web {
    const CHANNEL = "web"

    function sendJSON(json: any) {
        const msg = JSON.stringify(json)
        const buf = Buffer.fromUTF8(msg);
        control.simmessages.send(CHANNEL, buf)
    }

    /**
     * Opens a new browser window to the given URL.
     * In order for this to work, you will need to follow
     * the instructions in the README. This will not do 
     * anything in arcade.makecode.com out of the box.
     */
    export function open(url: string) {
        sendJSON({
            action: "open",
            url: url
        })
    }
}
enum SpriteKindLegacy {
    Player,
    Projectile,
    Food,
    Enemy
}
enum ActionKind {
    Walking,
    Idle,
    Jumping,
    Walking_right,
    Walking_left,
    Idle_right,
    Idle_left
}
function setLevel (num: number, mySprite: Sprite) {
    scene.setBackgroundColor(15)
    scene.setTile(14, img`
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
        `, true)
    scene.setTile(7, img`
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
        `, false)
    scene.setTile(5, img`
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
        `, false)
    scene.setTile(2, img`
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
        `, true)
    scene.setTile(3, img`
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
        `, true)
    scene.setTile(8, img`
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
        `, true)
    scene.setTile(9, img`
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
        `, true)
    scene.setTile(15, img`
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
        `, true)
    scene.setTile(1, img`
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
        `, true)
    scene.setTile(10, img`
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
        `, false)
    scene.setTile(13, img`
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
        `, true)
    if (num == 0) {
        scene.setTileMap(img`
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 
            `)
    } else if (num == 1) {
        scene.setBackgroundImage(assets.image`office1`)
        scene.setTile(2, img`
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
            `, true)
        scene.setTile(3, img`
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
            `, true)
        scene.setTile(1, img`
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
            `, true)
        myTile = scene.getTile(0, 5)
        myTile.place(mySprite)
        effects.bubbles.startScreenEffect()
        scene.setTileMap(img`
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            5 . . . . . . . . . . . . . . . . . . 7 . . . . . . . . . . . . 
            8 8 8 8 8 8 8 . 8 8 8 8 8 8 8 . 8 8 8 8 8 8 8 . . . . . . . . 1 
            8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 3 8 8 8 8 8 8 8 8 
            `)
        myTile = scene.getTile(0, 3)
        myTile.place(mySprite)
        effects.bubbles.startScreenEffect()
    } else if (num == 2) {
        scene.setBackgroundImage(assets.image`office2`)
        scene.setTile(2, img`
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
            `, true)
        scene.setTile(1, img`
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
            `, true)
        scene.setTile(3, img`
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
            `, true)
        scene.setTileMap(img`
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
            `)
        myTile = scene.getTile(0, 29)
        myTile.place(mySprite)
        effects.bubbles.startScreenEffect()
    } else if (num == 3) {
        scene.setBackgroundImage(assets.image`office3`)
        scene.setTile(3, img`
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
            `, true)
        scene.setTileMap(img`
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
            `)
        myTile = scene.getTile(0, 42)
        myTile.place(mySprite)
        effects.bubbles.startScreenEffect()
    } else {
        effects.blizzard.startScreenEffect()
    }
    game.splash("Level " + num)
    facingRight = 1
    animation.setAction(mySprite, ActionKind.Idle_right)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -160
        mySprite.startEffect(effects.bubbles, 500)
    }
})
scene.onHitTile(SpriteKindLegacy.Player, 13, function (sprite) {
    scene.cameraShake(4, 100)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    facingRight = 0
})
scene.onHitTile(SpriteKindLegacy.Player, 15, function (sprite) {
    scene.cameraShake(4, 100)
})
scene.onHitTile(SpriteKindLegacy.Player, 14, function (sprite) {
    scene.cameraShake(8, 1000)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    facingRight = 1
})
controller.combos.attachCombo("d+b", function () {
    if (level < 10) {
        level += 1
        setLevel(level, mySprite)
    }
})
scene.onHitTile(SpriteKindLegacy.Player, 1, function (sprite) {
    if (level == 1) {
        //game.over(true, effects.starField)
        web.open('https://google.com')
    } else {
        level += 1
        setLevel(level, mySprite)
    }
})
scene.onHitTile(SpriteKindLegacy.Player, 3, function (sprite) {
    game.over(false, effects.bubbles)
})
function intitPlayer () {
    mySprite = sprites.create(img`
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
        `, SpriteKindLegacy.Player)
    anim_idle_right = animation.createAnimation(ActionKind.Idle_right, 300)
    anim_idle_right.addAnimationFrame(img`
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
        `)
    anim_idle_right.addAnimationFrame(img`
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
        `)
    anim_idle_right.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(mySprite, anim_idle_right)
    anim_idle_left = animation.createAnimation(ActionKind.Idle_left, 300)
    anim_idle_left.addAnimationFrame(img`
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
        `)
    anim_idle_left.addAnimationFrame(img`
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
        `)
    anim_idle_left.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(mySprite, anim_idle_left)
    anim_walk_right = animation.createAnimation(ActionKind.Walking_right, 100)
    anim_walk_right.addAnimationFrame(img`
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
        `)
    anim_walk_right.addAnimationFrame(img`
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
        `)
    anim_walk_right.addAnimationFrame(img`
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
        `)
    anim_walk_right.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(mySprite, anim_walk_right)
    anim_walk_left = animation.createAnimation(ActionKind.Walking_left, 100)
    anim_walk_left.addAnimationFrame(img`
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
        `)
    anim_walk_left.addAnimationFrame(img`
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
        `)
    anim_walk_left.addAnimationFrame(img`
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
        `)
    anim_walk_left.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(mySprite, anim_walk_left)
    mySprite.ay = 300
    mySprite.setFlag(SpriteFlag.StayInScreen, true)
    scene.cameraFollowSprite(mySprite)
}
controller.combos.attachCombo("babb", function () {
    if (level == 1) {
        music.playMelody("B - - - - G A D ", 300)
    }
    game.splash("***release date***")
})
let anim_walk_left: animation.Animation = null
let anim_walk_right: animation.Animation = null
let anim_idle_left: animation.Animation = null
let anim_idle_right: animation.Animation = null
let facingRight = 0
let myTile: tiles.Tile = null
let mySprite: Sprite = null
let level = 0
game.setDialogCursor(img`
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
    `)
game.splash("MXQMC")
level = 1
intitPlayer()
setLevel(level, mySprite)
game.onUpdate(function () {
    mySprite.x += controller.dx(50)
})
game.onUpdate(function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        if (controller.right.isPressed()) {
            animation.setAction(mySprite, ActionKind.Walking_right)
        } else if (controller.left.isPressed()) {
            animation.setAction(mySprite, ActionKind.Walking_left)
        } else {
            if (facingRight == 1) {
                animation.setAction(mySprite, ActionKind.Idle_right)
            } else {
                animation.setAction(mySprite, ActionKind.Idle_left)
            }
        }
    } else {
        if (mySprite.vy < 0) {
            if (facingRight == 1) {
                mySprite.setImage(img`
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
                    `)
            } else {
                mySprite.setImage(img`
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
                    `)
            }
        } else {
            if (facingRight == 1) {
                mySprite.setImage(img`
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
                    `)
            } else {
                mySprite.setImage(img`
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
                    `)
            }
        }
    }
})
