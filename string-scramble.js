// Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

// Example
// input: "abcd", [0, 3, 1, 2]
// output: "acdb"
// Explanation
// The character 'a' is placed at index 0.

// The character 'b' is placed at index 3.

// The character 'c' is placed at index 1.

// The character 'd' is placed at index 2.

function scramble(str, arr) {
  //create an empty array with the size of str
  let result = new Array(str.length)
  //for loop and then replace each item in the empty array with letter in the string with index of array in the empty array 
  for(let i = 0; i < str.length ; i++){
    result[arr[i]] = str[i]
    
    
}
  
  //return result but use .join('')
  
  return result.join('')
}
