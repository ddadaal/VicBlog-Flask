function img_upload() {
    var upload = document.getElementById("img_upload_selector");
    var form = new FormData();
    var fileList=upload.files;
    for (var i= 0; i < fileList.length;i++){
        form.append(fileList[i].name, fileList[i]);
    };
    $.ajax({
        type: "POST", 
        url: "/compose", 
        contentType: false,
        data: form,  
        success: function(){ console.log("success"); }
    });
}
