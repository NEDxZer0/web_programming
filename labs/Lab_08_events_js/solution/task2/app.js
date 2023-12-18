document.addEventListener("DOMContentLoaded", function () {
    
    redInput = document.getElementById("red");
    greenInput = document.getElementById("green");
    blueInput = document.getElementById("blue");
    colorArea = document.getElementById("paintArea");

    redInput.addEventListener("input", changeColor);
    greenInput.addEventListener("input", changeColor);
    blueInput.addEventListener("input", changeColor);
    
    function changeColor() {
        red = parseInt(redInput.value) || 0;
        green = parseInt(greenInput.value) || 0;
        blue = parseInt(blueInput.value) || 0;
        colorArea.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
    }
});