let alpha = 2;
let vertices = 6;

$(document).ready(function () {
    var radius = 200;
    var fields = $(".itemDot");
    var container = $(".dotCircle");
    var width = container.width();
    radius = width / 2.5;

    var height = container.height();
    var angle = 0,
        step = (2 * Math.PI) / fields.length;
    fields.each(function () {
        var x = Math.round(
            width / 2 + radius * Math.cos(angle) - $(this).width() / 2
        );
        var y = Math.round(
            height / 2 + radius * Math.sin(angle) - $(this).height() / 2
        );
        if (window.console) {
            console.log($(this).text(), x, y);
        }

        $(this).css({
            left: x + "px",
            top: y + "px",
        });
        angle += step;
    });

    $(".itemDot").click(function () {
        var dataTab = $(this).data("tab");
        $(".itemDot").removeClass("active");
        $(this).addClass("active");
        $(".CirItem").removeClass("active");
        $(".CirItem" + dataTab).addClass("active");
        $(".ImgItem").removeClass("active");
        $(".ImgItem" + dataTab).addClass("active");
        alpha = dataTab;

        $(".dotCircle").css({
            transform:
                "rotate(" + (360 - (alpha - 1) * (360 / vertices)) + "deg)",
            transition: "2s",
        });
        $(".itemDot").css({
            transform: "rotate(" + (alpha - 1) * (360 / vertices) + "deg)",
            transition: "1s",
        });
    });

    setInterval(function () {
        var dataTab = $(".itemDot.active").data("tab");
        if (dataTab > vertices || alpha > vertices) {
            dataTab = 1;
            alpha = 1;
        }
        $(".itemDot").removeClass("active");
        $('[data-tab="' + alpha + '"]').addClass("active");
        $(".CirItem").removeClass("active");
        $(".CirItem" + alpha).addClass("active");
        $(".ImgItem").removeClass("active");
        $(".ImgItem" + alpha).addClass("active");
        alpha++;

        $(".dotCircle").css({
            transform:
                "rotate(" + (360 - (alpha - 2) * (360 / vertices)) + "deg)",
            transition: "2s",
        });
        $(".itemDot").css({
            transform: "rotate(" + (alpha - 2) * (360 / vertices) + "deg)",
            transition: "1s",
        });
    }, 5000);
});
