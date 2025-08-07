// 1. Array Basics
// Create an array with 10 random integers between 1 and 100.
// Remove the last 3 elements from the array.
// Add 2 new elements at the beginning of the array.
// 2. Access and Modify
// Replace the middle element with the number 999 (assume odd length).
// Swap the first and last elements in the array.
// 3. Searching
// Write a function that returns the index of the second occurrence of a number in an array.
// Write a function that checks if all elements in an array are unique.
// 4. Iteration
// Write a function that returns the sum of all even numbers in an array.
// Write a function that creates a new array of all elements that are divisible by 3.
// 5. Sorting & Reversing
// Sort an array of numbers in descending order without using sort().
// Reverse the array in place.
// 6. Nesting and Multidimensional
// Create a 2D array (3x3) and fill it with random numbers.
// Write a function that returns the sum of the diagonals of the 2D array.
// 7. Higher-Order Functions
// Write a function that takes an array of strings and returns a new array with only the strings longer than 4 characters.
// Use .map() to create a new array where each number is squared.
// Use .reduce() to get the product of all numbers in the array.
// 8. Destructuring & Spread
// Destructure the first 3 elements of an array into variables.
// Write a function that merges two arrays into one with unique values only (no duplicates).
// 9. Array Methods Mastery
// Write a function that returns the frequency count of each number in an array.
// Create a function that flattens a deeply nested array (e.g. [1, [2, [3, [4]]]] → [1, 2, 3, 4]).
// 10. Bonus: Algorithmic Thinking
// Given an array of numbers, find the longest increasing subsequence.
// Write a function that rotates an array to the right by k positions.
// Implement your own version of .filter() without using the built-in method.

let arrayNumber=[1,5,30,50,70,96,99,80,44,3];
const array=arrayNumber.splice(0,7);
console.log(array);

array.unshift(2,3);
console.log(array);
// Replace the middle element with the number 999 (assume odd length).
// Swap the first and last elements in the array.
array.splice(3,1,999);
console.log(array);
[array[0],array[array.length-1]]=[array[array.length-1],array[0]]
// array[0]=99;
// array[8]=2;
console.log(array);