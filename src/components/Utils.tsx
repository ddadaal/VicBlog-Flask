export class Utils{
    static FetchViaJSON(url:string,payload:Object,callback:(json:any)=>any):void{
        let initProps = {
            cors:"cors",
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(payload)
        };
        window.fetch(url,initProps).then(res=>{
            return res.json();
        }).then(callback);
    }

    static FetchJSON(url:string,callback:(json:any)=>any):void{
        let initProps = {
            cors:"cors",
            method:"GET",
        };
        window.fetch(url,initProps).then(res=>{
            return res.json();
        }).then(callback);
    }

    public static readonly APIRoot:string = "http://viccrubs.tk/api/";
    public static readonly APIS = {
        login:Utils.APIRoot+"login",
        regsiter:Utils.APIRoot+"register",
        articles:Utils.APIRoot+"articles",
        article:Utils.APIRoot+"articles/"
    };
} 