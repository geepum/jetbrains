let input = require('readline-sync');

const coffeeMachine = {
  coffee: {
    water: 400,
    milk: 540,
    beans: 120,
    cups: 9,
    money: 550
  },
  espresso: {
    water: 250,
    milk: 0,
    beans: 16,
    cups: 1,
    money: -4
  },
  latte: {
    water: 350,
    milk: 75,
    beans: 20,
    cups: 1,
    money: -7
  },
  cappuccino: {
    water: 200,
    milk: 100,
    beans: 12,
    cups: 1,
    money: -6
  }
}

function choices() {
  let action = input.question('Write action (buy, fill, take, remaining, exit):\n');

  return action;
}

function program(action) {
  let choice = '';
  switch (action) {
    case '1':
      choice = 'espresso';
      break;
    case '2':
      choice = 'latte';
      break;
    case '3':
      choice = 'cappuccino';
  }

  let chosen = coffeeMachine[choice];

  for (const item in chosen) {
    if (coffeeMachine.coffee[item] < chosen[item]) {
      console.log(`Sorry, not enough ${item}!\n`);
      return '';
    } else {
      coffeeMachine.coffee[item] -= chosen[item];
    }
  }
  console.log('I have enough resources, making you a coffee!\n');
}

function buy() {
  let action = input.question('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n');

  switch (action) {
    case '1':
      program(action);
      break;
    case '2':
      program(action);
      break;
    case '3':
      program(action);
      break;
    case 'back':
      program(action);
      break;
  }
}

function fill() {
  let fillWater = input.question('\nWrite how many ml of water do you want to add:\n');
  let fillMilk = input.question('Write how many ml of milk do you want to add:\n');
  let fillBeans = input.question('Write how many grams of coffee beans do you want to add:\n');
  let fillCups = input.question('Write how many disposable cups of coffee do you want to add:\n')

  coffeeMachine.coffee['water'] += Number(fillWater);
  coffeeMachine.coffee['milk'] += Number(fillMilk);
  coffeeMachine.coffee['beans'] += Number(fillBeans);
  coffeeMachine.coffee['cups'] += Number(fillCups);
  console.log('');
}

function take() {
  console.log(`\nI gave you ${coffeeMachine.coffee['money']}\n`);
  coffeeMachine.coffee['money'] = 0;
}

function remaining() {
  console.log(`\nThe coffee machine has:
${coffeeMachine.coffee['water']} ml of water
${coffeeMachine.coffee['milk']} ml of milk
${coffeeMachine.coffee['beans']} g of coffee beans
${coffeeMachine.coffee['cups']} disposable cups
${coffeeMachine.coffee['money']} of money\n`);
}

while (true) {
  let choice = choices();

  switch (choice) {
    case 'buy':
      buy();
      break;

    case 'fill':
      fill();
      break;

    case 'take':
      take();
      break;

    case 'remaining':
      remaining();
      break;

    case 'exit':
      return false;
  }
}