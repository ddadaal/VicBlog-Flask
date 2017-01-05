import * as React from 'react';

interface AccountIndicatorProps {}
interface AccountIndicatorStates { LoggedIn?: boolean, User?:IUser}


export class AccountIndicator extends React.Component<AccountIndicatorProps,AccountIndicatorStates>{
    constructor(props:AccountIndicatorProps){
        super(props);
        this.state={
            LoggedIn: false,
            User: undefined
        }
    }
    render(){
        if (this.state.LoggedIn){
            return <a>Hello! {this.state.User.Username}</a>;
        }
        else{
            return <a>Login please</a>;
        }
    }
}