class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0;
        string final = "";
        while (i<word1.length() || i<word2.length()){
            if (i < word1.length()) {
                final += word1[i];
            }
            if (i < word2.length()) {
                final += word2[i];
            }
            i++;
        }
    return final;
    }
};