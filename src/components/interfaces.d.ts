interface IUser{
    Username: string
}

interface IArticle{
    Username:string,
    SubmitTime:number    
}

declare class User implements IUser {
    Username: string;
}