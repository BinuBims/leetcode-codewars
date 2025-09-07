// Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array).

// You will need to add periods (.) to the end of the name if necessary, to turn it into a matrix.

// If the name has a length of 0, return "name must be at least one letter"

// Examples
// "Bill" ==> [ ["B", "i"],
//              ["l", "l"] ]

// "Frank" ==> [ ["F", "r", "a"],
//               ["n", "k", "."],
//               [".", ".", "."] ]


function matrixfy(str) {
  
  const perfectSquare = Math.ceil(Math.sqrt(str.length))
//   let i = 0
  let squareArray = []
  for(let s = 0 ; s < perfectSquare ; s++){
    squareArray.push([])
    for(let i=0 ; i < perfectSquare ; i++){
      squareArray[s].push(str[i] || '.')
      
    }
    str = str.slice(perfectSquare)
    
  }
  
  return squareArray.length ? squareArray : "name must be at least one letter"
  
//   find the length and the square root and then math.ceil
//   add the square root time square root, if nothing fill it with .

}
