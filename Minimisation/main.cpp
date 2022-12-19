#include <iostream>
using namespace std;

const int DIM_TAB = 7;

void afficheTab(int mat[DIM_TAB][DIM_TAB]);
void transposee(int mat[DIM_TAB][DIM_TAB]);

int main(){
    int matA[DIM_TAB][DIM_TAB] = {
        {0,1,0,0,0,0,0},
        {0,0,0,0,0,1,0},
        {0,0,0,0,0,0,0},
        {0,0,0,0,0,0,1},
        {0,0,1,0,0,0,0},
        {0,0,0,0,0,1,0},
        {0,0,0,0,0,1,0},
    };

    int matB[DIM_TAB][DIM_TAB] = {
        {0,0,0,0,1,0,0},
        {0,0,1,0,0,0,0},
        {0,0,1,0,0,0,0},
        {0,0,0,0,1,0,0},
        {0,0,0,0,0,1,0},
        {0,0,0,1,0,0,0},
        {0,1,0,0,0,0,0},
    };
    int etatFinal = 2;
    transposee(matA);
    transposee(matB);
    


    cout << "Bonjour le monde" << endl;
    return 0;
}



void transposee(int mat[DIM_TAB][DIM_TAB]){
    int tmp[DIM_TAB][DIM_TAB];
    for (int i = 0; i<DIM_TAB; i++){
        for (int j = 0; j<DIM_TAB; j++){
            tmp[j][i] = mat[i][j];
        }
    }
    for (int i = 0; i<DIM_TAB; i++){
        for (int j = 0; j<DIM_TAB; j++){
            mat[i][j] = tmp[i][j];
        }
    }
    
}

void afficheTab(int mat[DIM_TAB][DIM_TAB]){
    for (int i = 0; i<DIM_TAB; i++){
        cout << "[ ";
        for (int j = 0; j<DIM_TAB; j++){
            cout << mat[i][j]<< " ";
        }
        cout << "]\n";
    }
    cout << "\n";
}