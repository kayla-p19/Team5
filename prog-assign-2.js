var readLineSync = require('readline-sync'); // enable reading from the console

function main() { // main function
    const integers = []; // array to store integers entered by the user

    while (true) {
        const input = readLineSync.question("Enter an integer (or 'q' to quit):"); // prompting user to enter integers

        if (input.toLowerCase() === 'q') { // breaking loop if user enters 'q' or 'Q'
            console.log("Program terminating.")
            break;
          }

        // validating that the input is an integer
        const number = parseInt(input, 10);
        if (isNaN(number)) {
            console.log("Invalid input. Please enter an integer or 'q' to quit.");
            continue;
          }

        // adding the valid integer to the list
        integers.push(number);
}

  // displaying integers back to the user
  console.log(`You entered the following integers: ${integers.join(", ")}`);

  // checking if the condition is met
  let conditionMet = false;
  for (let i = 0; i < integers.length; i++) { // looping through each integer in the array
    for (let j = 0; j < integers.length; j++) { // using nested loop to compare with every other integer
      if (i !== j) { // making sure an integer isn't multiplying by itself
        const product = integers[i] * integers[j]; // computing product of the selected integers
        if (integers.includes(product)) { // if statement used to find product in array
          console.log(`Condition is met: ${integers[i]} x ${integers[j]} = ${product}`);
          conditionMet = true;
          break;
        }
      }
    }
    if (conditionMet) break;
  }

  if (!conditionMet) { // for when condition is not met
    console.log("Condition was not met.");
  }
}

// running the program
main();

console.log("i love brian")