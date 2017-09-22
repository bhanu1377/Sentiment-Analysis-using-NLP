/**
 * Created by CRK on 11/28/16.
 */

$(".dropdown .title").click(function () {
    $(this).parent().toggleClass("closed");
});

$(".dropdown li").click(function () {
    $(this).parent().parent().toggleClass("closed").find(".title").text($(this).text());
});