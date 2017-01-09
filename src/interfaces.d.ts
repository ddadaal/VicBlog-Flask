

interface IArticle extends IArticleItem{
    Content:string
}


interface IArticleItem{
    Username:string,
    Title:string,
    SubmitTime:string
    ID:number,
    Categories:string[]
}

declare class User {
    Username: string;
    Token:string;
}

declare class Article extends ArticleItem{
    Content:string;

}

declare class ArticleItem implements IArticleItem{
    Username:string;
    SubmitTime:string;
    Title:string;
    ID:number;
    Categories:string[];

}

interface Action{
    type:string,
    params:Object
}

declare class LoginStatus{
    User:User;
    LoggedIn:boolean;
}

declare class LoginProcessStatus{
    StatusText:string;
    Payload:User;
}