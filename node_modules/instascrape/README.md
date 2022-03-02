# instascrape

Scrape Instagram user public media without developer account or authentication. 

Uses the following endpoint:
https://www.instagram.com/username/media/

## Install

`npm install --save instascrape`

`yarn add instascrape`

## Usage

```javascript
import instascrape from 'instascrape';

instascrape('username')
  .then((data) => {
    // Do something with JSON data
  });

```
