import * as React from 'react';
import Utils from './Utils';
import { Button,Form,Modal,message } from 'antd';
import { loginForm } from './LoginForm';

interface NavAccountIndicatorProps {
    LoginStatus:LoginStatus;
}

interface NavAccountIndicatorStates{
    LoginStatus?:LoginStatus,
    LoginModalVisible?:boolean,
}


export class NavAccountIndicator extends React.Component<undefined,NavAccountIndicatorStates>{
    
    styleTop16pxMore = { marginTop: 16};

    constructor(){
        super();
        this.state = {
            LoginStatus:{
                User:undefined,
                LoggedIn:false
            },
            LoginModalVisible:false,
        };
    }
    componentDidMount(){
        this.setState({
            LoginStatus:Utils.loadLoginStatus(),
        });
    }

    handleLoginInit(){
        this.setState({
            LoginModalVisible:true
        });
    }

    handleModalCancel(){
        this.setState({
            LoginModalVisible:false
        });
    }

    handleLoginProcessEnd(status:LoginProcessStatus){
        if (status.StatusText=="success"){
            Utils.storeLoginStatus({
                User:status.Payload,
                LoggedIn:true
            });
            this.setState({
                LoginModalVisible:false,
                LoginStatus:Utils.loadLoginStatus()
            });
        }else{
            message.error("Login Failed! Try again!");
        };
    }


    render(){
        if (this.state.LoginStatus.LoggedIn){
            return <a style={this.styleTop16pxMore}>Welcome, {this.state.LoginStatus.User.Username}</a>;
        }else{
            return (<div>
            <Button style={this.styleTop16pxMore} type="primary" onClick={this.handleLoginInit.bind(this)} >Login</Button>
            <LoginModal onCancel={this.handleModalCancel.bind(this)} visible={this.state.LoginModalVisible} LoginEndCallback={this.handleLoginProcessEnd.bind(this)}  />
            </div>);
        }
    }
    
}

interface LoginModalProps{
    visible:boolean,
    LoginEndCallback:(status:LoginProcessStatus)=>any,
    onCancel:()=>any
}

interface LoginModalStates{
    processing:boolean,
}

export class LoginModal extends React.Component<LoginModalProps,undefined>{


    constructor(props){
        super(props);
    }

    Footer = <div/>;

    render(){
        let CreatedForm = Form.create({})(loginForm);
        return <Modal footer={this.Footer} title="Login" visible={this.props.visible} onCancel={this.props.onCancel}>
        <CreatedForm LoginCallback={this.props.LoginEndCallback}/>
        </Modal>;
    }
}
