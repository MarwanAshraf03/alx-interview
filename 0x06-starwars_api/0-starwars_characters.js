#!/usr/bin/node
const request = require("request");
function doRequest(url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (res.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}
async function main() {
  request(
    "https://swapi-api.alx-tools.com/api/films/" + process.argv[2],
    async function (error, response, body) {
      if (error) throw error;
      const b = JSON.parse(body);
      for (let i = 0; i < b.characters.length; i++) {
        try {
          const response = await doRequest(b.characters[i]);
          console.log(JSON.parse(response).name);
        } catch (error) {
          console.error(error);
        }
      }
    }
  );
}
main();
