function login(){
    var warning=$("#warning");
    if (!$("#form_user").val()){
        warning.text("Please input username!");
        warning.show();
        return;
    }
    if (!$("#form_password").val()){
        warning.text("Please input password!");
        warning.show();
        return;
    }
    $("#form_login").submit();
};

function login_clear(){
    $("#warning").hide();
};