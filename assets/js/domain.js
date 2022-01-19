var looper;
var degrees = 0;

function rotateAnimation(el, speed) {
    clearTimeout(looper);
    var elem = document.getElementById(el);
    if (navigator.userAgent.match("Chrome")) {
        elem.style.WebkitTransform = "rotate(" + degrees + "deg)";
    } else if (navigator.userAgent.match("Firefox")) {
        elem.style.MozTransform = "rotate(" + degrees + "deg)";
    } else if (navigator.userAgent.match("MSIE")) {
        elem.style.msTransform = "rotate(" + degrees + "deg)";
    } else if (navigator.userAgent.match("Opera")) {
        elem.style.OTransform = "rotate(" + degrees + "deg)";
    } else {
        elem.style.transform = "rotate(" + degrees + "deg)";
    }

    looper = setTimeout("rotateAnimation('" + el + "'," + speed + ")", speed);
    degrees++;
    if (degrees > 359) degrees = 1;
}

function stoprotate() {
    if (looper) clearTimeout(looper);
}

// Stopping background scroll at modal popup
function StopScroll () {
    document.querySelector('html').style.overflowY= "hidden";
}

function RestoreScroll () {
    document.querySelector('html').style.overflowY= "auto";
}

// Ensuring scroll on clicks only outside modal
var n;
function store_n(k){    n= k;}

function checkForChanges()
{   
    StopScroll();
    if ($('#exampleModal' + n).hasClass('show'))
    {
        document.addEventListener("click", (evt) => {
            const flyoutEl = document.getElementById("mc-" + n);
            let targetEl = evt.target;    
            do {
              if(targetEl == flyoutEl)            
                return;
              targetEl = targetEl.parentNode;
            } 
            while (targetEl);
            RestoreScroll();
        });
    }
    else
        setTimeout(checkForChanges, 500);
}