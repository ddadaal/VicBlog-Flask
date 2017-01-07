import * as React from 'react';
import { Spin } from 'antd';
import {ArticleCard} from "./ArticleCard";
import { Utils } from "../Utils";

interface ArticleListStates {
    ArticleList: ArticleItem[]
}



export class ArticleList extends React.Component<undefined, ArticleListStates>{
    constructor() {
        super();
        this.state = {
            ArticleList: undefined
        };
    }
    render() {
        if (this.state.ArticleList) {
            if (this.state.ArticleList.length == 0) {
                return <div>No article available!</div>;
            } else {
                var parts = this.state.ArticleList.map(item => {
                    return <ArticleCard key={item.ID} ArticleItem={item} />
                });
                return <div className="Content">{parts}</div>;
            }
        } else {
            return <div><Spin />Loading</div>;
        }
    }

    componentDidMount() {
        this.updateList();
    }

    updateList() {
        let myInit: RequestInit = {
            method: 'GET',
            mode: 'cors',
            cache: 'default'
        };
        let list: ArticleItem[] = [];

        Utils.FetchJSON(Utils.APIS.articles, (json: any) => {
            json.map(item => {
                list.push(this.constructArticleItem(item));
            });
            this.setState({
                ArticleList: list
            });
        });
    }

    constructArticleItem(json: any): ArticleItem {
        return {
            Title: json.title,
            SubmitTime: json.submit_time,
            Username: json.username,
            ID: json.id,
            Categories: json.categories
        };
    }
}