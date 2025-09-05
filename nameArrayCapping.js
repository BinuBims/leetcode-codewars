//Create a function that accepts an array of names, and returns an array of each name with its first letter capitalized and the remainder in lowercase.

//Examples
//["jo", "nelson", "jurie"] -->  ["Jo", "Nelson", "Jurie"]
//["KARLY", "DANIEL", "KELSEY"] --> ["Karly", "Daniel", "Kelsey"]

function capMe(names) {
//take an array of names
// output array of names that each name's first letter capitalized and the remainder in lowercase.
// capMe(["jo", "nelson", "jurie"]) => ["Jo", "Nelson", "Jurie"]
  
// use .map() create a new array / capture the firstletter of each word and use .toUpperCase() and rest of the word to .toLowerCase()

  const names_list = names.map(name => name.slice(0,1).toUpperCase() + name.slice(1).toLowerCase());
  
  return names_list
}
