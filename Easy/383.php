<?php

/*
Ransom Note (Easy)
Solved in O(n) time complexity and O(n) space complexity
*/

class Solution {

/**
 * @param String $ransomNote
 * @param String $magazine
 * @return Boolean
 */
function canConstruct($ransomNote, $magazine) {
    $tracker = array();

    for ($i = 0; $i < strlen($magazine); $i++) {
        $letter = $magazine[$i];
        if (array_key_exists($letter, $tracker)) {
            $tracker[$letter] += 1;
        }
        else {
            $tracker[$letter] = 1;
        }
    }

    for ($i = 0; $i < strlen($ransomNote); $i++) {
        $letter = $ransomNote[$i];
        if (!array_key_exists($letter, $tracker) || $tracker[$letter] <= 0) {
            return false;
        }
        else {
            $tracker[$letter] -= 1;
        }
    }

    return true;
}
}

?>