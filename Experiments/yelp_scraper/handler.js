'use strict';

const {getPage, parsePage, saveRatingsToDb} = require("./utils");

module.exports.scrape = async (event, context) => {
  

	// 1. fetch yelp page
  getPage(event)
    // 2. Parse the page
    .then(page => parsePage(page))



	// 3. Save the ratings data to the db	


  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Go Serverless v1.0! Your function executed successfully!',
      input: event,
    }),
  };

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};
