class Solution {
public:

    bool isAlpha(char &c) {

        if((c <= '9' && c >= '0') || (c <= 'Z' && c >= 'A') || (c <= 'z' && c >= 'a')){
            cout << c << endl;
            return true;
        }
        return false;
    }

    bool isPalindrome(string s) {

        char *p1 = &s[0];
        char *p2 = &s[s.length()-1];
        
        while(p1 <= p2){

            if(!isAlpha(*p1)){
                p1++;
            }
            if(!isAlpha(*p2)){
                p2--;
            }
            if(isAlpha(*p1) && isAlpha(*p2)){
                if (toupper(*p1) != toupper(*p2)){
                    return false;
                }
                p1++;
                p2--;
            }

        }

        return true;
    }
};
