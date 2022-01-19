var preloadTime;

preloader();

function preloader() {
    preloadTime = setTimeout(showPage, 2000);
}

function showPage() {
    document.getElementById("iaspreloader").style.display = "none";
}
