import * as React from 'react';
import { Button, Card } from 'antd';
import { LoginForm } from './LoginForm';

interface ProfileProps { }
interface ProfileStates { LoggedIn?: boolean, User?: IUser }


export class ProfileCard extends React.Component<ProfileProps, ProfileStates>{

    onLogout(){
        this.setState({
            LoggedIn: false,
            User: undefined
        });
    }

    onLogin(user: User) {
        this.setState({
            LoggedIn: true,
            User: user
        });
    }

    constructor(props: ProfileProps) {
        super(props);
        this.state = {
            LoggedIn: false,
            User: undefined
        }
    }
    render() {
        if (this.state.LoggedIn) {
            return <Card title={`Welcome, ${this.state.User.Username}`}>
            Your username: {this.state.User.Username}
            <Button onClick={this.onLogout.bind(this)}>Log out</Button>
            </Card>;
        }
        else {
            return <LoginForm LoginCallback={this.onLogin.bind(this)} />;
        }
    }
}