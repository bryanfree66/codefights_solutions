#include <algorithm>

bool checkPalindrome(std::string inputString) {
    int string_length = inputString.length();
    if(string_length == 1){return true;}
    int half_string_length = string_length / 2;
    bool is_even_length = false;
    if(string_length % 2 == 0){is_even_length = true;}
    std::string first_half = inputString.substr(0,half_string_length);
    std::string second_half;
    if(is_even_length){
         second_half = inputString.substr(half_string_length, half_string_length);
    }
    else{
       second_half = inputString.substr(half_string_length + 1, half_string_length);
    }

    std::reverse(second_half.begin(), second_half.end());
    if(first_half == second_half){return true;}
    return false;
}
