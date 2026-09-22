#include <iostream>

using namespace std;
int main() {
 const int N = 6;
 int v[N];
 cout << "Ingrese 6 valores: ";
 for (int i = 0; i < N; i++) {
 cin >> v[i];
 }
 // Mostrar el arreglo del ultimo al primero
 for (int i = N - 1; i >= 0; i--) {
 cout << v[i];
 if (i > 0) cout << " ";
 }
 cout << endl;
 return 0;
}