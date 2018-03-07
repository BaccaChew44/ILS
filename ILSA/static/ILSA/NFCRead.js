$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "http://192.168.1.1:8000/ILSA/NFC",
        dataType: "text",
        success: function(data) {
            if (data === "No Swipe") {
                location.reload(true);
            }
            else if (data === "Error") {
                location.reload(true);
            } else {
                $.ajax({
                    type: "GET",
                    url: "http://192.168.1.1:8000/ILSA/swipe/" + data + "/",
                    success: function (swipe_response) {
                        var value = swipe_response.response;
                        var url = "http://192.168.1.1:8000/";
                        if (value === "admin") {
                            window.location.href = url + value + "/";
                        } else if (value === "lockers") {
                            window.location.href = url + "ILSA/" + value + "/";
                        } else if (value === "success") {
                            window.location.href = url + "ILSA/lockers/" + value + "/";
                        }
                    }
                });
            }
        },
        error: function() {
            // alert('Error');
        }
    });
});
