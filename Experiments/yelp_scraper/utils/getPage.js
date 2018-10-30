const request = require('request-promise')

module.exports = businessName => {
    //https://www.yelp.com/biz/flights-of-fantasy-books-and-games-albany-4
    
    const url = `https://www.yelp.com/biz/${businessName}`;

    return request({method : 'GET', url});

} 