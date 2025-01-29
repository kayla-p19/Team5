var readLineSync = require('readline-sync'); // enable reading from the console

function main() { // main function
    const integers = []; // array to store integers entered by the user

    while (true) {
        const input = readLineSync.question("Enter an integer (or 'q' to quit):"); // prompting user to enter integers

        if (input.toLowerCase() === 'q') { // breaking loop if user enters 'q' or 'Q'
            console.log("Program terminating.")
            break;
          }

        // Validate that the input is an integer
        const number = parseInt(input, 10);
        if (isNaN(number)) {
            console.log("Invalid input. Please enter an integer or 'q' to quit.");
            continue;
          }

        // Add the valid integer to the list
        integers.push(number);
}

  // Echo the integers back to the user
  console.log(`You entered the following integers: ${integers.join(", ")}`);

  // Check if the condition is met
  let conditionMet = false;
  for (let i = 0; i < integers.length; i++) {
    for (let j = 0; j < integers.length; j++) {
      if (i !== j) {
        const product = integers[i] * integers[j];
        if (integers.includes(product)) {
          console.log(`Condition is met: ${integers[i]} x ${integers[j]} = ${product}`);
          conditionMet = true;
          break;
        }
      }
    }
    if (conditionMet) break;
  }

  if (!conditionMet) {
    console.log("Condition was not met.");
  }
}

// Run the program
main();