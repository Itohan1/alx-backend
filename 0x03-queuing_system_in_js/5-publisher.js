import { createClient, print } from 'redis';
import { promisify } from 'util';
let client = createClient();

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message, (err, res) => {
      if (err) {
        console.error("Could not send message");
      } else {
        console.log(`Message sent: ${message}`);
      }
   });
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
