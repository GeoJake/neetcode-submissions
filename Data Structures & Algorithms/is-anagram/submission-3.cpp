class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> s_letters;
        map<char, int> t_letters;
        int len = s.length();
        
        if(len != t.length()){
            return false;
        }
        else{
            for(int i = 0; i < len; i++){

                char s_l = s[i];
                char t_l = t[i];

                if(s_letters.count(s_l)){
                    s_letters[s_l] += 1;
                }
                else{
                    s_letters.insert({s[i], 1});
                }

                if(t_letters.count(t_l)){
                    t_letters[t_l] += 1;
                }
                else{
                    t_letters.insert({t[i], 1});
                }
            }

            for(auto l : s_letters){
                cout << l.first << " " << l.second << endl;
                cout << t_letters[l.first] << endl;
                if(l.second != t_letters[l.first]){
                    return false;
                }
            }
        }
        return true;
    }
};
