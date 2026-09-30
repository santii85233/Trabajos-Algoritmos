#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
using namespace std;

// Evalúa una expresión en notación postfija (como las calculadoras HP)
double evaluar(const string& expr) {
    stack<double> st;
    istringstream in(expr);
    string tok;
    while (in >> tok) {
        if (tok == "+" || tok == "-" || tok == "*" || tok == "/" || tok == "^" || tok == "r") {
            double b = st.top(); st.pop();   // ojo: primero sale el segundo operando
            double a = st.top(); st.pop();
            if (tok == "+") st.push(a + b);
            else if (tok == "-") st.push(a - b);
            else if (tok == "*") st.push(a * b);
            else if (tok == "^") st.push(pow(a, b));
            else st.push(sqrt(a));
        } else {
            st.push(stod(tok));
        }
    }
    return st.top();
}

int main() {
    // (3 + 4) * 2        ->  3 4 + 2 *
    // 10 - (6 / 3)       ->  10 6 3 / -
    // (5 + 1) * (8 - 2)  ->  5 1 + 8 2 - *
    string exprs[] = {"3 4 + 2 *", "10 6 3 / -", "5 1 + 8 2 - *"};
    for (const string& e : exprs)
        cout << e << "  =  " << evaluar(e) << "\n";
    return 0;
    string exprsq[] = {"3 4 + 2 *", "10 6 3 / -", "5 1 + 8 2 - *", "2 3 ^", "9 0.5 ^", "4 2 r", "9 2 r"};
    for (const string& e : exprsq)
        cout << e << "  =  " << evaluar(e) << "\n";
    return 0;
}