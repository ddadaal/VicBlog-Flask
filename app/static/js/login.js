function login(){
    var warning=$("#warning");
    if (!$("#form_user").value){
        warning.css("display","inline");
        warning.text("Please input username");
    }
}