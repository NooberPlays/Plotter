// parse a function string and return a function
const parseFunction = () => {
    const funcString = document.getElementById("function-input").value;
    return Function("x", `return ${funcString};`);
  };
  
  // create the x and y scales
  const x = d3.scaleLinear().domain([-15, 15]).range([0, 1000]);
  const y = d3.scaleLinear().domain([-15, 15]).range([1000, 0]);
  
  // create the x and y axes
  const xAxis = d3.axisBottom(x);
  const yAxis = d3.axisLeft(y);
  
  // create the SVG element
  const svg = d3.select("body").append("svg")
    .attr("width", 1000)
    .attr("height", 1000)
    .call(d3.zoom().on("zoom", () => {
      svg.attr("transform", d3.event.transform);
    }))
    .append("g");
  
  // draw the x and y axes
  svg.append("g")
    .attr("transform", "translate(50, 550)")
    .call(xAxis);
  svg.append("g")
    .attr("transform", "translate(50, 50)")
    .call(yAxis);
  
  // handle draw button click
  document.getElementById("draw-button").addEventListener("click", () => {
    const func = parseFunction();
    const xValues = d3.range(-15, 15.1, 0.1);
    const yValues = xValues.map(func);
    const data = d3.zip(xValues, yValues);
    svg.selectAll("rect").remove();
    svg.selectAll("rect")
      .data(data)
      .enter().append("rect")
      .attr("x", (d) => x(d[0]) + 50)
      .attr("y", (d) => y(d[1]) + 50)
      .attr("width", 5)
      .attr("height", 5)
      .attr("fill", "red");
  });
  
  // count the number of shapes inside the function
  const countFigures = (func) => {
    const shapes = svg.selectAll("rect");
    const shapesInside = shapes.filter(function() {
      const shape = d3.select(this);
      // compute the coordinates of the corners of the rectangle
      const x1 = x.invert(shape.attr("x"));
      const y1 = y.invert(shape.attr("y") - shape.attr("height"));
      const x2 = x.invert(shape.attr("x") + shape.attr("width"));
      const y2 = y.invert(shape.attr("y"));
      // check if all corners are inside the function
      return func(x1) >= y1 && func(x2) >= y1 && func(x1) <= y2 && func(x2) <= y2;
    });
    return shapesInside.size();
  };
  
  // handle count button click
  document.getElementById("count-button").addEventListener("click", () => {
    const func = parseFunction();
    const count = countFigures(func);
    const message = `There are ${count} shapes inside the function. Do you want to include shapes touching the function?`;
    const includeTouching = confirm(message);
    const shapesInside = svg.selectAll("rect").filter(function() {
      // compute the coordinates of the corners of the rectangle
      const x1 = x.invert(this.getAttribute("x"));
      const y1 = y.invert(this.getAttribute("y") - this.getAttribute("height"));
      const x2 = x.invert(parseFloat(this.getAttribute("x")) + parseFloat(this.getAttribute("width")));
      const y2 = y.invert(this.getAttribute("y"));
      // check if all corners are inside or touching the function
      const insideOrTouching =
        (func(x1) >= y1 && func(x2) >= y1 && func(x1) <= y2 && func(x2) <= y2) ||
        (includeTouching && (
          func(x1) < y1 && func(x2) >= y1 && func(x2) <= y2 ||
          func(x2) < y1 && func(x1) >= y1 && func(x1) <= y2 ||
          func(x1) < y2 && func(x2) >= y2 && func(x2) <= y2 ||
          func(x2) < y2 && func(x1) >= y2 && func(x1) <= y2
        ));
      return insideOrTouching;
    });
    shapesInside.attr("fill", "green");
    const shapesOutside = svg.selectAll("rect").filter(function() {
    const shape = d3.select(this);
    return !shapesInside.nodes().includes(this);
    });
    shapesOutside.attr("fill", "red");
    });