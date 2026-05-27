class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> letters;

        if(s.length() != t.length()){
            return false;
        }

        for(int c : s){
            letters[c] += 1;
        }

        for(int c : t){
            letters[c] -= 1;
        }

        for(auto l : letters){

            if(l.second){
                return false;
            }

        }
        return true;
    }
};
