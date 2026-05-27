class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> vals;
        vector<int> out;

        for(int i = 0; i < nums.size(); i++){

            int curr_val = nums[i];
            int diff = target - curr_val;

            if(vals.count(diff) && (vals[diff] != i)){
                out.push_back(vals[diff]);
                out.push_back(i);
                return out; 
            }
            vals[curr_val] = i;
        }

        return out; 
    }
};
