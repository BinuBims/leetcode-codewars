/*Given the following input array:

var list1 = [
  { firstName: 'Emily', lastName: 'N.', country: 'Ireland', continent: 'Europe', age: 30, language: 'Ruby' },
  { firstName: 'Nor', lastName: 'E.', country: 'Malaysia', continent: 'Asia', age: 20, language: 'Clojure' }
];
write a function that adds the username property to each object in the input array:

[
  { firstName: 'Emily', lastName: 'N.', country: 'Ireland', continent: 'Europe', age: 30, language: 'Ruby', 
    username: 'emilyn1990' },
  { firstName: 'Nor', lastName: 'E.', country: 'Malaysia', continent: 'Asia', age: 20, language: 'Clojure', 
    username: 'nore2000' }
]
*/

function addUsername(list) {
  let today = new Date();

  for(let i=0 ; i < list.length ; i++){
    const userName = list[i].firstName.toLowerCase() + list[i].lastName[0].toLowerCase() + String(today.getFullYear() - list[i].age)
    Object.assign(list[i], {'username': userName});
    console.log(list)
  }
  return list
  
  }
