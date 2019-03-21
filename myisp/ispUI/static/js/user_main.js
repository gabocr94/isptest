$('#btn_send').click(function(){

try{
console.log('clicked meh');
var params = {}
params.username = $('#tx_username').val();
params.password = $('#tx_passw').val();
params.email = $('#tx_email').val();
params.csrftoken = getCookie('csrftoken');

var host = 'http://localhost:8000/'
console.log(params);
$.ajax({
            url : host+"api/create/user", // the endpoint
            type : "POST", // http method
            data : params,
            success : function(json, textMsg, xhr) {
                window.location.href = host+'customer/register';
            },
            error : function(xhr,errmsg,err) {
                alert('Opps! Something is wrong')
                console.log('Error:'+err)
            }
        });
}

catch (err){
   console.log(err)
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



