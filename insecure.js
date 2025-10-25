// Bad practice: using eval
const userInput = process.argv[2];
eval(userInput);

// Hardcoded credentials
const password = "P@ssw0rd123";
console.log("Welcome", userInput);