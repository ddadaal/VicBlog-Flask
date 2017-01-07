import * as React from 'react';
import { Card } from 'antd';

interface ArticleItemProps {
    Username : string,
    SubmitTime: Number
}

export class ArticleItem extends React.Component<ArticleItemProps,undefined>{
    constructor(props:ArticleItemProps){
        super(props);
    }
    render(){
        return <div/>;
    }
}