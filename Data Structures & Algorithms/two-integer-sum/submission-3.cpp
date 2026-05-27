class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> vals;
        vector<int> out;

        for(int i = 0; i < nums.size(); i++){

            int curr_val = nums[i];
            int diff = target - curr_val;

            if(!vals.count(curr_val)){
                vals[curr_val] = i;
            }
            if(vals.count(diff) && (vals[diff] != i)){
                out.push_back(vals[diff]);
                out.push_back(i);
                return out; 
            }

        }

        return out; 
    }
};
