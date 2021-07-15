$(document).ready(function() {
$("#user").click(function() {
$("#first").slideUp("slow", function() {
$("#second").slideDown("slow");
});
});
// On Click SignIn It Will Hide Registration Form and Display Login Form
$("#admin").click(function() {
$("#second").slideUp("slow", function() {
$("#first").slideDown("slow");
});
});
$("#user1").click(function(e) {
$("#forms").slideUp("slow");
 e.preventDefault();
});
});