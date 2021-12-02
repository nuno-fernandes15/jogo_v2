def on_button_pressed_a():
    global Tesoura, Microbit
    basic.show_string("You")
    Tesoura = 2
    basic.show_icon(IconNames.SCISSORS)
    basic.show_icon(IconNames.SCISSORS)
    basic.show_string("Micro")
    Microbit = randint(2, 4)
    if Microbit == 2:
        basic.show_icon(IconNames.SCISSORS)
        basic.show_icon(IconNames.SCISSORS)
        basic.show_string("Tie!")
    if Microbit == 4:
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_string("You win!")
    if Microbit == 3:
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_string("You loose!")
    game.resume()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Papel, Microbit
    basic.show_string("You")
    Papel = 4
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_string("Micro")
    Microbit = randint(2, 4)
    if Microbit == 4:
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_string("Tie!")
    if Microbit == 3:
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_string("You win!")
    if Microbit == 2:
        basic.show_icon(IconNames.SCISSORS)
        basic.show_icon(IconNames.SCISSORS)
        basic.show_string("You lose!")
    game.resume()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Pedra, Microbit
    basic.show_string("You")
    Pedra = 3
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_string("Micro")
    Microbit = randint(2, 4)
    if Microbit == 3:
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_string("Tie!")
    if Microbit == 2:
        basic.show_icon(IconNames.SCISSORS)
        basic.show_icon(IconNames.SCISSORS)
        basic.show_string("You win!")
    if Microbit == 4:
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_string("You lose!")
    game.resume()
input.on_button_pressed(Button.B, on_button_pressed_b)

Papel = 0
Pedra = 0
Tesoura = 0
Microbit = 0
basic.show_string("Starting Game")
Microbit = 1
Tesoura = 2
Pedra = 3
Papel = 4
basic.show_icon(IconNames.YES)
basic.show_string("Choose!")