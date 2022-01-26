if (screen.width < 430) {
    document.getElementById("boardbtn1").addEventListener(
        "click",
        (function1 = () => {
            document.getElementById("M-Board21").style.display = "block";
            document.getElementById("M-Board22").style.display = "none";
        })
    );

    document.getElementById("boardbtn2").addEventListener(
        "click",
        (function2 = () => {
            document.getElementById("M-Board21").style.display = "none";
            document.getElementById("M-Board22").style.display = "block";
        })
    );
} else {
    document.getElementById("M-Board21").remove();
    document.getElementById("M-Board22").remove();
    document.getElementById("boardbtn1").remove();
    document.getElementById("boardbtn2").remove();
}

function BoardColorChange(element) {
    document.getElementById("boardbtn1").style.color = "#FFF";
    document.getElementById("boardbtn2").style.color = "#FFF";

    element.style.color = "#0c8a2f";
}
