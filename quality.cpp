#include <iostream>
using namespace std;

int main() {
    int periods;
    float sum = 0;
    float x, y;
    cin >> periods;
    int i = 0;
    while(i < periods) {
            cin >> x;
            cin >> y;
            sum = sum + (x * y);
        i++;
    }
    cout << sum;
	return 0;
}
