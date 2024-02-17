/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {string}
 */
var findLongestWord = function (s, dictionary) {
  let left = 0;
  let right = 0;
  let str = "";
  for (i = 0; i < dictionary.length; i++) {
    left = 0;
    right = 0;
    while (left < s.length && right < dictionary[i].length) {
      if (s.charAt(left) === dictionary[i].charAt(right)) {
        right++;
      }
      if (right === dictionary[i].length) {
        if (
          dictionary[i].length > str.length ||
          (dictionary[i].length == str.length && dictionary[i] < str)
        ) {
          str = dictionary[i];
        }
      }
      left++;
    }
  }
  return str;
};
