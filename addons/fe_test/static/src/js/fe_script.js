odoo.define("test.code2", function (require) {
  "use strict";

  let SearchSubmitBlock = document.getElementsByClassName("input-group-append"); //Collecting all blocks with search button
  let ClearButtonsArray = []; //an array which keeps all Clear button instances

  //The functions which runs on clear button click

  const clearSearchField = function (event) {
    event.preventDefault();
    const SearchField = document.querySelectorAll("input[type=search]");
    SearchField.forEach((el) => {
      el.value = "";
    });
  };

  //Creating a new instance of Clear button for every Search box element, asigning its properties and placing it alongside to the Search button

  Array.from(SearchSubmitBlock).forEach((el, index) => {
    ClearButtonsArray[index] = document.createElement("button");
    ClearButtonsArray[index].class = "btn btn-primary";
    ClearButtonsArray[index].innerText = "Clear";
    ClearButtonsArray[index].onclick = clearSearchField;
    ClearButtonsArray[index].style = "border:1px solid black";
    console.log(ClearButtonsArray[index]);
    el.appendChild(ClearButtonsArray[index]);
  });
});
