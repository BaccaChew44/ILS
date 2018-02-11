$(document).ready(function () {
/*	
    $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                             break;
                         }
                     }
                 }
                 return cookieValue;
             }*/
            // if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
               //  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            // }
        // }
   // });
    while (true) {
        $.ajax({
            type: "POST",
            url: "http://192.168.1.1:8000/ILSA/NFC",
            async: false,
            error: function() {
               // alert('Error');
            }
        });
    }
});
