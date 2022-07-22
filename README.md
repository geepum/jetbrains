# Jetbrains

## Regex

### Slice method
let email = "hyperskill@gmail.com";
email.slice(11, 16); // 'gmail'

let text = "She sells seashells on the sea shore.";
text.slice(1, 4); 'he '

let str = "I am learning string methods."
str.slice(-8); // 'methods.'

let newStr = "JavaScript";
newStr.slice(-6, -1); // 'Scrip'

### Split method
let numbers = "123,456,789";

// separator is ","
let splitNumbers = numbers.split(",");  
console.log(splitNumbers); // [ '123', '456', '789' ]


let text = "jetbrains@gmail.com";

// separator is "@"
let splitText = text.split("@"); 
console.log(splitText); // [ 'jetbrains', 'gmail.com' ]

let languages = "JavaScript, Java, C++, C, Python, Kotlin";

// separator is "," and limit is "3"
let splitLang = languages.split(",", 3); 
console.log(splitLang); // [ 'JavaScript', ' Java', ' C++' ]


let text = "JetBrains";

// separator is empty string
let textSplit = text.split("", 5); 
console.log(textSplit); // ['J', 'e', 't', 'B', 'r']

let numbers = "2, 4, 6, 8, 10";

// separator is a regexp 
let splitNumbers = numbers.split(/\s*,\s*/);
console.log(splitNumbers); // ['2', '4', '6', '8', '10']


let text = "box, beatbox, boxer, boxing, postbox, box-sizing";

// separator is a regexp and limit is "4"
let regexp = /\bbox/
let splitText = text.split(regexp, 4);
console.log(splitText); // [ '', ', beatbox, ', 'er, ', 'ing, postbox, ' ]

### Replace method
let text = "Javascript Javascript javascript";

text.replace(/Javascript/, "JavaScript"); // 'JavaScript Javascript javascript'

text.replace(/Javascript/g, "JavaScript"); // 'JavaScript JavaScript javascript'

text.replace(/Javascript/gi, "JavaScript"); // 'JavaScript JavaScript JavaScript'

