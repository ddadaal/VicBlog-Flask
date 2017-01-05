import * as React from 'react';
import { Link } from 'react-router';
import { Col, Row, Menu, Layout } from 'antd';
const { Header }= Layout;
import { AccountIndicator } from './AccountIndicator';

interface NavbarProps { selectedTab?:number }

export class SiteNavbar extends React.Component<NavbarProps,undefined>{
    constructor(props:NavbarProps){
        super(props);
    }
    render(){
        return (
            <Header style={{ background: "#fff" }}  >
            <Row gutter={0}>
            <Col span={2}>
            <img style={{margin: "10px 24px 16px 0", float: "right"}} src={require("../assets/LOGO4-Circle.jpg")} alt="VicBlog"/>
            </Col>
            <Col span={18}>
            <Menu style={{ fontSize:15, margin:"16px 0px 0px 0px"}} theme="light" mode="horizontal" defaultSelectedKeys={['1']}>
            <Menu.Item key='0'></Menu.Item>
            <Menu.Item key='1'><Link className="navLink" to="/">Home</Link></Menu.Item>
            <Menu.Item key='2'>Articles</Menu.Item>
            <Menu.Item key='3'><Link className="navLink" to="/about">About</Link></Menu.Item>
            </Menu>
            </Col>
            <Col span={4}>
            <AccountIndicator />
            </Col>
            </Row>
            </Header>
        );
    }
}

export class Footer extends React.Component<undefined,undefined>{
    constructor(){
        super();
    }
    render(){
        return (
            <div style={{textAlign:"Center"}}>
            <p>Code by VicCrubs</p>
            <p>Click <a href="https://github.com/viccrubs/VicBlog">here</a> for Github Repository</p>
            </div>
        );
    }
}