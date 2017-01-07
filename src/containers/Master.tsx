import * as React from 'react';
import { connect } from 'react-redux';
import { SiteLayout } from '../components/Layout';


export class Master extends React.Component<undefined,undefined>{
    render(){
        return <SiteLayout>
        {this.props.children}
        </SiteLayout>;
    }
}