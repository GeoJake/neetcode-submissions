class Solution {
public:
    bool isAnagram(string s, string t){
        unordered_map<char, int> letters;

        if(s.length() != t.length()){
            return false;
        }

        if(!s.length() && !t.length()){
            return true;
        }
        
        for(int c: s){
            letters[c] += 1;
            // cout << char(c) << ": " << letters[c] << endl;
        }

        for(int c: t){
            letters[c] -= 1;
            // cout << char(c) << ": " << letters[c] << endl;
        }

        for(auto l : letters){

            if(l.second != 0){
                return false;
            }

        }

        return true;
    }
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int strs_size = strs.size();
        
        // cout << strs_size << endl;

        vector<vector<string>> groups;
        vector<int> pos(strs_size, -1);

        if(strs_size == 1){
            vector<string> temp = {strs[0]};
            groups.push_back(temp);
            return groups;
        }

        for(int i = 0; i < strs_size; i++){
            string curr_str = strs[i];
            if(pos[i] == -1){
                vector<string> temp = {strs[i]};
                groups.push_back(temp);
                pos[i] = groups.size()-1;
            }
            
            for(int j = i + 1; j < strs_size; j++){
                if(isAnagram(strs[i], strs[j]) && (pos[j] < 0)){
                    pos[j] = pos[i];
                    groups[pos[j]].push_back(strs[j]);
                }
            }
            

        }

        return groups;
    }
};
