//Write your code here
const input = require('sync-input');

function phrase1() {
  console.log(`Welcome to Currency Converter!
1 USD equals  1 USD
1 USD equals  113.5 JPY
1 USD equals  0.89 EUR
1 USD equals  74.36 RUB
1 USD equals  0.75 GBP`);
}

function q1() {
  let q1 = input(`What do you want to do?
1-Convert currencies 2-Exit program\n`);
  return q1;
}

function q2() {
  console.log('What do you want to convert?');
}

function q2a1() {
  let q2a1 = input('From: ');
  return q2a1.toLowerCase();
}

function q2a2() {
  let q2a2 = input('To: ');
  return q2a2.toLowerCase();
}

function q2a3() {
  let q2a3 = input('Amount: ');
  return q2a3;
}

function answer(userAmount, fromCurrency, toCurrency) {
  let finalAmount = (userAmount * convert[toCurrency] / convert[fromCurrency]).toFixed(4);
  console.log(`Result: ${userAmount} ${fromCurrency.toUpperCase()} equals ${finalAmount} ${toCurrency.toUpperCase()}`);
}

const convert = {
  usd: 1,
  jpy: 113.5,
  eur: 0.89,
  rub: 74.36,
  gbp: 0.75
}

phrase1();

while (true) {
  let runProgram = q1().toString();

  if (runProgram == '1' || runProgram == '2') {
    if (runProgram == '2') {
      console.log('Have a nice day!');
    return false;
    } else {
      q2();
      let fromCurrency = q2a1();

      if (!(fromCurrency in convert)) {
        console.log('Unknown currency');
      } else {
        let toCurrency = q2a2();

        if (!(toCurrency in convert)) {
          console.log('Unknown currency');
        } else {
          let userAmount = q2a3();
          
          if (isNaN(userAmount)) {
            console.log('The amount has to be a number');
          } else {
            if (userAmount < 1) {
            console.log('The amount can not be less than 1');
          } else {
            answer(userAmount, fromCurrency, toCurrency);
          }  
          }
          
        }
      }
    }
  } else {
    console.log('Unknown input');
  }
}