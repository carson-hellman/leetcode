<?php

/*
Word Pattern (Easy)
Solved in O(n) time complexity and O(n) space complexity
*/

class Solution {

    /**
     * @param String $pattern
     * @param String $s
     * @return Boolean
     */
    function wordPattern($pattern, $s) {
        $s = explode(" ", $s);
        $sLen = count($s);
        $pLen = strlen($pattern);

        if ($sLen != $pLen) {
            return false;
        }

        $mapping1 = [];
        $mapping2 = [];

        for ($i = 0; $i < $sLen; $i++) {
            $sWord = $s[$i];
            $pLetter = $pattern[$i];

            if (array_key_exists($sWord, $mapping1) || array_key_exists($pLetter, $mapping2)) {
                if ($mapping1[$sWord] != $pLetter || $mapping2[$pLetter] != $sWord) {
                    return false;
                }
            }
            else {
                $mapping1[$sWord] = $pLetter;
                $mapping2[$pLetter] = $sWord;
            }
        }

        return true;
    }
}

?>