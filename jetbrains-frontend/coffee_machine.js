let input = require('readline-sync');

const coffee = {
  water: 200,
  milk: 50,
  beans: 15
}

let water = Number(input.question(`Write how many ml of water the coffee machine has:\n`));
let milk = Number(input.question(`Write how many ml of milk the coffee machine has:\n`));
let beans = Number(input.question(`Write how many grams of coffee beans the coffee machine has:\n`));
let demand = Number(input.question(`Write how many cups of coffee you will need:\n`));

function compareWater() {
  return Math.floor(water / coffee['water']);
}
function compareMilk() {
  return Math.floor(milk / coffee['milk']);
}
function compareBeans() {
  return Math.floor(beans / coffee['beans']);
}

let coffeeWater = compareWater();
let coffeeMilk = compareMilk();
let coffeeBeans = compareBeans();
let minimumNumber = Math.min(coffeeWater, coffeeMilk, coffeeBeans);

if (demand === 1 && minimumNumber === 1) {
  console.log(`Yes, I can make that amount of coffee`);
} else if (demand > minimumNumber) {
  console.log(`No, I can make only ${minimumNumber} cups of coffee`);
} else if (demand < minimumNumber) {
  console.log(`Yes, I can make that amount of coffee (and even ${minimumNumber - demand} more than that)`);
} else if (water === 0 && milk === 0 && beans === 0 && demand === 0) {
  console.log(`Yes, I can make that amount of coffee`);
} 

