// Write a function that accepts an integer argument n and generates an array containing the pairs of integers [a, b] that satisfy the condition

// 0 <= a <= b <= n
// The pairs should be sorted by increasing values of a, then by increasing values of b.

// For example,

// for input: 2
// it should return: [  [0, 0], [0, 1], [0, 2],  [1, 1], [1, 2],  [2, 2]  ]
function generatePairs(n) {
  //need an empty list
  let result = []
  // need two for loop to iterate over each cycle, however, after each iterate j start where i begins.
  for(let i = 0 ; i < n+1; i++){
    for(let j = 0; j+i < n+1; j++){
      //create a sublist and add it to the main list
      let sub_array = [i,j+i];
      result.push(sub_array)
      
    }
  }
  return result;
}
