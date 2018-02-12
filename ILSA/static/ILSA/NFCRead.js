$(document).ready(function () {
    var poll = true;
    while (poll) {
        $.ajax({
            type: "POST",
            url: "http://192.168.1.1:8000/ILSA/NFC",
            dataType: "text",
            async: false,
            success: function(data) {
                if (data === "No Swipe") {
                    window.location.href = 'http://192.168.1.1:8000/ILSA/';
                }
                else if (data === "Error") {
                    window.location.href = 'http://192.168.1.1:8000/ILSA/';
                } else {
                    poll = false;
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
    }
});
