"use strict"
// var came First .
// then let was introduced as var had some limitations.

// ################ Var keyword ##################

// #1. declare variable with var keyword.

var firstName = "Harshada";
// Can store information and declare variable.

firstName ="Harsh";
// Can change existing value.

var firstName ="HP"; 
// can be declared with same variable and overwrite value.

console.log(firstName);

// ################ let keyword ##################

// #1 . declare variable with let keyword.

let first_Name = "Harshu"; 
// Can store information and declare variable.

first_Name = "Patil"; 
// Can change existing value.

//  let first_Name ="Siddhi"; 
// (Already has been Declared error)
// Cannot redeclare same variable.
console.log(first_Name);

// ################ const keyword ##################

// #3 . declare constants
// whose values cannot be changed.

const pi = 3.14;
console.log(pi);
// Can store information and declare constant.


const pi1 = 3.14;
pi1 = 3.15; 
// cannot change the value of constant variable .
console.log(pi);


// block scope vs Function Scope 