$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "http://192.168.1.1:8000/ILSA/NFC",
        dataType: "text",
        async: false,
        success: function(data) {
            if (data === "No Swipe") {
                location.reload(true);
            }
            else if (data === "Error") {
                location.reload(true);
            } else {
                $.ajax({
                    type: "POST",
                    url: "http://192.168.1.1:8000/ILSA/swipe/" + data,
                    async: false,
                    success: function (swipe_response) {
                        window.location.href = swipe_response;
                    }
                });
            }
        },
        error: function() {
            // alert('Error');
        }
    });
});