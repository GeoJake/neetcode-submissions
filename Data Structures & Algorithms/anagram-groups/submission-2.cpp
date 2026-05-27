class Solution {
public:
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int strs_size = strs.size();
        
        // cout << strs_size << endl;

        unordered_map<string, vector<string>> words;
        vector<vector<string>> out;

        for(const string & str : strs){
            string sortedString = str;
            sort(sortedString.begin(), sortedString.end());
            words[sortedString].push_back(str);
        }

        for(const auto & [key, value] : words){
            out.push_back(value);
        }

        return out;
    }
};
