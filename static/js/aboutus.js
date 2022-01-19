if (screen.width > 430) {
    let x = document.getElementById("swipe");
    x.style.display = "none";
    document.getElementById("bt1").addEventListener(
        "click",
        (function1 = () => {
            document.querySelector("#pop").innerHTML =
                "<p>IEEE IAS VIT joins the league of prominent professional student chapters functioning at the university in the academic year 2015-16. We, the IEEE Industrial Applications Society, a group of undergraduates at VIT, aim to build a bridge between enthusiasm and excellence by providing a platform for brainstorming solutions to the industrial world, through the largest research conferences, expert talks, seminars, and bootcamps. We link research to practice, thereby connecting students to industrial experts.</p>";
        })
    );

    document.getElementById("bt2").addEventListener(
        "click",
        (function2 = () => {
            document.querySelector("#pop").innerHTML =
                "<p>Our chapter’s mission is to be the leading supplier of technological and industrial information to scholars whose skills and capabilities are wanted by larger industries and organizations. We will show you the path to achieve your dreams.  We tend to gift the various events, workshops, and webinars that we’ve organised to accomplish this with pride.</p>";
        })
    );

    document.getElementById("bt3").addEventListener(
        "click",
        (function3 = () => {
            document.querySelector("#pop").innerHTML =
                "<p>IEEE IAS vision lies in the advancement of technology linking theory and practice in the application of electrical and electronic systems for the benefit of humanity. We value the sharing of knowledge in our domains and the professional development of our membership.</p>";
        })
    );
} else {
    document.getElementById("pop").remove();
    document.getElementById("bt1").remove();
    document.getElementById("bt2").remove();
    document.getElementById("bt3").remove();
}

function ColorChange(element) {
    document.getElementById("bt1").style.color = "#FFF";
    document.getElementById("bt2").style.color = "#FFF";
    document.getElementById("bt3").style.color = "#FFF";

    element.style.color = "#0c8a2f";
}
