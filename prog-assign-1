var readLineSync = require('readline-sync'); // enable reading from the console

console.log("Enter five integers below."); 

var inputs = []; // creation of array to store inputs
inputs.push(parseInt(readLineSync.question("One: "), 10)); // asks user for the first number and so on
inputs.push(parseInt(readLineSync.question("Two: "), 10));
inputs.push(parseInt(readLineSync.question("Three: "), 10));
inputs.push(parseInt(readLineSync.question("Four: "), 10));
inputs.push(parseInt(readLineSync.question("Five: "), 10));

var sum = inputs.reduce((acc, val) => acc + val, 0); // summing all inputs
var mean = sum / 5; // finding mean of inputs

console.log("Mean of your integers: " + mean); // printing mean of integers