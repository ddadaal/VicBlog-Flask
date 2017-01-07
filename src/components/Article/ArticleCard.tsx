import * as React from 'react';
import { Card,Tag } from 'antd';
import { Link } from 'react-router';

interface ArticleCardProps {
    ArticleItem: IArticleItem
}

export class ArticleCard extends React.Component<ArticleCardProps,undefined>{
    constructor(props:ArticleCardProps){
        super(props);
    }
    render(){
        let url:string = `/articles/${this.props.ArticleItem.ID}`;
        let tags = this.props.ArticleItem.Categories.map(item=>{
            return <Tag>{item}</Tag>;
        });
        return (
            <Card style={{margin:"5px 5px 5px 5px"}} title={<Link to={url}>{this.props.ArticleItem.Title}</Link>} extra={<Link to={url}>More</Link>}>
            <div>
            {tags}
            </div>
            By {this.props.ArticleItem.Username}<br/>
            At {this.props.ArticleItem.SubmitTime}
            </Card>
        );
    }
}