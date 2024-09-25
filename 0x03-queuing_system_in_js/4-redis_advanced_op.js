import { createClient, print } from 'redis';
import { promisify } from 'util';
let client = createClient();

client.on('error', (err) => {
  console.error('Error connecting to redis', err);
});

client.on('connect', () => {
  console.log('Connected to redis');

  const key = 'HolbertonSchools';

  const hash = {
    'Portland': '50',
    'Seattle': '80',
    'New York': '20',
    'Bogota': '20',
    'Cali': '40',
    'Paris': '2'
  };

  for (const field in hash) {
    client.hset(key, field, hash[field], print);
  }

});

const getAsync = promisify(client.hgetall).bind(client);

async function getSchool(dschool) {
  try {
    const reply = await getAsync(dschool);
    console.log(reply);
  } catch (err) {
    console.error('Error getting value:', err);
  }

  client.quit();
};

getSchool("HolbertonSchools");
