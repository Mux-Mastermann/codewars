// This file contains different solution functions from codewars challenges for JavaScript

filter_list([1,2,'a','b']);

function filter_list(l) {
    // Kata: List Filtering
    return l.filter(item => typeof item != 'string')
}

function createPhoneNumber(numbers){
    //Kata: Create Phone Number
    // Create string with open (
    let result = "("
    // take first 3 numbers from input array and add to string
    for (let index = 0; index < 3; index++) {
        result += numbers.shift(); 
    }
    // add )SPACE to string
    result += ") "
    // take next 3 numbers from input array and add to string
    for (let index = 0; index < 3; index++) {
        result += numbers.shift(); 
    }
    // add - to string
    result += "-"
    // take last 4 numbers from input array and add to string
    for (let index = 0; index < 4; index++) {
        result += numbers.shift(); 
    }
    // return result
    return result
}
