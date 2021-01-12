
var svgWidth = 960;
var svgHeight = 500;

var margin = {
    top:20,
    right: 40,
    bottom: 80,
    left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create svg wrapper, append an svg group that will hold the chart
var svg = d3
    .select('#scatter')
    .append('svg')
    .attr('width', svgWidth)
    .attr('height', svgHeight);

// Append svg group
var chartGroup = svg.append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);

// Import the Data
d3.csv('../data/data.csv').then(function(mainData) {
    
    var povertyData = []
    // Parse the data and casts as numbers 
    mainData.forEach(function(data) {
        data.poverty = +data.poverty;
        data.healthcare = +data.healthcare;
        povertyData.push(+data.poverty)
    });

    console.log(povertyData);

    // Create scale functions
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(povertyData) - 1, d3.max(povertyData) + 1])  //d3.max(mainData, d => d.poverty
        .range([0, width - margin.right]);

    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(mainData, d => d.healthcare)])
        .range([height, 0]);

        
    // Create axis functions 
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append axes to the chart
    chartGroup.append('g')
        .attr('transform', `translate(0, ${height})`)
        .call(bottomAxis);

    chartGroup.append('g')
        .call(leftAxis);

    // Create the circles for the scatter plot
    var plotGroup = chartGroup.selectAll('g circle')
        .data(mainData)
        .enter();

    plotGroup
        .append('circle')
        .attr('cx', d => xLinearScale(d.poverty))
        .attr('cy', d => yLinearScale(d.healthcare))
        .attr('r', '10')
        .attr('class', 'stateCircle');
        

    plotGroup.append('text').text(d => d.abbr)
        .attr('dx', d => xLinearScale(d.poverty))
        .attr('dy', d => yLinearScale(d.healthcare))
        .attr('font-size', 12)
        .attr('class', 'stateText');


    // Create axes labels
    chartGroup.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('y', 0 - margin.left + 40)
        .attr('x', 0 - (height / 2))
        .attr('dy', '1em')
        .attr('class', 'aText')
        .text('Lacks Healthcare (%)');

    chartGroup.append('text')
        .attr('transform', `translate(${width / 2}, ${height + margin.top + 30})`)
        .attr('class', 'aText')
        .text('In Poverty (%)');

}).catch(function(error) {
    console.log(error);
});


