var xhr = new XMLHttpRequest();
xhr.open('GET', '/static/data/moving_data.csv');
xhr.send(null);

xhr.onreadystatechange = function () {
  var DONE = 4;
  var OK = 200;
  if (xhr.readyState === DONE) {
    if (xhr.status === OK) {
      var lines = csvToObject(xhr.responseText);
      var processedData = parseFields(lines);
      console.log(processedData);
      console.log("Total cubic footage: ");
      console.log(sumProperty("cubicFeet", processedData));
      console.log("Total square footage:");
      console.log(sumProperty("squareFeet", processedData));
      console.log("Square footage with mattress upright:");
      console.log(sumProperty("squareFeet", rotateFootprints(processedData, ["Mattress and box spring"])));
    }
    else {
      console.log('Error: ' + xhr.status);
    }
  }
};

function csvToObject(data) {
  var allLines = data.split(/\r\n|\n/);
  var headers = allLines[0].split(',');
  var lines = [];

  for (var i = 1; i < allLines.length; i++) {
    var data = allLines[i].split(',');
    if (data.length == headers.length) {
      var row = {};
      for (var j = 0; j < headers.length; j++) {
        row[headers[j]] = data[j];
      }
      lines.push(row);
    }
  }
  return lines;
}

function parseFields(data) {
  return data.map(function(i) {
    return {
      id: i.Thing,
      height: parseInt(i.Height),
      length: parseInt(i.Length),
      width: parseInt(i.Width),
      cubicFeet: cuInToCuFt(i.Height * i.Width * i.Length),
      squareFeet: sqInToSqFt(i.Width * i.Length)
    }
  });
}

function cuInToCuFt(cuIn) {
  return Math.ceil(cuIn / 1728); // Round up; be conservative in our estimation
}

function sqInToSqFt(sqIn) {
  return Math.ceil(sqIn / 144);
}

function sumProperty(prop, arr) {
  return arr.reduce(function(a, b) {
    return a + b[prop];
  }, 0);
  /*var total = 0;
  for (i in arr) {
    total += arr[i][prop];
  }
  return total;*/
}

function rotateFootprints(arr, item) {
  return arr.map(function(i) {
    if (i.id == item) {
      return {
        id: i.id,
        height: i.height,
        length: i.length,
        width: i.width,
        cubicFeet: i.cubicFeet,
        squareFeet: sqInToSqFt(i.width * i.height)
      };
    }
    else {
      return i;
    }
  });
}
