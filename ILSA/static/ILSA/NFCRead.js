$(document).ready(function () {
while (true) {
    $.ajax({
        type: "POST",
        url: "/NFC",
        async: false,
        error: function() {
           // alert('Error');
        }
    });
}
});
