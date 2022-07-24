let input = require('readline-sync');

const coffee = {
  water: 400,
  milk: 540,
  beans: 120,
  cups: 9,
  money: 550
}

const espresso = {
  water: 250,
  milk: 0,
  beans: 16,
  cups: 1,
  money: -4
}

const latte = {
  water: 350,
  milk: 75,
  beans: 20,
  cups: 1,
  money: -7
}

const cappuccino = {
  water: 200,
  milk: 100,
  beans: 12,
  cups: 1,
  money: -6
}

const refresh = {
  water: 0,
  milk: 0,
  beans: 0,
  cups: 0,
  money: 0,
}

function beginPhrase() {
  console.log(`The coffee machine has:
${coffee['water']} ml of water
${coffee['milk']} ml of milk
${coffee['beans']} g of coffee beans
${coffee['cups']} disposable cups
${coffee['money']} of money\n`);
}

function endPhrase() {
  console.log(`\nThe coffee machine has:
${refresh['water']} ml of water
${refresh['milk']} ml of milk
${refresh['beans']} g of coffee beans
${refresh['cups']} disposable cups
${refresh['money']} of money\n`); 
}

function buy() {
  let coffeeChoices = input.question('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')

  switch (coffeeChoices) {
    case '1':
      for (const c in coffee) {
        refresh[c] = coffee[c] - espresso[c];
      }
      break;
    case '2':
      for (const c in coffee) {
        refresh[c] = coffee[c] - latte[c];
      } 
      break;
    case '3':
      for (const c in coffee) {
        refresh[c] = coffee[c] - cappuccino[c];
      }
      break;
  }
}

function fill() {
  let water = input.question('Write how many ml of water you want to add:\n')
  let milk = input.question('Write how many ml of milk you want to add:\n')
  let beans = input.question('Write how many ml of beans you want to add:\n')
  let cups = input.question('Write how many ml of cups you want to add:\n')

  refresh['water'] = coffee['water'] + Number(water);
  refresh['milk'] = coffee['milk'] + Number(milk);
  refresh['beans'] = coffee['beans'] + Number(beans);
  refresh['cups'] = coffee['cups'] + Number(cups);
  refresh['money'] = coffee['money'];
}

function take() {
  console.log(`I gave you ${coffee['money']}`);
  coffee['money'] = 0;
  for (const c in coffee) {
    refresh[c] = coffee[c];
  }
}

beginPhrase();

let choices = input.question('Write action (buy, fill, take):');

switch (choices) {
  case 'buy':
    buy();
    break;
  case 'fill':
    fill();
    break;
  case 'take':
    take();
    break;
}

endPhrase();