import * as React from 'react';
import { Form, Icon, Input, Button, Checkbox } from 'antd';
import { Utils } from './Utils';
const FormItem = Form.Item;

interface RegisterPageStates{
    
}


export class registerPage extends React.Component<undefined,undefined>{

    handleRegister(e){
        e.preventDefault();
        (this.props as any).form.validateFields((err, values) => {
        if (!err) {
            Utils.FetchViaJSON(Utils.APIS.regsiter,values,json=>{

            });
        }
        });
    }

    render(){
        const { getFieldDecorator } = (this.props as any).form;
        return <Form onSubmit={this.handleRegister.bind(this)} className="login-form">
        <FormItem>
          {getFieldDecorator('userName', {
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
          {getFieldDecorator('remember', {
            valuePropName: 'checked',
            initialValue: true,
          })(
            <Checkbox>Remember me</Checkbox>
          )}
          <Button type="primary" htmlType="submit" className="login-form-button">
            Register
          </Button>
        </FormItem>
      </Form>
    }
}

export class RegisterPage extends React.Component<undefined,undefined>{
    
}