$('#btn_send').click(function(){

try{
var params = {};
params.username = $('#tx_username').val();
params.password = $('#tx_passw').val();
params.email = $('#tx_email').val();
params.csrftoken = getCookie('csrftoken');

var host = 'http://localhost:8000/';


$.post( host+"api/create/user", params, function() {
  window.location.href = host+'customer/register';
});
}
catch (err){
   alert(err);
}
})



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



