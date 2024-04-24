/**
 * Return Length of Arguments Passed (Easy)
 * Solved in O(n) time complexity and O(1) space complexity
*/

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    count = 0
    for(let i = 0; i < args.length; i++) {
        count += 1
    }
    return count
};

/**
 * argumentsLength(1, 2, 3); // 3
 */