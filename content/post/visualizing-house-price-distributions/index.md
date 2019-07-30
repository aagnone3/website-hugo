---
title: Visualizing House Price Distributions
subtitle: "With Zillow and python's Folium, it's easier than ever"
summary: "With Zillow and python's Folium, it's easier than ever"
authors:
- anthonyagnone

date: "2019-07-19T18:29:33Z"
featured: false
draft: false
# url: /visualizing-house-price-distributions/
# image: c.jpeg
# featured_image: /wp-content/uploads/2019/07/c.jpeg
image:
  placement: 2
  caption: ""
  focal_point: ""
  preview_only: false
categories:
  - data
tags:
  - algorithms
  - api
  - data-structures
  - data-visualization

---
### Wait, but&nbsp;Why?

I’m in the process of closing on my first home in Atlanta, GA, and have been heavily using various real estate websites like Zillow, Redfin, and Trulia. I’ve also been toying with <a rel="noreferrer noopener" href="https://www.zillow.com/howto/api/APIOverview.htm" target="_blank">Zillow’s API</a>, although somewhat spotty in functionality and documentation. Despite its shortcomings, I was fully inspired once I read the <a rel="noreferrer noopener" href="https://towardsdatascience.com/rat-city-visualizing-new-york-citys-rat-problem-f7aabd6900b2" target="_blank">post</a> by <a rel="noreferrer noopener" href="https://medium.com/u/5164378fc848" target="_blank">Lukas Frei</a> on using the `folium` library to seamlessly create geography-based visualizations. A few days and some quick fun later, I’ve combined Zillow and Folium to make some cool visualizations of housing prices both within Atlanta and across the U.S.

### Topics

  * API integration
  * Graph traversal
  * Visualization

### A Small Working&nbsp;Example

Let’s start simple by using some <a href="https://github.com/aagnone3/zillium/blob/master/data/State_MedianValuePerSqft_AllHomes.csv" rel="noreferrer noopener" target="_blank">pre-aggregated data</a> I downloaded from the Zillow website. This data set shows the median price by square foot for every state in the U.S. for each month from April 1996 to May 2019. Naturally, one could build a rich visualization on the progression of these prices over time; however, let’s stick with the most recent prices for now, which are in the last column of the file.

Having a look at the top-10 states, there aren’t many surprises. To be clear, I was initially caught off guard by the ordering of some of these, notably D.C. and Hawaii topping the chart. However, recall the normalization of “per square foot” in the metric. By that token, I’m maybe more surprised now that California still hits #3, given its size.

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://cdn-images-1.medium.com/max/800/1*m8dv-PmWxEdxXc-3f-O-Wg.png" alt="" /><figcaption>Top 10 price/sqft in thousands of $$$ (May&nbsp;2019)</figcaption></figure>
</div>

Anyways, onto the show! Since this is a visualization article, I’ll avoid throwing too many lines of code in your face, and link it all to you to it at the end of the article. In short, I downloaded a GeoJSON file of the U.S. states from the <a rel="noreferrer noopener" href="https://github.com/python-visualization/folium" target="_blank">folium repo</a>. This was a great find, because it immediately gave me the schema of the data that I needed to give to folium for a seamless process; the only information I needed to add was the pricing data (to generate coloring in the final map). After providing that, a mere 5 lines of code got me the following plot:

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://cdn-images-1.medium.com/max/800/1*otHI92R87cptloOqONQGxA.png" alt="" /><figcaption>Heatmap of price/sqft of homes in the U.S. for May&nbsp;2019</figcaption></figure>
</div>

### One Step&nbsp;Further

Now that I’d dipped my toes into the waters of Zillow and Folium, I was ready to be immersed. I decided to create a heat map of Metro Atlanta housing prices. One of the drawbacks of the Zillow API is that it’s rather limited in search functionality — I couldn’t find any way to perform a search based on lat/long coordinates, which would have been quite convenient for creating a granular heat map. Nevertheless, I took it as an opportunity to brush up on some crawler-style code; I used the results of an initial search by a city’s name as seeds for future calls to get the <a href="https://en.wikipedia.org/wiki/Comparables" rel="noreferrer noopener" target="_blank">comps</a> (via the <a href="https://www.zillow.com/howto/api/GetComps.htm" rel="noreferrer noopener" target="_blank">GetComps</a> endpoint) of those homes.

It’s worth noting that Zillow does have plenty of URL-based search filters that one could use to e.g. search by lat/long (see below). Obtaining the homes from the web page then becomes a scraping job, though, and you are subject to any sudden changes in Zillow’s web page structure. That being said, scraping projects can be a lot of fun; if you’d like to build this into what I made, let me know!

<pre class="wp-block-preformatted"># an example of a Zillow search URL, with plenty of specifications<br /><a href="https://www.zillow.com/atlanta-ga/houses/2-_beds/2.0-_baths/?searchQueryState=%7B%22pagination%22:%7B%7D,%22mapBounds%22:%7B%22west%22:-84.88217862207034,%22east%22:-84.07880337792972,%22south%22:33.53377471775447,%22north%22:33.999556422130006%7D,%22usersSearchTerm%22:%22Atlanta,%20GA%22,%22regionSelection%22:[%7B%22regionId%22:37211,%22regionType%22:6%7D],%22isMapVisible%22:true,%22mapZoom%22:11,%22filterState%22:%7B%22price%22:%7B%22min%22:300000,%22max%22:600000%7D,%22monthlyPayment%22:%7B%22min%22:1119,%22max%22:2237%7D,%22hoa%22:%7B%22max%22:200%7D,%22beds%22:%7B%22min%22:2%7D,%22baths%22:%7B%22min%22:2%7D,%22sqft%22:%7B%22min%22:1300%7D,%22isAuction%22:%7B%22value%22:false%7D,%22isMakeMeMove%22:%7B%22value%22:false%7D,%22isMultiFamily%22:%7B%22value%22:false%7D,%22isManufactured%22:%7B%22value%22:false%7D,%22isLotLand%22:%7B%22value%22:false%7D,%22isPreMarketForeclosure%22:%7B%22value%22:false%7D,%22isPreMarketPreForeclosure%22:%7B%22value%22:false%7D%7D,%22isListVisible%22:true%7D" rel="noreferrer noopener" target="_blank">https://www.zillow.com/atlanta-ga/houses/2-_beds/2.0-_baths/?searchQueryState={%22pagination%22:{},%22mapBounds%22:{%22west%22:-84.88217862207034,%22east%22:-84.07880337792972,%22south%22:33.53377471775447,%22north%22:33.999556422130006},%22usersSearchTerm%22:%22Atlanta,%20GA%22,%22regionSelection%22:[{%22regionId%22:37211,%22regionType%22:6}],%22isMapVisible%22:true,%22mapZoom%22:11,%22filterState%22:{%22price%22:{%22min%22:300000,%22max%22:600000},%22monthlyPayment%22:{%22min%22:1119,%22max%22:2237},%22hoa%22:{%22max%22:200},%22beds%22:{%22min%22:2},%22baths%22:{%22min%22:2},%22sqft%22:{%22min%22:1300},%22isAuction%22:{%22value%22:false},%22isMakeMeMove%22:{%22value%22:false},%22isMultiFamily%22:{%22value%22:false},%22isManufactured%22:{%22value%22:false},%22isLotLand%22:{%22value%22:false},%22isPreMarketForeclosure%22:{%22value%22:false},%22isPreMarketPreForeclosure%22:{%22value%22:false}},%22isListVisible%22:true}</a></pre>

Returning to the chosen path, I mentioned that I used initial results as entry points into the web of homes in a given city. With those entry points, I kept recursing into calls for each homes comps. An important assumption here is that Zillow’s definition of similarity between houses includes location proximity in addition to other factors. Without location proximity, the comp-based traversal of homes will be very non-smooth with respect to location.

So, what algorithms are at our disposal for traversing through a network of nodes in different ways? Of course, breadth-first search (BFS) and depth-first search (DFS) quickly come to mind. For the curious, have a look at the basic logic flow of it below. Besides a set membership guard, new homes are only added to the collection when they satisfy the constraints asserted in the `meets_criteria` function. For now, I do a simple L2 distance check between a pre-defined root lat/long location and the current home’s location. This criterion encouraged the search to stay local to the root, for the purposes of a well-connected and granular heat map. The implementation below uses DFS by popping off the end of the list (line 5) and adding to the end of the list (14), but BFS can be quickly achieved by changing either line (but not both) to instead use the front of the list.

Letting this algorithm run for 10,000 iterations on Atlanta homes produces the following map in just a few minutes! What’s more, the <a rel="noreferrer noopener" href="https://anthonyagnone.com/wp-shares-aagnone/atlanta_heatmap.html" target="_blank">generated web page</a> by folium is interactive, allowing common map navigation tools like zooming and panning. To prove out its modularity, I generated some smaller-scale maps of prices for <a rel="noreferrer noopener" href="https://anthonyagnone.com/wp-shares-aagnone/boston_heatmap.html" target="_blank">Boston, MA</a> and <a rel="noreferrer noopener" href="https://anthonyagnone.com/wp-shares-aagnone/seattle_heatmap.html" target="_blank">Seattle, WA</a> as well.

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://cdn-images-1.medium.com/max/800/1*Q81SBWiXe77l8xq8oqpgyw.png" alt="" /><figcaption>Heat map of Atlanta housing prices. See the interactive version&nbsp;<a href="https://anthonyagnone.com/wp-shares-aagnone/atlanta_heatmap.html" rel="noreferrer noopener" target="_blank">here</a>.</figcaption></figure>
</div>

### The Code

As promised, [here’s the project][1]. It has a Make+Docker setup for ease of use and reproducibility. If you’d like to get an intro to how these two tools come together nicely for reproducible data science, <a rel="noreferrer noopener" href="https://anthonyagnone.com/2019/07/10/towards-efficient-and-reproducible-ml-workflows-part-1-analysis/" target="_blank">keep reading here</a>. Either way, the <a rel="noreferrer noopener" href="https://github.com/aagnone3/zillium/blob/master/README.md" target="_blank">README</a> will get you up and running in no time, either via script or Jupyter notebook. Happy viz!

### What Now?

There are numerous different directions in which we could take this logic next. I’ve detailed a few below for stimulation, but I’d prefer to move in the direction that has the most support, impact, and collaboration. What do you think?



<!-- AddThis Advanced Settings generic via filter on the_content -->

<!-- AddThis Share Buttons generic via filter on the_content -->

 [1]: https://github.com/aagnone3/zillium
