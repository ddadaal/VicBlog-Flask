function img_upload() {
    var form= new FormData(document.getElementById("form_img_upload"));
    $.ajax({
        type: "POST", 
        url: "/compose", 
        contentType: false,
        data: form,  
        processData : false, 
        cache: false, 
        success: function(msg){ 
            if (msg==="success"){
                $("#img_upload_modal").modal('hide');
            }
         },
    });
}
