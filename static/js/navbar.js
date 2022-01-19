function HamburgerToggle() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") x.className += " responsive";
    else x.className = "topnav";
}

$(".topnav a").on("click", function () {
    $(".topnav").removeClass("responsive");
});

$(document).ready(function() {
  $(window).scroll(function() {
  if($(this).scrollTop() < 100) 
    document.getElementById("scrollupbtn").style.display = "none";
  else 
    document.getElementById("scrollupbtn").style.display = "block";
  })
})

$(document).ready(function() {
    $(window).scroll(function() {
        var winScroll = $(window).scrollTop();
        var height =  $(document).height() - $(window).height();
        var scrolled = (winScroll / height) * 100;
        document.getElementById("myBar").style.width = scrolled + "%";
    })
})

// Navbar links turn active on scrolling 
const sections = document.querySelectorAll(".scroll-section");
const Lia = document.querySelectorAll(".navbar .topnav li a");
window.onscroll = () => {
    var current = "";
    
    sections.forEach((section) => {
        const sectionTop = section.offsetTop;
        const sectionHeight= section.offsetHeight;
        if (pageYOffset >= sectionTop - (sectionHeight / 3)) 
            current = section.getAttribute("id"); 
    });

    Lia.forEach((a) => {
        a.classList.remove("active");
        if (a.classList.contains(current)) 
            a.classList.add("active");        
    });
};
