var file_list={};


function img_upload() {
    var form= new FormData(document.getElementById("form_img_upload"));
    $.ajax({
        type: "POST", 
        url: "/upload", 
        contentType: false,
        data: form,  
        processData : false, 
        cache: false, 
        success: function(msg){ 
            var resp=JSON.parse(msg);
            if (resp["status"]==="success"){
                $("#img_upload_modal").modal('hide');
                var filename=resp["filename"];
                file_list[filename]=resp["url"];
                update_list();
            }
         },
    });
}


function add_image(filename,url){
    var original = simplemde.value();
    original+="![{0}]({1})".format(filename,url);
    simplemde.value(original);    
}

function update_list(){
    var list=document.getElementById("files");
    for (var filename in file_list){
        var file =document.createElement("p");
        var url = document.createElement("a");
        url.setAttribute("href","javascript:add_image(\"{0}\",\"{1}\");".format(filename,file_list[filename]));
        url.innerText = file_list[filename];
        file.innerHTML="Filename: {0} :".format(filename);
        file.appendChild(url);
        list.innerHTML= "";
        list.append(file);
    }

}

function compose(){
    var form= new FormData();
    form.append("content",simplemde.value());
    $.ajax({
        type: "POST", 
        url : "/compose",   
        data: form, 
        processData: false,
        contentType: false, 
        success : function (msg){
            var resp=JSON.parse(msg);
            if (resp["status"]==="success"){
                window.location.href="/articles";
            }
        }
    })
}
