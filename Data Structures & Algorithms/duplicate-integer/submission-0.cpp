class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dup;

        for(int i = 0; i < nums.size(); i++){

            int curr_num = nums.at(i);
            if (dup.find(curr_num) != dup.end()){
                return true;
            }
            else{
                dup.insert(curr_num);
            }

        }

        return false;

    }
};