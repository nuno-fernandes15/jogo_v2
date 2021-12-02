radio.onReceivedNumber(function (receivedNumber) {
    if (Player_2 == 2) {
        basic.showIcon(IconNames.Scissors)
        basic.showIcon(IconNames.Scissors)
        basic.showString("Tie!")
    }
    if (Player_2 == 3) {
        basic.showIcon(IconNames.SmallSquare)
        basic.showIcon(IconNames.SmallSquare)
        basic.showString("You loose!")
    }
    if (Player_2 == 4) {
        basic.showIcon(IconNames.Chessboard)
        basic.showIcon(IconNames.Chessboard)
        basic.showString("You win!")
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(2)
    basic.showIcon(IconNames.Scissors)
    basic.showIcon(IconNames.Scissors)
    basic.showString("P2,choose!")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(4)
    basic.showIcon(IconNames.Chessboard)
    basic.showIcon(IconNames.Chessboard)
    basic.showString("P2,choose!")
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(3)
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.SmallSquare)
    basic.showString("P2,choose!")
})
let Player_2 = 0
radio.setGroup(1)
Player_2 = 1
let Tesoura = 2
let Pedra = 3
let Papel = 4
basic.showString("Starting Game")
music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.OnceInBackground)
basic.showIcon(IconNames.Yes)
basic.showString("Choose!")
