document.addEventListener("DOMContentLoaded", function () {

    redInput = document.getElementById("red");
    greenInput = document.getElementById("green");
    blueInput = document.getElementById("blue");
    paintArea = document.getElementById("paintArea");
    generateButton = document.getElementById("generateButton");
    colorsArea = document.getElementById("colorsArea");
    colorsArray = [];
    colorsMax = 15;

    redInput.addEventListener("input", changeColor);
    greenInput.addEventListener("input", changeColor);
    blueInput.addEventListener("input", changeColor);

    function changeColor() {
        red = parseInt(redInput.value) || 0;
        green = parseInt(greenInput.value) || 0;
        blue = parseInt(blueInput.value) || 0;
        paintArea.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
    }

    generateButton.addEventListener("click", function () {
        red = parseInt(redInput.value);
        green = parseInt(greenInput.value);
        blue = parseInt(blueInput.value);

        if (ValidCheck(red) && ValidCheck(green) && ValidCheck(blue)) {
            color = `rgb(${red}, ${green}, ${blue})`;

            if (!colorsArray.includes(color)) {
                colorsArray.push(color);
                newColor = document.createElement("div");
                newColor.classList.add("newColor");
                newColor.style.backgroundColor = color;
                colorsArea.appendChild(newColor);

                if (colorsArea.children.length > colorsMax) {
                    colorsArea.removeChild(colorsArea.firstElementChild);
                }
            } else {
                alert("This Color is already exist in the area");
            }
        } else {
            alert("Invalid value for RGB color");
        }
    });

    function ValidCheck(value) {
        return value >= 0 && value <= 255;
    }

    colorsArea.addEventListener("click", function (event) {
        newColor = event.target;
        if (newColor.classList.contains("newColor")) {
            chooseColor = newColor.style.backgroundColor;
            localStorage.setItem("chosenColor", chooseColor);
        }
    });

    document.addEventListener("click", function (event) {
        target = event.target;
        chosenColor = localStorage.getItem("chosenColor");
        if (target !== colorsArea && target !== paintArea &&
            chosenColor) {
            target.style.backgroundColor = chosenColor;
        }
    });

});