#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    let count = 0;
    
    function getCharacterName(index) {
      if (index >= characters.length) {
        return;
      }
      request(characters[index], (error, response, body) => {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
          getCharacterName(index + 1);
        }
      });
    }
    
    getCharacterName(count);
  }
});
