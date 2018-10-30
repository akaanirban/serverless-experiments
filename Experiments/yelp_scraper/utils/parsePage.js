const cheerio = require('cheerio');

module.exports = page => {
	try {
        const $ = cheerio.load(page);
        const ratings = $(".rating-info .i-stars").attr("title").trim();
        const reviewCount = $(".rating-info .review-count").text().trim();
        console.log(ratings, reviewCount);
    } catch (error) {
        return Promise.reject(`Error parsing string : ${JSON.stringify(error)}`);
    }
}