#include <iostream>
using namespace std;

const int SIZE = 3;
char board[SIZE][SIZE];

void initializeBoard() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            board[i][j] = ' ';
        }
    }
}

void printBoard() {
    cout << "  0   1   2\n";
    for (int i = 0; i < SIZE; i++) {
        cout << i << " ";
        for (int j = 0; j < SIZE; j++) {
            cout << board[i][j];
            if (j < SIZE - 1) cout << " | ";
        }
        cout << endl;
        if (i < SIZE - 1) cout << " ---|---|---\n";
    }
}

bool isMoveValid(int row, int col) {
    return row >= 0 && row < SIZE && col >= 0 && col < SIZE && board[row][col] == ' ';
}

bool checkWin(char player) {
    // Check rows and columns
    for (int i = 0; i < SIZE; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
            (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
            return true;
        }
    }
    // Check diagonals
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
        return true;
    }
    return false;
}

bool isBoardFull() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == ' ') {
                return false;
            }
        }
    }
    return true;
}

void playGame() {
    char currentPlayer = 'X';
    int row, col;
    bool gameWon = false;

    initializeBoard();

    while (!gameWon && !isBoardFull()) {
        printBoard();
        cout << "Player " << currentPlayer << ", enter your move (row and column): ";
        cin >> row >> col;

        if (isMoveValid(row, col)) {
            board[row][col] = currentPlayer;
            gameWon = checkWin(currentPlayer);

            if (!gameWon) {
                currentPlayer

