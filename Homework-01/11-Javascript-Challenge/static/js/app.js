// Assign the data from `data.js` to a var
var ufo = data

// Reference table body
var tbody = d3.select('tbody')

// Creates table
data.forEach((siting) => {
    console.log(siting);
    var row = tbody.append('tr');
    Object.entries(siting).forEach(([key,value]) => {
        var cell = row.append('td');
        cell.text(value);
    });
});

// Lets make the search engine operational //

// Selects the button
var button = d3.select('#filter-btn');
// Selects the form
var form = d3.select('#datetime');


// Sets event handlers
button.on('click', runEnter);
form.on('submit', runEnter);


function runEnter() {

    
    // prevents page from refreshing
    d3.event.preventDefault();

    // Selects the input elements and gets HTML node
    var inputElement = d3.select('#datetime');

    // Gets the value property of the input element
    var inputValue = inputElement.property('value');

    console.log(inputValue);


    var filteredUfo = ufo.filter(ufo => ufo.datetime === inputValue);

    console.log(filteredUfo);

    /////////////////// Form Filter //////////////////////////
    tbody.html("");
    
    var list = d3.select('#filters');

    filteredUfo.forEach((siting) => {
        console.log(siting);
        var row = tbody.append('tr');
        Object.entries(siting).forEach(([key,value]) => {
            var cell = row.append('td');
            cell.text(value);
        });
    });

};
