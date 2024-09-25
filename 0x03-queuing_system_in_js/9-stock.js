import { createClient } from 'redis';
const client = createClient();

const express = require('express');
const app = express();
const listProducts = [
  {'Id': '1', 'name': 'Suitcase 250', 'price': '50', 'stock': '4'},
  {'Id': '2', 'name': 'Suitcase 450', 'price': '100', 'stock': '10'},
  {'Id': '3', 'name': 'Suitcase 650', 'price': '350', 'stock': '2'},
  {'Id': '4', 'name': 'Suitcase 1050', 'price': '550', 'stock': '5'}
]

function getItemById(Id) {
  return listProducts.find(product => product.id === id);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
}).listen(1245);

client.on('error', (err) => console.error(Redis client error: ${err}));
client.on('connect', () => console.log('Connected to Redis server'));

async function reserveStockById(itemId, stock) {
  try {
    await client.set(item.${itemId}, stock);
    console.log(Reserved stock for the item ${itemId}: ${stock});
  } catch (error) {
    console.error(Error setting stock for ${itemId}: ${error})
  }
}

async function getCurrentReservedStockById(itemId) {
  try {
    const stock = await client.get(item.${itemId});
    return stock ? parseInt(stock, 10) : 0;
  } catch (error) {
    console.error(Error setting stock for ${itemId}: ${error});
    return null;
  }
};
