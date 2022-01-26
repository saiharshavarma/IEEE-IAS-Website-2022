if (screen.width < 430) {
    document.getElementById("boardbt1").addEventListener(
        "click",
        (function1 = () => {
            document.getElementById("Board22").style.display = "none";
            document.getElementById("Board21").style.display = "block";
        })
    );

    document.getElementById("boardbt2").addEventListener(
        "click",
        (function2 = () => {
            document.getElementById("Board21").style.display = "none";
            document.getElementById("Board22").style.display = "block";
        })
    );
} else {
    document.getElementById("boardbt1").remove();
    document.getElementById("boardbt2").remove();
    document.getElementById("Board21").remove();
    document.getElementById("Board22").remove();
}

function BoardColorChange(element) {
    document.getElementById("boardbt1").style.color = "#FFF";
    document.getElementById("boardbt2").style.color = "#FFF";

    element.style.color = "#0c8a2f";
}
