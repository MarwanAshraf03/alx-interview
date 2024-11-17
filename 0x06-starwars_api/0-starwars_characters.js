#!/usr/bin/node
const request = require('request');
function requestAsync (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      resolve(body);
    });
  });
}
async function main () {
  request(
    'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
    async function (error, response, body) {
      if (error) throw error;
      const b = JSON.parse(body);
      for (let i = 0; i < b.characters.length; i++) {
        const response = await requestAsync(b.characters[i]);
        console.log(JSON.parse(response).name);
      }
    }
  );
}
main();
