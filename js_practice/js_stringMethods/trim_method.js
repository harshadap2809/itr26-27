// ############# Useful String Methods ################


// #1. Trim Method.

/* 
The trim() method in Java String is a built-in 
function that eliminates leading and trailing spaces.
*/
// --------------------------------------------------------------

let first_name = " Harshada     ";

// Spaces are even counted in String.length

console.log(first_name.length); 
first_name.trim();
console.log(first_name.length); 
// No Change
// As strings are immutable the output will be new string
// in string constant  pool;
// we need to make new variable to assign that value or it will
// Garbage collected later.
 

// --------------------------------------------------------------
// Storing in completely new Variable
let newString = first_name.trim();
console.log(newString); 

console.log(newString.length); 
console.log(first_name.length); 

// --------------------------------------------------------------
// Storing in old Variable itself and modifying it

first_name = first_name.trim();
console.log(newString); 

console.log(newString.length); // 9
console.log(first_name.length); // 9

