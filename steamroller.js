var flatten = function(input) {
    var flattenedArray = [];
    console.log(input.length);
    for (var i = 0; i < input.length; i++) {
        if (typeof input[i] === 'object') {
            flattenedArray = flattenedArray.concat(flatten(input[i]));
        } else {
            flattenedArray.push(input[i]); 
        }; 
 //         if (Array.isArray(array[i]) && array[i].length > 1) {
 //             flatten(array[i]);
 //         }
 //         else {
 //             flattenedArray.push(array[i]);
 //         }
    }
    return flattenedArray;
 }
 
console.log(flatten([1, [2], [3, [[4]]]]));