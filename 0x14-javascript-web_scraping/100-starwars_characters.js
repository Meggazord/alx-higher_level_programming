#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movie = JSON.parse(body);
    movie.characters.forEach((characterURL) => {
      request(characterURL, (error, response, body) => {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
