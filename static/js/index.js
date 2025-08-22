document.addEventListener("DOMContentLoaded", function() {
    var centeredContainer = document.querySelector(".centered-container");
    var loadingScreen = document.getElementById("loadingScreen");
    loadingScreen.classList.add("hidden");
    setTimeout(function() {
        centeredContainer.classList.add("loaded");
        loadingScreen.style.display = "none";
    }, 200); 
});
window.addEventListener('load', function() {
    var loadingScreen = document.getElementById('loadingScreen');
    loadingScreen.classList.add('hidden');
});
function sendEmail() {
    var subject = "";
    var body = "";
    var email = "mehmtalnn07@gmail.com";
    var mailtoLink = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    window.location.href = mailtoLink;
}