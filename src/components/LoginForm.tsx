import * as React from 'react';
import { Link } from 'react-router';
interface NavbarProps { selectedTab?:number }

export class Login extends React.Component<NavbarProps,undefined>{
    constructor(props:NavbarProps){
        super(props);
    }
    render(){
        return (
            <div/>
        );
    }
}