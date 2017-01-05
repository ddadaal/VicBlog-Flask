import * as React from 'react';
import { Menu, Breadcrumb, Icon, Layout } from 'antd';
const { Header, Content } = Layout;
import { Link } from 'react-router';
import { SiteNavbar, Footer } from './SiteNavbar';
interface LayoutProps { }

export class SiteLayout extends React.Component<LayoutProps, undefined>{
    constructor(props: LayoutProps) {
        super(props);
    }
    render() {
        return (
            <div style={{background:"#f5f5f5"}}>
                <SiteNavbar />
                <Content style={{ padding: '0px 50px 20px 50px' }}>>
                    <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                        {this.props.children}</div>
                </Content>
                <Footer />
            </div>
        );           
    }
}