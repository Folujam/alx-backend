//check the connection status of the Redis client instance.s
import Redis from 'redis';

const client = Redis.createClient();

//on connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

//on error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
