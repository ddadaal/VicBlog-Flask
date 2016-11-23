function login() {
    var warning = $("#warning");
    if (!$("#form_user").val()) {
        warning.text("Please input username!");
        warning.show();
        return;
    }
    if (!$("#form_password").val()) {
        warning.text("Please input password!");
        warning.show();
        return;
    }

    var form_login=$("#form_login");

    $.ajax({
        type: "POST", 
        url: form_login.attr("action"), 
        data: form_login.serialize(), 
        success: function( msg ) {
            var resp=JSON.parse(msg);
            if ( resp["status_code"]==200){
                Cookies.set('login', resp["token"]);
                location.reload();
            }
            if ( resp["status_code"]==401){
                warning.text("Invalid login.");
                warning.show();
            }
        },

    });

};



function login_clear() {
    $("#warning").hide();
};