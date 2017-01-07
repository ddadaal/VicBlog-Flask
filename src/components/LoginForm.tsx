import * as React from 'react';
import { Link } from 'react-router';
import { Form, Icon, Input, Button, Card, message } from 'antd';
import { Utils } from "./Utils";
const FormItem = Form.Item;

interface LoginFormProps {
    LoginCallback: (User: User) => any;
}

class loginForm extends React.Component<LoginFormProps, undefined>{
    constructor(props) {
        super(props);
    }

    handleSubmit(e: any) {
        e.preventDefault();
        (this.props as any).form.validateFields((err, values) => {
            if (!err) {
                console.log(values);

                Utils.FetchViaJSON(Utils.APIS.login, values, (json: any) => {
                    if (json.status == "success") {
                        this.props.LoginCallback({ Username: json.user.username });
                    } else {
                        message.error("Login failed");
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
                    <Button type="primary" htmlType="submit" className="login-form-button">
                        Log in
                    </Button>
                    <Link to="/register"><Button>Register</Button></Link>
                </FormItem>
            </Form>
        );
    }
}

export class LoginForm extends React.Component<LoginFormProps, undefined>{
    render() {
        let CreatedForm = Form.create({})(loginForm);
        return (
            <Card title="Login">
                <CreatedForm LoginCallback={this.props.LoginCallback} />
            </Card>
        );
    }
}