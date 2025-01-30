<?php

/*
Isomorphic Strings (Easy)
Solved in O(n) time complexity and O(n) space complexity
*/


class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isIsomorphic($s, $t) {
        $sLen = strlen($s);
        $tLen = strlen($t);

        if ($sLen != $tLen) {
            return false;
        }

        $mapping1 = [];
        $mapping2 = [];

        for ($i = 0; $i < $sLen; $i++) {
            $sLetter = $s[$i];
            $tLetter = $t[$i];

            if (array_key_exists($sLetter, $mapping1) || array_key_exists($tLetter, $mapping2)) {
                if ($mapping1[$sLetter] != $tLetter || $mapping2[$tLetter] != $sLetter) {
                    return false;
                }
            }
            else {
                $mapping1[$sLetter] = $tLetter;
                $mapping2[$tLetter] = $sLetter;
            }
        }

        return true;
    }
}

?>