#include <iostream>
#include <string>
using namespace std;

int main(){
  string str;
  string cycle;
  bool h = false;
  cin >> str >> cycle;
  for (int i = 0; i < cycle.length(); i++){
      cycle = cycle.substr(1, cycle.length()-1)+ cycle[0];
      if (str.find (cycle) != std::string::npos){
        cout << "yes";
        h = true;
        break;
	    }
  }
  if (h != true){
      cout << "no";
  }
  return 0;
}
