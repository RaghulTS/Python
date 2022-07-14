#include <iostream>
using namespace std;

char xro[9] = {' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};

void printBoard() {
    cout << xro[0] << " | " << xro[1] << " | " << xro[2] << endl;
    cout << "-----------" << endl;
    cout << xro[3] << " | " << xro[4] << " | " << xro[5] << endl;
    cout << "-----------" << endl;
    cout << xro[6] << " | " << xro[7] << " | " << xro[8] << endl;
}

bool flag = false;
void winning(char winVar) {
    
    int winCase[8][3] = {
        {0, 1, 2},
        {3, 4, 5},
        {6, 7, 8},
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},
        {0, 4, 8},
        {2, 4, 6}
    };
    int winVal = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 3; j++) {
            if (xro[winCase[i][j]] == winVar) {
                winVal += 1;
            }
        }
        if (winVal == 3) {
            flag = true;
            break;
        }
        winVal = 0;
    }

}


int main() {

    printBoard();
    bool stopLoop = true;
    while (stopLoop) {
        int enterX;
        cout << "Enter X: ";
        cin >> enterX;
        while (xro[enterX-1] == 'X' || xro[enterX-1] == 'O'){
            cout << "Invalid\nEnter X: ";
            cin >> enterX;
        }

        xro[enterX-1] = 'X';
        printBoard();

        winning('X');

        if (flag == true) {
            cout << "X won" << endl;
            break;
        }



        int enterO;
        cout << "Enter O: ";
        cin >> enterO;
        while (xro[enterO-1] == 'X' || xro[enterO-1] == 'O'){
            cout << "Invalid\nEnter O: ";
            cin >> enterO;
        }
        
        xro[enterO-1] = 'O';
        printBoard();

        winning('O');

        if (flag == true) {
            cout << "X won" << endl;
            break;
        }


    }

}
