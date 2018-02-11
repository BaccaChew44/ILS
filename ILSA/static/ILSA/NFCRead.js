while (true) {
    $.ajax({
        type: "GET",
        url: "~/pi/linbfc/libnfc-1.7.0/examples/testCall.py",
        dataType: "text",
        async: false,
        success: function(data) {
            if (data === "No Swipe"){
            }
            if (data === "Error"){
            }
            else {
                $.ajax({
                    type: "POST",
                    url: "http://192.168.1.1/ILSA/swipe/" + data,
                    async: false
                });
            }
        },
        error: function() {
            alert('Error');
        }
    });
}