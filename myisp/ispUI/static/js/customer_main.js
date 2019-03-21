
$('#btn_send').click(function(){

try{

var params = {}
params.id_card = $('#tx_idcard').val();
params.name = $('#tx_name').val();
params.lastname1 = $('#tx_last1').val();
params.lastname2 = $('#tx_last2').val();
params.csrftoken = getCookie('csrftoken');

var host = 'http://localhost:8000/'
console.log(params);
$.ajax({
            url : host+"api/create/customer", // the endpoint
            type : "POST", // http method
            data : params,
            success : function(json, textMsg, xhr) {
                alert('Registered succesfully.')
            },
            error : function(xhr,errmsg,err) {
                alert('Opps! Something is wrong: '+ err)
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