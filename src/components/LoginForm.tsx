import * as React from 'react';
import { Link } from 'react-router';
import { Form, Icon, Input, Button, Card, message, Modal } from 'antd';
import { Utils } from "./Utils";
const FormItem = Form.Item;

interface LoginFormProps {
    LoginCallback: (status: LoginProcessStatus) => any;
}

interface LoginFormStates{
    processing:boolean
}

export class loginForm extends React.Component<LoginFormProps, LoginFormStates>{
    constructor(props) {
        super(props);
        this.state={
            processing:false
        };
    }

    handleSubmit(e: any) {
        e.preventDefault();
        (this.props as any).form.validateFields((err, values) => {
            if (!err) {
                this.setState({
                    processing:true
                });
                Utils.FetchViaJSON(Utils.APIS.login, values, (json: any) => {
                    this.setState({
                        processing:false
                    });
                    if (json.status == "success") {
                        this.props.LoginCallback({StatusText:"success",Payload:{ Username: json.user.username,Token:json.token }});
                    } else {
                        this.props.LoginCallback({StatusText:"failure",Payload:undefined});
                    }
                });
            }
        });
    }



    render() {
        const { getFieldDecorator } = (this.props as any).form;
        return (
            <Form onSubmit={this.handleSubmit.bind(this)} className="login-form">
                <FormItem >
                    {getFieldDecorator('username', {
                        rules: [{ required: true, message: 'Please input your username!' }],
                    })(
                        <Input addonBefore={<Icon type="user" />} placeholder="Username" />
                        )}
                </FormItem>
                <FormItem>
                    {getFieldDecorator('password', {
                        rules: [{ required: true, message: 'Please input your Password!' }],
                    })(
                        <Input addonBefore={<Icon type="lock" />} type="password" placeholder="Password" />
                        )}
                </FormItem>
                <FormItem>
                    <Button type="primary" htmlType="submit" className="login-form-button" loading={this.state.processing}>
                        Log in
                    </Button>
                    <Link to="/register"><Button>Register!</Button></Link>
                </FormItem>
            </Form>
        );
    }
}

export class LoginForm extends React.Component<LoginFormProps, undefined>{
    render() {
        let CreatedForm = Form.create({})(loginForm);
        return (
            <Modal title="Login" >
                <CreatedForm LoginCallback={this.props.LoginCallback} />
            </Modal>
        );
    }
}