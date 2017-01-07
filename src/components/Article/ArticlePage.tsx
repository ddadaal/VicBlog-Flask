import * as React from 'react';
import ReactMarkdown from 'react-markdown';
import { Card, Spin, Layout, Tag } from 'antd';
var hljs = require("../../../node_modules/highlight.js/lib/highlight.js");
import "../../../node_modules/highlight.js/styles/default.css"
const { Header, Content } = Layout;
import { Utils} from "../Utils";

interface ArticlePageStates {
    Article: Article
}

export class ArticlePage extends React.Component<undefined, ArticlePageStates>{
    constructor() {
        super();
        this.state = {
            Article: undefined
        };

    }
    componentDidMount() {

        this.updateArticle((this.props as any).params.ID);
    }

    componentDidUpdate() {
        console.log("calling");
        hljs.initHighlighting();
    }

    updateArticle(id: number) {
        let myInit: RequestInit = {
            method: 'GET',
            mode: 'cors',
            cache: 'default'
        };

        Utils.FetchJSON(Utils.APIS.article+id.toString(),json=>{
            this.setState({
                    Article: this.constructArticle(json)
                });
        });
    }

    constructArticle(json: any): Article {
        return {
            Title: json.title,
            Content: json.content,
            SubmitTime: json.submit_time,
            Username: json.username,
            ID: json.id,
            Categories: json.categories
        };
    }

    render() {
        if (this.state.Article) {
            let tags = this.state.Article.Categories.map(item => {
                return <Tag key={item}>{item}</Tag>;
            });
            return (
                <div>
                    <div className="Content" >
                        <h1 style={{ textAlign: "Center" }}>{this.state.Article.Title}</h1>
                        <h3 style={{ textAlign: "Right" }}>{this.state.Article.SubmitTime}</h3>
                        <br />
                        {tags}
                        <div>
                            <ReactMarkdown source={this.state.Article.Content} />
                        </div>
                    </div>
                </div>
            );
        } else {
            return <div><Spin />Loading!</div>;
        }

    }
}