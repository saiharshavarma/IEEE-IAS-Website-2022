(function () {
  const second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;
 
  let offer= "July 26, 2022 23:59:59",
  // let offer= "Jan 2, 2022 17:00:00",
      countDown = new Date(offer).getTime(),
      x = setInterval(function() {    
 
        let now = new Date().getTime(),
            distance = countDown - now;
        document.getElementById("days").innerText = Math.floor(distance / (day)),
          document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
          document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
          document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);
          if (distance < 0) {

            document.getElementById("event_container").style.display = "none";
            if (screen.width < 430)
            {
              document.getElementById("About").style.marginTop = "300px";
            }
            let headline1 = document.getElementById("headline1"),
                headline2 = document.getElementById("headline2"),
                pak  = document.getElementById("pak"),
                countdown = document.getElementById("countdown"),
                content = document.getElementById("content");

            headline1.innerText = "Registrations are closed";
            headline2.innerText = "Stay tuned for the results!!";

            countdown.style.display = "none";
            pak.style.display = "none";
            content.style.display = "block";   

            clearInterval(x);
          }
        
       
      }, 0)
  }());
