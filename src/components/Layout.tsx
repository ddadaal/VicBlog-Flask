import * as React from 'react';
import { Menu, Breadcrumb, Icon, Layout,Collapse   } from 'antd';
const { Header, Content, Sider } = Layout;
import { Link } from 'react-router';
import { SiteNavbar, Footer } from './SiteNavbar';
import { ProfileCard } from './ProfileCard';

interface LayoutProps { }

export class SiteLayout extends React.Component<LayoutProps, undefined>{
    constructor(props: LayoutProps) {
        super(props);
    }
    render() {
        return (
            <div style={{ background: "#f5f5f5" }}>
                <SiteNavbar />
                <div style={{ padding: '20px 50px 20px 50px' }}>
                    <Layout style={{ background: "#fff", margin: '6px 48px 24px 48px' }}>
                        <Content style={{ padding: '0px 50px 20px 50px' }}>
                            <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                                {this.props.children}
                            </div>
                        </Content>
                    </Layout>
                </div>
                <Footer />
            </div>
        );
    }
}