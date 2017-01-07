interface IUser{
    Username: string
}

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

declare class User implements IUser {
    Username: string;
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