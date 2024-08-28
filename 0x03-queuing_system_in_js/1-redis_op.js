#!/usr/bin/yarn dev
//check the connection status of the Redis client instance.s
import { createClient, print } from 'redis';

const client = Redis.createClient();

//on connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

//on error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (_err, resp) => {
    console.log(resp);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
