var readLineSync = require('readline-sync'); // enable reading from the console

console.log("Enter five integers below or enter 'q' to exit program."); 

// Collecting inputs in a for loop
var inputs = [];
for (var i = 1; i <= 5; i++) {
  while (true) {
    var input = readLineSync.question(`Enter integer ${i}: `);
    var num = parseInt(input, 10);

    // Checking if the input is a valid number
    if (!isNaN(num)) {
      inputs.push(num); // Adding valid number to the array
      break; // Exiting the while loop (after entering all valid numbers)
    } else if (input.toLowerCase() === 'q'){ // Else if statement if user hits q to exit program
      console.log("Program is quitting."); 
      process.exit(); // Exiting the program
    } else {
      console.log("Invalid input. Please enter a valid integer."); // If user enters a non-number or non-q, the message will show and allow user another chance 
    }
  }
}

// Calculating mean
var sum = inputs.reduce((acc, val) => acc + val, 0); // Summing all inputs
var mean = sum / 5; // Calculating mean of inputs

// Calculating median
inputs.sort((a, b) => a - b); // sorting the array in ascending order
var median = inputs[2]; // finding median; number 2 is used because it is a 0-based system and we are looking for the middle number which is the 3rd number in this case

console.log("Mean of your integers: " + mean); // Printing mean of integers
console.log("Median of your integers: " + median);