// This file contains different solution functions from codewars challenges for JavaScript

filter_list([1,2,'a','b']);

function filter_list(l) {
    // Kata: List Filtering
    return l.filter(item => typeof item != 'string')
}
